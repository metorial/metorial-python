from __future__ import annotations

from typing import Any, Dict, Optional, Union, Callable
from urllib.parse import urljoin
import time

import requests


class MetorialSDKError(Exception):
    """Unified error that carries HTTP/status info and the raw payload.

    Attributes
    ----------
    status: int
        HTTP status code (0 for network errors).
    code: str
        Error code returned by the API or synthesized locally.
    message: str
        Human readable message.
    data: Dict[str, Any]
        Full decoded error body (if JSON) or a dict with snippet/meta when not JSON.
    """

    def __init__(self, data: Dict[str, Any]):
        self.status: int = int(data.get("status", 0))
        self.code: str = data.get("code", "unknown_error")
        self.message: str = data.get("message", "Unknown error")
        self.data: Dict[str, Any] = data
        super().__init__(f"[{self.code}] {self.message}")


class MetorialRequest:
    def __init__(
        self,
        path: Union[str, list[str]],
        host: Optional[str] = None,
        query: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
    ):
        self.path = path
        self.host = host
        self.query = query
        self.body = body


class MetorialEndpointManager:
    def __init__(
        self,
        config: Any,
        api_host: str,
        get_headers: Callable[[Any], Dict[str, str]],
        enable_debug_logging: bool = False,
    ):
        self.config = config
        self.api_host = api_host
        self.get_headers = get_headers
        self.enable_debug_logging = enable_debug_logging

    # --------------- internal HTTP helpers ---------------
    def _request(self, method: str, request: MetorialRequest, try_count: int = 0) -> Any:
        path = "/".join(request.path) if isinstance(request.path, list) else request.path
        base_url = request.host or self.api_host
        url = urljoin(base_url if base_url.endswith('/') else base_url + '/', path)

        params = request.query or {}
        headers = {"Accept": "application/json", **(self.get_headers(self.config) or {})}

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
            print(f"[Metorial] {method} {url}", {"body": request.body, "query": request.query})

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
                print(f"[Metorial] {method} {url} network error:", error)
            raise MetorialSDKError(
                {
                    "status": 0,
                    "code": "network_error",
                    "message": "Unable to connect to Metorial API - please check your internet connection",
                    "error": str(error),
                }
            )

        # simple retry on 429
        if resp.status_code == 429 and try_count < 3:
            retry_after = resp.headers.get("Retry-After")
            sleep_for = int(retry_after) + 3 if retry_after and retry_after.isdigit() else 3
            time.sleep(sleep_for)
            return self._request(method, request, try_count + 1)

        # Handle empty / no-content
        text = resp.text or ""
        if resp.status_code == 204 or not text.strip():
            data = {}
        else:
            # Try to decode JSON, otherwise raise malformed_response
            try:
                data = resp.json()
            except Exception as err:
                if self.enable_debug_logging:
                    print(f"[Metorial] {method} {url} decode error:", err)
                    print("RAW RESPONSE (first 500 chars):", text[:500])
                raise MetorialSDKError(
                    {
                        "status": resp.status_code,
                        "code": "malformed_response",
                        "message": "The Metorial API returned an unexpected response. Expected JSON.",
                        "content_type": resp.headers.get("content-type"),
                        "body_snippet": text[:1000],
                    }
                )

        if not resp.ok:
            # API returned structured JSON error OR we synthesize one
            if self.enable_debug_logging:
                print(f"[Metorial] {method} {url} error:", data)
            if isinstance(data, dict) and "code" in data:
                raise MetorialSDKError(data)
            raise MetorialSDKError(
                {
                    "status": resp.status_code,
                    "code": data.get("code", "http_error") if isinstance(data, dict) else "http_error",
                    "message": data.get("message", resp.reason) if isinstance(data, dict) else resp.reason,
                    "raw": data,
                }
            )

        if self.enable_debug_logging:
            print(f"[Metorial] {method} {url}", data)
        return data

    # --------------- transform helpers ---------------
    def _request_and_transform(self, method: str, request: MetorialRequest):
        manager = self

        class Transformer:
            def transform(self_inner, mapper):
                data = manager._request(method, request)
                # Support both generated mapper functions and objects with transformFrom
                if hasattr(mapper, "transformFrom"):
                    return mapper.transformFrom(data)
                return mapper(data)

        return Transformer()

    # --------------- public verbs ---------------
    def _get(self, request: MetorialRequest):
        return self._request_and_transform("GET", request)

    def _post(self, request: MetorialRequest):
        return self._request_and_transform("POST", request)

    def _put(self, request: MetorialRequest):
        return self._request_and_transform("PUT", request)

    def _patch(self, request: MetorialRequest):
        return self._request_and_transform("PATCH", request)

    def _delete(self, request: MetorialRequest):
        return self._request_and_transform("DELETE", request)


class BaseMetorialEndpoint:
    def __init__(self, manager: MetorialEndpointManager):
        self.manager = manager

    def _get(self, request: MetorialRequest):
        return self.manager._get(request)

    def _post(self, request: MetorialRequest):
        return self.manager._post(request)

    def _put(self, request: MetorialRequest):
        return self.manager._put(request)

    def _patch(self, request: MetorialRequest):
        return self.manager._patch(request)

    def _delete(self, request: MetorialRequest):
        return self.manager._delete(request)
