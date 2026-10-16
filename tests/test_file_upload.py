from __future__ import annotations

import io
import json
import os
import threading
import zipfile
from collections.abc import Iterator
from email.parser import BytesParser
from email.policy import HTTP
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

import pytest

from metorial._endpoint import MetorialEndpointManager
from metorial._file_upload import upload_file
from metorial.exceptions import MetorialSDKError

FILE_RESPONSE = {
  "object": "file",
  "id": "file_1",
  "status": "active",
  "file_name": "notes.txt",
  "file_size": 5,
  "file_type": "text/plain",
  "title": None,
  "purpose": {"name": "Generic", "identifier": "generic"},
  "created_at": "2026-01-01T00:00:00.000Z",
  "updated_at": "2026-01-01T00:00:00.000Z",
}


class FakeFilesApi:
  def __init__(self) -> None:
    self.requests: list[dict[str, Any]] = []
    self.storage_status = 200
    self.api_status = 200

  def handle(self, handler: BaseHTTPRequestHandler) -> None:
    length = int(handler.headers.get("Content-Length") or 0)
    body = handler.rfile.read(length)
    content_type = handler.headers.get("Content-Type") or ""
    record: dict[str, Any] = {
      "method": handler.command,
      "path": handler.path,
      "headers": dict(handler.headers),
      "body": body,
    }
    self.requests.append(record)

    if handler.command == "PUT":
      handler.send_response(self.storage_status)
      handler.end_headers()
      if self.storage_status != 200:
        handler.wfile.write(b"SignatureDoesNotMatch")
      return

    if self.api_status != 200:
      self._json(
        handler, self.api_status, {"status": "error", "message": "Unknown file purpose"}
      )
      return

    if content_type.startswith("multipart/form-data"):
      record["form"], record["files"] = parse_multipart(content_type, body)
      self._json(handler, 200, FILE_RESPONSE)
      return

    payload = json.loads(body)
    record["json"] = payload
    if payload["mode"] == "get_upload_url":
      host = handler.headers["Host"]
      self._json(
        handler,
        200,
        {
          "object": "file_upload",
          "id": "fup_1",
          "upload": {"url": f"http://{host}/storage", "method": "PUT"},
        },
      )
    else:
      self._json(handler, 200, {**FILE_RESPONSE, "id": "file_2"})

  def _json(self, handler: BaseHTTPRequestHandler, status: int, value: Any) -> None:
    data = json.dumps(value).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def parse_multipart(
  content_type: str, body: bytes
) -> tuple[dict[str, str], dict[str, tuple[str, str, bytes]]]:
  message = BytesParser(policy=HTTP).parsebytes(
    f"Content-Type: {content_type}\r\n\r\n".encode() + body
  )
  form: dict[str, str] = {}
  files: dict[str, tuple[str, str, bytes]] = {}
  for part in message.iter_parts():
    name = part.get_param("name", header="content-disposition")
    payload = part.get_payload(decode=True)
    filename = part.get_filename()
    if filename:
      files[str(name)] = (filename, part.get_content_type(), payload)
    else:
      form[str(name)] = payload.decode()
  return form, files


@pytest.fixture
def api() -> Iterator[tuple[FakeFilesApi, MetorialEndpointManager]]:
  fake = FakeFilesApi()

  class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
      fake.handle(self)

    def do_PUT(self) -> None:
      fake.handle(self)

    def log_message(self, *args: Any) -> None:
      pass

  server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
  thread = threading.Thread(target=server.serve_forever, daemon=True)
  thread.start()

  manager = MetorialEndpointManager(
    {},
    f"http://127.0.0.1:{server.server_address[1]}",
    lambda _: {"Authorization": "Bearer metorial_sk_test"},
  )
  try:
    yield fake, manager
  finally:
    server.shutdown()


def upload(manager: MetorialEndpointManager, file: Any, **kwargs: Any) -> Any:
  options: dict[str, Any] = {
    "purpose": "generic",
    "title": None,
    "file_name": None,
    "content_type": None,
    "store_id": None,
    "store_path": None,
    "store_replace": False,
    "instance_id": None,
  }
  options.update(kwargs)
  return upload_file(manager, file, **options)


