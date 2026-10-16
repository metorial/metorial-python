from __future__ import annotations

import io
import logging
import mimetypes
import os
import tempfile
import zipfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import IO, Any, Union

import requests

from metorial._endpoint import MetorialEndpointManager, MetorialRequest
from metorial._generated.magnetar.resources import (
  DashboardInstanceFilesGetOutput,
  mapDashboardInstanceFilesGetOutput,
)
from metorial.exceptions import MetorialSDKError

logger = logging.getLogger(__name__)

# Must stay in sync with maxDirectUploadSize in the files API.
MAX_DIRECT_UPLOAD_SIZE = 100 * 1024 * 1024

UPLOAD_TIMEOUT_SECONDS = 30

FileSource = Union[str, "os.PathLike[str]", bytes, IO[bytes]]


@dataclass
class _Source:
  stream: IO[bytes]
  name: str
  content_type: str
  size: int


def upload_file(
  manager: MetorialEndpointManager,
  file: FileSource,
  *,
  purpose: str,
  title: str | None,
  file_name: str | None,
  content_type: str | None,
  store_id: str | None,
  store_path: str | None,
  store_replace: bool,
  instance_id: str | None,
  direct_limit: int = MAX_DIRECT_UPLOAD_SIZE,
) -> DashboardInstanceFilesGetOutput:
  if (store_id is None) != (store_path is None):
    raise ValueError("store_id and store_path must be given together")
  if store_replace and store_id is None:
    raise ValueError("store_replace requires store_id and store_path")

  fields: dict[str, Any] = {"purpose": purpose}
  if title is not None:
    fields["title"] = title
  if instance_id is not None:
    fields["instance_id"] = instance_id
  if store_id is not None:
    fields["store_id"] = store_id
    fields["path"] = store_path
    fields["store_replace"] = store_replace

  with _open_source(file, file_name, content_type) as source:
    if source.size <= direct_limit:
      data = _upload_direct(manager, source, fields)
    else:
      data = _upload_with_url(manager, source, fields, instance_id)

  return mapDashboardInstanceFilesGetOutput.from_dict(data)


def _upload_direct(
  manager: MetorialEndpointManager, source: _Source, fields: dict[str, Any]
) -> Any:
  form = {
    key: ("true" if value else "false") if isinstance(value, bool) else str(value)
    for key, value in fields.items()
  }
  # Read into memory so the 429 retry in the endpoint manager can resend the body.
  content = source.stream.read()
  request = MetorialRequest(
    path=["files"],
    files={"file": (source.name, content, source.content_type)},
    data=form,
  )
  return manager._request("POST", request)


def _upload_with_url(
  manager: MetorialEndpointManager,
  source: _Source,
  fields: dict[str, Any],
  instance_id: str | None,
) -> Any:
  session = manager._request(
    "POST",
    MetorialRequest(
      path=["files"],
      body={
        "mode": "get_upload_url",
        "file_name": source.name,
        "file_size": source.size,
        "file_type": source.content_type,
        **fields,
      },
    ),
  )

  upload = session.get("upload") if isinstance(session, dict) else None
  if not isinstance(upload, dict) or not upload.get("url") or not session.get("id"):
    raise MetorialSDKError(
      {
        "status": 0,
        "code": "malformed_response",
        "message": "The Metorial API did not return an upload URL.",
      }
    )

  _put_to_storage(upload.get("method") or "PUT", upload["url"], source)

  complete: dict[str, Any] = {"mode": "complete", "file_upload_id": session["id"]}
  if instance_id is not None:
    complete["instance_id"] = instance_id
  return manager._request("POST", MetorialRequest(path=["files"], body=complete))


def _put_to_storage(method: str, url: str, source: _Source) -> None:
  # The URL signature covers the content type, so it must match the declared
  # file_type, and Metorial credentials must not be sent to the storage backend.
  try:
    response = requests.request(
      method,
      url,
      data=source.stream,
      headers={
        "Content-Type": source.content_type,
        "Content-Length": str(source.size),
      },
      timeout=UPLOAD_TIMEOUT_SECONDS,
    )
  except Exception as error:
    raise MetorialSDKError(
      {
        "status": 0,
        "code": "network_error",
        "message": f"Failed to upload {source.name} to storage",
        "error": str(error),
      }
    ) from error

  if not response.ok:
    raise MetorialSDKError(
      {
        "status": response.status_code,
        "code": "upload_failed",
        "message": f"Failed to upload {source.name}: storage responded with {response.status_code}",
        "body_snippet": (response.text or "")[:1000],
      }
    )


@contextmanager
def _open_source(
  file: FileSource, file_name: str | None, content_type: str | None
) -> Iterator[_Source]:
  if isinstance(file, (bytes, bytearray)):
    if not file_name:
      raise ValueError("file_name is required when uploading bytes")
    yield _Source(
      stream=io.BytesIO(file),
      name=file_name,
      content_type=content_type or _guess_content_type(file_name),
      size=len(file),
    )
    return

  if isinstance(file, (str, os.PathLike)):
    path = os.path.abspath(os.fspath(file))
    if os.path.isdir(path):
      with _zip_directory(path) as archive:
        name = file_name or os.path.basename(path.rstrip(os.sep)) + ".zip"
        with open(archive, "rb") as stream:
          yield _Source(
            stream=stream,
            name=name,
            content_type=content_type or "application/zip",
            size=os.path.getsize(archive),
          )
      return

    name = file_name or os.path.basename(path)
    with open(path, "rb") as stream:
      yield _Source(
        stream=stream,
        name=name,
        content_type=content_type or _guess_content_type(name),
        size=os.fstat(stream.fileno()).st_size,
      )
    return

  name = file_name or os.path.basename(str(getattr(file, "name", "") or ""))
  if not name:
    raise ValueError("file_name is required when uploading a stream without a name")

  if file.seekable():
    start = file.tell()
    size = file.seek(0, io.SEEK_END) - start
    file.seek(start)
    readable: IO[bytes] = file
  else:
    content = file.read()
    readable = io.BytesIO(content)
    size = len(content)

  yield _Source(
    stream=readable,
    name=name,
    content_type=content_type or _guess_content_type(name),
    size=size,
  )


@contextmanager
def _zip_directory(directory: str) -> Iterator[str]:
  """Zips the directory's contents (not the directory itself) into a temporary
  file. Symlinks and special files are skipped."""
  handle, archive = tempfile.mkstemp(prefix="metorial-upload-", suffix=".zip")
  os.close(handle)

  try:
    files = 0
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
      for root, directories, names in os.walk(directory):
        directories.sort()
        for name in directories:
          path = os.path.join(root, name)
          if os.path.islink(path):
            logger.warning("Skipping %s: not a regular file", path)
            continue
          zip_file.write(path, os.path.relpath(path, directory))

        for name in sorted(names):
          path = os.path.join(root, name)
          if os.path.islink(path) or not os.path.isfile(path):
            logger.warning("Skipping %s: not a regular file", path)
            continue
          if os.path.samefile(path, archive):
            continue
          zip_file.write(path, os.path.relpath(path, directory))
          files += 1

    if files == 0:
      raise ValueError(f"{directory} has no files to upload")

    yield archive
  finally:
    os.remove(archive)


def _guess_content_type(name: str) -> str:
  return mimetypes.guess_type(name)[0] or "application/octet-stream"
