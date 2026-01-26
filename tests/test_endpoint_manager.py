"""
Tests for endpoint manager HTTP client functionality.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from metorial._endpoint.endpoint_manager import MetorialEndpointManager
from metorial._endpoint.request import MetorialRequest
from metorial.exceptions import (
  AuthenticationError,
  BadRequestError,
  InternalServerError,
  MetorialSDKError,
  NotFoundError,
  RateLimitError,
)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def endpoint_manager() -> MetorialEndpointManager:
  """Create an endpoint manager for testing."""
  config = {"apiKey": "test-key"}
  return MetorialEndpointManager(
    config=config,
    api_host="https://api.metorial.com",
    get_headers=lambda c: {"Authorization": f"Bearer {c['apiKey']}"},
    enable_debug_logging=False,
  )


@pytest.fixture
def mock_response() -> MagicMock:
  """Create a mock HTTP response."""
  response = MagicMock()
  response.status_code = 200
  response.ok = True
  response.text = '{"data": "test"}'
  response.headers = {"Content-Type": "application/json"}
  response.json.return_value = {"data": "test"}
  return response


# =============================================================================
# Request ID Capture Tests
# =============================================================================


class TestRequestIdCapture:
  """Tests for X-Request-ID header capture in errors."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_request_id_on_400(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Request ID should be captured on 400 errors."""
    mock_request.return_value = MagicMock(
      status_code=400,
      ok=False,
      text='{"message": "Bad request"}',
      headers={"X-Request-ID": "req-bad-400", "Content-Type": "application/json"},
      json=MagicMock(return_value={"message": "Bad request"}),
      reason="Bad Request",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(BadRequestError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.request_id == "req-bad-400"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_request_id_on_401(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Request ID should be captured on 401 errors."""
    mock_request.return_value = MagicMock(
      status_code=401,
      ok=False,
      text='{"message": "Unauthorized"}',
      headers={"X-Request-ID": "req-auth-401"},
      json=MagicMock(return_value={"message": "Unauthorized"}),
      reason="Unauthorized",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(AuthenticationError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.request_id == "req-auth-401"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_request_id_on_404(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Request ID should be captured on 404 errors."""
    mock_request.return_value = MagicMock(
      status_code=404,
      ok=False,
      text='{"message": "Not found"}',
      headers={"X-Request-ID": "req-notfound-404"},
      json=MagicMock(return_value={"message": "Not found"}),
      reason="Not Found",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(NotFoundError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.request_id == "req-notfound-404"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_request_id_on_429(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Request ID should be captured on 429 errors (after retries exhausted)."""
    mock_request.return_value = MagicMock(
      status_code=429,
      ok=False,
      text='{"message": "Rate limited"}',
      headers={"X-Request-ID": "req-rate-429"},
      json=MagicMock(return_value={"message": "Rate limited"}),
      reason="Too Many Requests",
    )

    request = MetorialRequest(path="/test")
    # After 3 retries, should raise RateLimitError
    with pytest.raises(RateLimitError) as exc_info:
      endpoint_manager._request("GET", request, try_count=3)

    assert exc_info.value.request_id == "req-rate-429"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_request_id_on_500(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Request ID should be captured on 500 errors."""
    mock_request.return_value = MagicMock(
      status_code=500,
      ok=False,
      text='{"message": "Internal server error"}',
      headers={"X-Request-ID": "req-server-500"},
      json=MagicMock(return_value={"message": "Internal server error"}),
      reason="Internal Server Error",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(InternalServerError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.request_id == "req-server-500"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_handles_missing_request_id(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should handle responses without X-Request-ID header."""
    mock_request.return_value = MagicMock(
      status_code=400,
      ok=False,
      text='{"message": "Bad request"}',
      headers={},  # No X-Request-ID
      json=MagicMock(return_value={"message": "Bad request"}),
      reason="Bad Request",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(BadRequestError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.request_id is None


# =============================================================================
# Error Message Extraction Tests
# =============================================================================


class TestErrorMessageExtraction:
  """Tests for error message extraction from responses."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_extracts_message_from_message_field(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should extract message from 'message' field."""
    mock_request.return_value = MagicMock(
      status_code=400,
      ok=False,
      text='{"message": "Custom error message"}',
      headers={"X-Request-ID": "req-123"},
      json=MagicMock(return_value={"message": "Custom error message"}),
      reason="Bad Request",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(BadRequestError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.message == "Custom error message"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_extracts_message_from_error_field(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should extract message from 'error' field when 'message' is missing."""
    mock_request.return_value = MagicMock(
      status_code=400,
      ok=False,
      text='{"error": "Error description"}',
      headers={"X-Request-ID": "req-123"},
      json=MagicMock(return_value={"error": "Error description"}),
      reason="Bad Request",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(BadRequestError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.message == "Error description"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_falls_back_to_reason_phrase(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should fall back to HTTP reason phrase when no message in body."""
    mock_request.return_value = MagicMock(
      status_code=400,
      ok=False,
      text='{"code": "ERROR_CODE"}',  # No message or error field
      headers={"X-Request-ID": "req-123"},
      json=MagicMock(return_value={"code": "ERROR_CODE"}),
      reason="Bad Request",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(BadRequestError) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.message == "Bad Request"

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_handles_string_response_body(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should handle string response body."""
    mock_request.return_value = MagicMock(
      status_code=500,
      ok=False,
      text="Plain text error",
      headers={"X-Request-ID": "req-123"},
      json=MagicMock(side_effect=ValueError("Not JSON")),
      reason="Internal Server Error",
    )

    request = MetorialRequest(path="/test")
    # Should raise MetorialSDKError due to malformed response
    with pytest.raises(MetorialSDKError):
      endpoint_manager._request("GET", request)


# =============================================================================
# Response Body Capture Tests
# =============================================================================


class TestResponseBodyCapture:
  """Tests for response body capture in errors."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_dict_body(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should capture dict response body."""
    body = {"message": "Error", "details": {"field": "invalid"}}
    mock_request.return_value = MagicMock(
      status_code=422,
      ok=False,
      text='{"message": "Error", "details": {"field": "invalid"}}',
      headers={"X-Request-ID": "req-123"},
      json=MagicMock(return_value=body),
      reason="Unprocessable Entity",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(Exception) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.body == body

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_captures_validation_errors(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should capture validation error details."""
    body = {
      "message": "Validation failed",
      "errors": [
        {"field": "email", "message": "Invalid format"},
        {"field": "password", "message": "Too short"},
      ],
    }
    mock_request.return_value = MagicMock(
      status_code=422,
      ok=False,
      text="...",
      headers={"X-Request-ID": "req-validation"},
      json=MagicMock(return_value=body),
      reason="Unprocessable Entity",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(Exception) as exc_info:
      endpoint_manager._request("GET", request)

    assert exc_info.value.body["errors"][0]["field"] == "email"


# =============================================================================
# Successful Response Tests
# =============================================================================


class TestSuccessfulResponses:
  """Tests for successful response handling."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_returns_json_for_200(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should return parsed JSON for 200 response."""
    mock_request.return_value = MagicMock(
      status_code=200,
      ok=True,
      text='{"data": "test"}',
      headers={},
      json=MagicMock(return_value={"data": "test"}),
    )

    request = MetorialRequest(path="/test")
    result = endpoint_manager._request("GET", request)

    assert result == {"data": "test"}

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_returns_empty_dict_for_204(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should return empty dict for 204 No Content."""
    mock_request.return_value = MagicMock(
      status_code=204,
      ok=True,
      text="",
      headers={},
    )

    request = MetorialRequest(path="/test")
    result = endpoint_manager._request("DELETE", request)

    assert result == {}


# =============================================================================
# Network Error Tests
# =============================================================================


class TestNetworkErrors:
  """Tests for network error handling."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_raises_sdk_error_on_connection_error(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should raise MetorialSDKError on connection error."""
    mock_request.side_effect = ConnectionError("Connection refused")

    request = MetorialRequest(path="/test")
    with pytest.raises(MetorialSDKError) as exc_info:
      endpoint_manager._request("GET", request)

    assert "Unable to connect" in str(exc_info.value)

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_raises_sdk_error_on_timeout(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should raise MetorialSDKError on timeout."""
    import requests

    mock_request.side_effect = requests.Timeout("Request timed out")

    request = MetorialRequest(path="/test")
    with pytest.raises(MetorialSDKError) as exc_info:
      endpoint_manager._request("GET", request)

    assert "Unable to connect" in str(exc_info.value)


# =============================================================================
# Status Code Mapping Tests
# =============================================================================


class TestStatusCodeMapping:
  """Tests for HTTP status code to exception mapping."""

  @pytest.mark.parametrize(
    "status,expected_exception",
    [
      (400, BadRequestError),
      (401, AuthenticationError),
      (404, NotFoundError),
      (429, RateLimitError),
      (500, InternalServerError),
      (502, InternalServerError),
      (503, InternalServerError),
    ],
  )
  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_maps_status_to_correct_exception(
    self,
    mock_request: MagicMock,
    endpoint_manager: MetorialEndpointManager,
    status: int,
    expected_exception: type,
  ) -> None:
    """Should map HTTP status codes to correct exception types."""
    mock_request.return_value = MagicMock(
      status_code=status,
      ok=False,
      text='{"message": "Error"}',
      headers={"X-Request-ID": "req-test"},
      json=MagicMock(return_value={"message": "Error"}),
      reason="Error",
    )

    request = MetorialRequest(path="/test")

    # Skip retry for 429 by setting try_count to 3
    try_count = 3 if status == 429 else 0

    with pytest.raises(expected_exception):
      endpoint_manager._request("GET", request, try_count=try_count)


# =============================================================================
# Debug Logging Tests
# =============================================================================


class TestDebugLogging:
  """Tests for debug logging functionality."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  @patch("metorial._endpoint.endpoint_manager.logger")
  def test_logs_request_when_debug_enabled(
    self,
    mock_logger: MagicMock,
    mock_request: MagicMock,
  ) -> None:
    """Should log request when debug logging is enabled."""
    config = {"apiKey": "test-key"}
    manager = MetorialEndpointManager(
      config=config,
      api_host="https://api.metorial.com",
      get_headers=lambda c: {},
      enable_debug_logging=True,
    )

    mock_request.return_value = MagicMock(
      status_code=200,
      ok=True,
      text='{"data": "test"}',
      headers={},
      json=MagicMock(return_value={"data": "test"}),
    )

    request = MetorialRequest(path="/test")
    manager._request("GET", request)

    mock_logger.debug.assert_called()

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  @patch("metorial._endpoint.endpoint_manager.logger")
  def test_logs_error_with_request_id_when_debug_enabled(
    self,
    mock_logger: MagicMock,
    mock_request: MagicMock,
  ) -> None:
    """Should log error with request ID when debug logging is enabled."""
    config = {"apiKey": "test-key"}
    manager = MetorialEndpointManager(
      config=config,
      api_host="https://api.metorial.com",
      get_headers=lambda c: {},
      enable_debug_logging=True,
    )

    mock_request.return_value = MagicMock(
      status_code=400,
      ok=False,
      text='{"message": "Error"}',
      headers={"X-Request-ID": "req-debug-test"},
      json=MagicMock(return_value={"message": "Error"}),
      reason="Bad Request",
    )

    request = MetorialRequest(path="/test")
    with pytest.raises(BadRequestError):
      manager._request("GET", request)

    # Verify error was logged with request_id
    mock_logger.error.assert_called()
    call_args = str(mock_logger.error.call_args)
    assert "req-debug-test" in call_args


# =============================================================================
# URL Construction Tests
# =============================================================================


class TestUrlConstruction:
  """Tests for URL construction."""

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_constructs_url_from_string_path(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should construct URL from string path."""
    mock_request.return_value = MagicMock(
      status_code=200,
      ok=True,
      text="{}",
      headers={},
      json=MagicMock(return_value={}),
    )

    request = MetorialRequest(path="users/123")
    endpoint_manager._request("GET", request)

    # requests.request is called with positional args: method, url
    call_args = mock_request.call_args
    called_url = (
      call_args.args[1] if len(call_args.args) > 1 else call_args.kwargs.get("url")
    )
    assert "users/123" in called_url

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_constructs_url_from_list_path(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should construct URL from list path."""
    mock_request.return_value = MagicMock(
      status_code=200,
      ok=True,
      text="{}",
      headers={},
      json=MagicMock(return_value={}),
    )

    request = MetorialRequest(path=["users", "123", "sessions"])
    endpoint_manager._request("GET", request)

    # requests.request is called with positional args: method, url
    call_args = mock_request.call_args
    called_url = (
      call_args.args[1] if len(call_args.args) > 1 else call_args.kwargs.get("url")
    )
    assert "users/123/sessions" in called_url

  @patch("metorial._endpoint.endpoint_manager.requests.request")
  def test_uses_custom_host(
    self, mock_request: MagicMock, endpoint_manager: MetorialEndpointManager
  ) -> None:
    """Should use custom host when specified."""
    mock_request.return_value = MagicMock(
      status_code=200,
      ok=True,
      text="{}",
      headers={},
      json=MagicMock(return_value={}),
    )

    request = MetorialRequest(
      path="test",
      host="https://custom.metorial.com",
    )
    endpoint_manager._request("GET", request)

    # requests.request is called with positional args: method, url
    call_args = mock_request.call_args
    called_url = (
      call_args.args[1] if len(call_args.args) > 1 else call_args.kwargs.get("url")
    )
    assert "custom.metorial.com" in called_url