def test_small_files_are_sent_as_multipart(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  fake, manager = api
  local = tmp_path / "notes.txt"
  local.write_text("hello")

  result = upload(
    manager,
    local,
    title="Notes",
    instance_id="inst_1",
    store_id="store_1",
    store_path="docs/notes.txt",
    store_replace=True,
  )

  assert result.id == "file_1"
  [request] = fake.requests
  assert request["path"] == "/files"
  assert request["form"] == {
    "purpose": "generic",
    "title": "Notes",
    "instance_id": "inst_1",
    "store_id": "store_1",
    "path": "docs/notes.txt",
    "store_replace": "true",
  }
  assert request["files"]["file"] == ("notes.txt", "text/plain", b"hello")


def test_directories_are_zipped(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  fake, manager = api
  context = tmp_path / "context"
  (context / "src").mkdir(parents=True)
  (context / "empty").mkdir()
  (context / "Dockerfile").write_text("FROM alpine")
  (context / "src" / "main.py").write_text("print('hi')")
  os.symlink("Dockerfile", context / "link")

  upload(manager, str(context), purpose="sandbox_image_build_context")

  name, content_type, data = fake.requests[0]["files"]["file"]
  assert (name, content_type) == ("context.zip", "application/zip")
  with zipfile.ZipFile(io.BytesIO(data)) as archive:
    assert sorted(archive.namelist()) == ["Dockerfile", "empty/", "src/", "src/main.py"]
    assert archive.read("src/main.py") == b"print('hi')"


def test_empty_directories_are_rejected(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  _, manager = api
  with pytest.raises(ValueError, match="no files"):
    upload(manager, tmp_path)


def test_bytes_and_streams_need_a_name(
  api: tuple[FakeFilesApi, MetorialEndpointManager],
) -> None:
  fake, manager = api
  with pytest.raises(ValueError, match="file_name"):
    upload(manager, b"hello")

  upload(manager, io.BytesIO(b"hello"), file_name="hello.json")
  assert fake.requests[0]["files"]["file"] == (
    "hello.json",
    "application/json",
    b"hello",
  )


def test_large_files_use_an_upload_url(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  fake, manager = api
  local = tmp_path / "archive.bin"
  local.write_bytes(b"large contents")

  result = upload(
    manager, local, purpose="skill_export", instance_id="inst_1", direct_limit=4
  )

  assert result.id == "file_2"
  get_url, put, complete = fake.requests
  assert get_url["json"] == {
    "mode": "get_upload_url",
    "file_name": "archive.bin",
    "file_size": len(b"large contents"),
    "file_type": "application/octet-stream",
    "purpose": "skill_export",
    "instance_id": "inst_1",
  }
  assert put["method"] == "PUT"
  assert put["body"] == b"large contents"
  assert put["headers"]["Content-Type"] == "application/octet-stream"
  assert "Authorization" not in put["headers"]
  assert complete["json"] == {
    "mode": "complete",
    "file_upload_id": "fup_1",
    "instance_id": "inst_1",
  }


def test_storage_failures_are_reported(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  fake, manager = api
  fake.storage_status = 403
  local = tmp_path / "archive.bin"
  local.write_bytes(b"large contents")

  with pytest.raises(MetorialSDKError, match="storage responded with 403"):
    upload(manager, local, direct_limit=4)


def test_api_errors_are_raised(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  fake, manager = api
  fake.api_status = 400
  local = tmp_path / "notes.txt"
  local.write_text("hello")

  with pytest.raises(MetorialSDKError, match="Unknown file purpose"):
    upload(manager, local, purpose="nope")


def test_store_options_are_validated(
  api: tuple[FakeFilesApi, MetorialEndpointManager], tmp_path: Path
) -> None:
  _, manager = api
  with pytest.raises(ValueError, match="together"):
    upload(manager, b"x", file_name="x.txt", store_id="store_1")
  with pytest.raises(ValueError, match="store_replace"):
    upload(manager, b"x", file_name="x.txt", store_replace=True)
