from __future__ import annotations

from types import TracebackType
from typing import Any
from urllib.parse import urlsplit

import httpx

from ._access import SandboxAccessCache
from ._errors import closed_error

_TOKEN_HEADER = "Metorial-Sandbox-Token"


class SandboxPort:
  def __init__(
    self,
    port: int,
    access: SandboxAccessCache,
    *,
    client: httpx.AsyncClient | None = None,
  ) -> None:
    self.port = port
    self._access = access
    self._client = client or httpx.AsyncClient()
    self._owns_client = client is None
    self._closed = False
    self._url = ""

  @classmethod
  async def connect(
    cls,
    port: int,
    access: SandboxAccessCache,
    *,
    client: httpx.AsyncClient | None = None,
  ) -> SandboxPort:
    connection = cls(port, access, client=client)
    connection._url = (await access.get()).url
    return connection

  @property
  def url(self) -> str:
    return self._url

  @property
  def is_closed(self) -> bool:
    return self._closed

  async def __aenter__(self) -> SandboxPort:
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc: BaseException | None,
    tb: TracebackType | None,
  ) -> None:
    await self.close()

  async def get_token(self) -> str:
    return (await self._access.get()).token

  async def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
    if self._closed:
      raise closed_error()

    headers = httpx.Headers(kwargs.pop("headers", None))

    async def send() -> httpx.Response:
      grant = await self._access.get()
      self._url = grant.url
      headers[_TOKEN_HEADER] = grant.token
      return await self._client.request(
        method, self._resolve(grant.url, path), headers=headers, **kwargs
      )

    response = await send()
    if response.status_code == 401:
      self._access.invalidate()
      response = await send()

    return response

  async def get(self, path: str, **kwargs: Any) -> httpx.Response:
    return await self.request("GET", path, **kwargs)

  async def head(self, path: str, **kwargs: Any) -> httpx.Response:
    return await self.request("HEAD", path, **kwargs)

  async def post(self, path: str, **kwargs: Any) -> httpx.Response:
    return await self.request("POST", path, **kwargs)

  async def put(self, path: str, **kwargs: Any) -> httpx.Response:
    return await self.request("PUT", path, **kwargs)

  async def patch(self, path: str, **kwargs: Any) -> httpx.Response:
    return await self.request("PATCH", path, **kwargs)

  async def delete(self, path: str, **kwargs: Any) -> httpx.Response:
    return await self.request("DELETE", path, **kwargs)

  async def close(self) -> None:
    if self._closed:
      return
    self._closed = True
    if self._owns_client:
      await self._client.aclose()

  def _resolve(self, base: str, path: str) -> str:
    if path.startswith(("http://", "https://")):
      target, origin = urlsplit(path), urlsplit(base)
      if (target.scheme, target.netloc) != (origin.scheme, origin.netloc):
        raise ValueError(f"{path} is not on the sandbox port {self.port}.")
      return path

    return f"{base.rstrip('/')}/{path.lstrip('/')}"
