"""
Raw response wrapper for debugging and accessing HTTP response metadata.

Provides access to raw HTTP response details while still allowing
convenient access to the parsed response data.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
  import httpx
  from requests import Response as RequestsResponse

T = TypeVar("T")


class RawResponse(Generic[T]):
  """Wrapper providing access to raw HTTP response alongside parsed data.

  This class wraps an HTTP response and its parsed content, allowing
  users to access both the raw response metadata (headers, status code,
  request ID) and the parsed data.

  Example:
      response = await client.with_raw_response.sessions.create(...)
      print(response.request_id)
      print(response.headers)
      data = response.parse()
  """

  def __init__(
    self,
    response: httpx.Response | RequestsResponse,
    parsed: T,
  ) -> None:
    self._response = response
    self._parsed = parsed

  @property
  def headers(self) -> dict[str, str]:
    """Get response headers as a dictionary."""
    return dict(self._response.headers)

  @property
  def status_code(self) -> int:
    """Get HTTP status code."""
    return self._response.status_code

  @property
  def request_id(self) -> str | None:
    """Get X-Request-ID header value for debugging."""
    return self._response.headers.get("X-Request-ID")

  @property
  def content_type(self) -> str | None:
    """Get Content-Type header value."""
    return self._response.headers.get("Content-Type")

  @property
  def is_success(self) -> bool:
    """Check if the response indicates success (2xx status code)."""
    return 200 <= self._response.status_code < 300

  def parse(self) -> T:
    """Get the parsed response data.

    Returns:
        The parsed response data of type T
    """
    return self._parsed

  def __repr__(self) -> str:
    return (
      f"RawResponse(status_code={self.status_code}, "
      f"request_id={self.request_id!r}, "
      f"content_type={self.content_type!r})"
    )


class RawResponseWrapper(Generic[T]):
  """Wrapper that returns RawResponse objects from API calls.

  This is used to provide a `with_raw_response` interface that mirrors
  the normal API but returns RawResponse objects instead of just the
  parsed data.
  """

  def __init__(self, parsed: T, response: httpx.Response | RequestsResponse) -> None:
    self._parsed = parsed
    self._response = response

  def to_raw(self) -> RawResponse[T]:
    """Convert to a RawResponse object."""
    return RawResponse(self._response, self._parsed)


__all__ = ["RawResponse", "RawResponseWrapper"]
