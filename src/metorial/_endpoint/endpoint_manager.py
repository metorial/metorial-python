from __future__ import annotations

import logging
import time
from collections.abc import Callable
from typing import Any
from urllib.parse import urljoin

import requests

from metorial.exceptions import MetorialSDKError, make_status_error

from .request import MetorialRequest

logger = logging.getLogger(__name__)


class MetorialEndpointManager:
  """Main HTTP client manager for Metorial API requests.

  Handles request execution, error handling, retries, and response transformation.
  """

  def __init__(
    self,
    config: Any,
    api_host: str,
    get_headers: Callable[[Any], dict[str, str]],
    enable_debug_logging: bool = False,
  ):
    self.config = config
    self.api_host = api_host
    self.get_headers = get_headers
    self.enable_debug_logging = enable_debug_logging

  def _request(self, method: str, request: MetorialRequest, try_count: int = 0) -> Any:
    path = "/".join(request.path) if isinstance(request.path, list) else request.path
    base_url = request.host or self.api_host
    url = urljoin(base_url if base_url.endswith("/") else base_url + "/", path)

    params = request.query or {}
    headers = {
      "Accept": "application/json",
      **(self.get_headers(self.config) or {}),
    }

    has_body = method in {"POST", "PUT", "PATCH"}
    json_payload = None
    files_payload = None

    if has_body and request.body is not None:
      # If body is a file-like object, send as multipart
      if hasattr(request.body, "read"):
        files_payload = request.body
      else:
        json_payload = request.body
        headers.setdefault("Content-Type", "application/json")

    if self.enable_debug_logging:
      logger.debug(f"📡 {method} {url} body=%s query=%s", request.body, request.query)

    try:
      resp = requests.request(
        method,
        url,
        params=params,
        headers=headers,
        json=json_payload,
        files=files_payload,
        allow_redirects=True,
        timeout=30,
      )
    except Exception as error:
      if self.enable_debug_logging:
        logger.error(f"❌ {method} {url} network error: %s", error)
      raise MetorialSDKError(
        {
          "status": 0,
          "code": "network_error",
          "message": "Unable to connect to Metorial API - please check your internet connection",
          "error": str(error),
        }
      ) from error

    # simple retry on 429
    if resp.status_code == 429 and try_count < 3:
      retry_after = resp.headers.get("Retry-After")
      sleep_for = int(retry_after) + 3 if retry_after and retry_after.isdigit() else 3
      time.sleep(sleep_for)
      return self._request(method, request, try_count + 1)

    # Handle empty / no-content
    text = resp.text or ""
    data: Any  # Could be dict, list, str, etc. from JSON
    if resp.status_code == 204 or not text.strip():
      data = {}
    else:
      # Try to decode JSON, otherwise raise malformed_response
      try:
        data = resp.json()
      except Exception as err:
        if self.enable_debug_logging:
          logger.error(f"❌ {method} {url} decode error: %s", err)
          logger.debug("Raw response: %s", text[:500])
        raise MetorialSDKError(
          {
            "status": resp.status_code,
            "code": "malformed_response",
            "message": "The Metorial API returned an unexpected response. Expected JSON.",
            "content_type": resp.headers.get("content-type"),
            "body_snippet": text[:1000],
          }
        ) from err

    if not resp.ok:
      # Capture X-Request-ID header for debugging (Knock pattern)
      request_id = resp.headers.get("X-Request-ID")

      # API returned structured JSON error OR we synthesize one
      if self.enable_debug_logging:
        logger.error(f"❌ {method} {url} error: %s (request_id=%s)", data, request_id)

      # Extract message from response body
      if isinstance(data, dict):
        message = data.get("message") or data.get("error") or resp.reason
      else:
        message = str(data) if data else resp.reason

      # Use status-specific exception factory
      raise make_status_error(
        status=resp.status_code,
        message=message,
        request_id=request_id,
        body=data,
      )

    if self.enable_debug_logging:
      logger.debug(f"✅ {method} {url} response=%s", data)
    return data

  def _request_and_transform(self, method: str, request: MetorialRequest) -> Any:
    manager = self

    class Transformer:
      def transform(self_inner: Any, mapper: Any) -> Any:
        data = manager._request(method, request)
        if hasattr(mapper, "transformFrom"):
          return mapper.transformFrom(data)
        return mapper(data)

    return Transformer()

  def _get(self, request: MetorialRequest) -> Any:
    return self._request_and_transform("GET", request)

  def _post(self, request: MetorialRequest) -> Any:
    return self._request_and_transform("POST", request)

  def _put(self, request: MetorialRequest) -> Any:
    return self._request_and_transform("PUT", request)

  def _patch(self, request: MetorialRequest) -> Any:
    return self._request_and_transform("PATCH", request)

  def _delete(self, request: MetorialRequest) -> Any:
    return self._request_and_transform("DELETE", request)
