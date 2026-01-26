"""
Tests for exception classes and make_status_error factory.
"""

import pytest

from metorial.exceptions import (
  AuthenticationError,
  BadRequestError,
  ConflictError,
  InternalServerError,
  MetorialAPIError,
  MetorialConfigError,
  MetorialConnectionError,
  MetorialDuplicateToolError,
  MetorialError,
  MetorialSDKError,
  MetorialSessionError,
  MetorialTimeoutError,
  MetorialToolError,
  NotFoundError,
  PermissionDeniedError,
  RateLimitError,
  UnprocessableEntityError,
  is_metorial_sdk_error,
  make_status_error,
)

# =============================================================================
# make_status_error Factory Tests
# =============================================================================


class TestMakeStatusError:
  """Tests for make_status_error factory function."""

  def test_returns_bad_request_error_for_400(self) -> None:
    err = make_status_error(400, "Bad request")
    assert isinstance(err, BadRequestError)
    assert err.status_code == 400
    assert err.message == "Bad request"

  def test_returns_authentication_error_for_401(self) -> None:
    err = make_status_error(401, "Invalid API key")
    assert isinstance(err, AuthenticationError)
    assert err.status_code == 401

  def test_returns_permission_denied_error_for_403(self) -> None:
    err = make_status_error(403, "Forbidden")
    assert isinstance(err, PermissionDeniedError)
    assert err.status_code == 403

  def test_returns_not_found_error_for_404(self) -> None:
    err = make_status_error(404, "Not found")
    assert isinstance(err, NotFoundError)
    assert err.status_code == 404

  def test_returns_conflict_error_for_409(self) -> None:
    err = make_status_error(409, "Conflict")
    assert isinstance(err, ConflictError)
    assert err.status_code == 409

  def test_returns_unprocessable_entity_error_for_422(self) -> None:
    err = make_status_error(422, "Validation failed")
    assert isinstance(err, UnprocessableEntityError)
    assert err.status_code == 422

  def test_returns_rate_limit_error_for_429(self) -> None:
    err = make_status_error(429, "Rate limited", request_id="req-123")
    assert isinstance(err, RateLimitError)
    assert err.status_code == 429
    assert err.request_id == "req-123"

  def test_returns_internal_server_error_for_500(self) -> None:
    err = make_status_error(500, "Internal server error")
    assert isinstance(err, InternalServerError)
    assert err.status_code == 500

  def test_returns_internal_server_error_for_502(self) -> None:
    err = make_status_error(502, "Bad gateway")
    assert isinstance(err, InternalServerError)
    assert err.status_code == 502

  def test_returns_internal_server_error_for_503(self) -> None:
    err = make_status_error(503, "Service unavailable")
    assert isinstance(err, InternalServerError)
    assert err.status_code == 503

  def test_returns_internal_server_error_for_504(self) -> None:
    err = make_status_error(504, "Gateway timeout")
    assert isinstance(err, InternalServerError)
    assert err.status_code == 504

  def test_returns_generic_api_error_for_unknown_status(self) -> None:
    err = make_status_error(418, "I'm a teapot")
    assert isinstance(err, MetorialAPIError)
    assert not isinstance(err, BadRequestError)
    assert err.status_code == 418

  def test_returns_generic_api_error_for_uncommon_4xx(self) -> None:
    for status in [402, 405, 406, 407, 408, 410, 411, 412, 413, 414, 415]:
      err = make_status_error(status, f"Error {status}")
      assert isinstance(err, MetorialAPIError)
      assert err.status_code == status

  def test_includes_request_id(self) -> None:
    err = make_status_error(404, "Not found", request_id="req-abc-123")
    assert err.request_id == "req-abc-123"
    assert "request_id=req-abc-123" in str(err)

  def test_includes_body_dict(self) -> None:
    body = {"error": "details", "code": "RESOURCE_NOT_FOUND"}
    err = make_status_error(404, "Not found", body=body)
    assert err.body == body

  def test_includes_body_string(self) -> None:
    body = "Raw error text"
    err = make_status_error(500, "Server error", body=body)
    assert err.body == body

  def test_all_parameters_together(self) -> None:
    body = {"detail": "User not found"}
    err = make_status_error(
      status=404,
      message="User not found",
      request_id="req-xyz-789",
      body=body,
    )
    assert err.status_code == 404
    assert err.message == "User not found"
    assert err.request_id == "req-xyz-789"
    assert err.body == body


# =============================================================================
# Exception String Representation Tests
# =============================================================================


class TestExceptionStringRepresentation:
  """Tests for exception __str__ method."""

  def test_str_includes_message_and_status(self) -> None:
    err = make_status_error(404, "Resource not found")
    s = str(err)
    assert "Resource not found" in s
    assert "status=404" in s

  def test_str_includes_request_id_when_present(self) -> None:
    err = make_status_error(500, "Server error", request_id="req-xyz")
    s = str(err)
    assert "request_id=req-xyz" in s

  def test_str_without_request_id(self) -> None:
    err = make_status_error(400, "Bad request")
    s = str(err)
    assert "request_id" not in s

  def test_str_with_empty_request_id(self) -> None:
    err = make_status_error(400, "Bad request", request_id="")
    s = str(err)
    # Empty string is falsy, so should not appear
    assert "request_id=" not in s

  def test_str_format_consistency(self) -> None:
    """Verify string format is consistent across exception types."""
    error_classes = [
      (400, BadRequestError),
      (401, AuthenticationError),
      (403, PermissionDeniedError),
      (404, NotFoundError),
      (429, RateLimitError),
      (500, InternalServerError),
    ]
    for status, _cls in error_classes:
      err = make_status_error(status, "Test message", request_id="req-test")
      s = str(err)
      assert "Test message" in s
      assert f"status={status}" in s
      assert "request_id=req-test" in s


# =============================================================================
# Exception Inheritance Tests
# =============================================================================


class TestExceptionInheritance:
  """Tests for exception class hierarchy."""

  def test_all_status_errors_inherit_from_metorial_api_error(self) -> None:
    error_classes = [
      BadRequestError,
      AuthenticationError,
      PermissionDeniedError,
      NotFoundError,
      ConflictError,
      UnprocessableEntityError,
      RateLimitError,
      InternalServerError,
    ]
    for cls in error_classes:
      err = cls("test")
      assert isinstance(err, MetorialAPIError)
      assert isinstance(err, MetorialSDKError)
      assert isinstance(err, MetorialError)
      assert isinstance(err, Exception)

  def test_can_catch_specific_error(self) -> None:
    err = make_status_error(429, "Rate limited")
    with pytest.raises(RateLimitError):
      raise err

  def test_can_catch_generic_api_error(self) -> None:
    err = make_status_error(429, "Rate limited")
    with pytest.raises(MetorialAPIError):
      raise err

  def test_can_catch_sdk_error(self) -> None:
    err = make_status_error(500, "Server error")
    with pytest.raises(MetorialSDKError):
      raise err

  def test_can_catch_base_metorial_error(self) -> None:
    err = make_status_error(404, "Not found")
    with pytest.raises(MetorialError):
      raise err


# =============================================================================
# Individual Exception Class Tests
# =============================================================================


class TestBadRequestError:
  """Tests for BadRequestError (400)."""

  def test_creation(self) -> None:
    err = BadRequestError("Invalid input")
    assert err.message == "Invalid input"
    assert isinstance(err, MetorialAPIError)

  def test_with_body(self) -> None:
    err = BadRequestError(
      "Validation failed",
      status_code=400,
      body={"errors": [{"field": "email", "message": "Invalid format"}]},
    )
    assert err.body["errors"][0]["field"] == "email"


class TestAuthenticationError:
  """Tests for AuthenticationError (401)."""

  def test_creation(self) -> None:
    err = AuthenticationError("Invalid API key")
    assert err.message == "Invalid API key"

  def test_with_request_id(self) -> None:
    err = AuthenticationError(
      "Token expired",
      status_code=401,
      request_id="req-auth-fail",
    )
    assert err.request_id == "req-auth-fail"


class TestRateLimitError:
  """Tests for RateLimitError (429)."""

  def test_creation(self) -> None:
    err = RateLimitError("Rate limit exceeded")
    assert err.message == "Rate limit exceeded"

  def test_with_retry_info_in_body(self) -> None:
    err = RateLimitError(
      "Too many requests",
      status_code=429,
      body={"retry_after": 60, "limit": 100, "remaining": 0},
    )
    assert err.body["retry_after"] == 60
    assert err.body["limit"] == 100


class TestInternalServerError:
  """Tests for InternalServerError (5xx)."""

  def test_creation(self) -> None:
    err = InternalServerError("Database connection failed")
    assert err.message == "Database connection failed"

  def test_with_trace_id(self) -> None:
    err = InternalServerError(
      "Unexpected error",
      status_code=500,
      request_id="trace-abc-123",
      body={"trace_id": "trace-abc-123"},
    )
    assert err.request_id == "trace-abc-123"


# =============================================================================
# Domain-Specific Exception Tests
# =============================================================================


class TestMetorialToolError:
  """Tests for MetorialToolError."""

  def test_creation(self) -> None:
    err = MetorialToolError("Tool execution failed", tool_name="my_tool")
    assert err.message == "Tool execution failed"
    assert err.tool_name == "my_tool"

  def test_with_args(self) -> None:
    err = MetorialToolError(
      "Invalid arguments",
      tool_name="search",
      tool_args={"query": "test"},
    )
    assert err.tool_args == {"query": "test"}

  def test_str_includes_tool_name(self) -> None:
    err = MetorialToolError("Failed", tool_name="test_tool")
    assert "test_tool" in str(err)


class TestMetorialTimeoutError:
  """Tests for MetorialTimeoutError."""

  def test_creation(self) -> None:
    err = MetorialTimeoutError("Request timed out", timeout_duration=30.0)
    assert err.timeout_duration == 30.0

  def test_with_operation(self) -> None:
    err = MetorialTimeoutError(
      "Timeout",
      timeout_duration=10.0,
      operation="tool_execution",
    )
    assert err.operation == "tool_execution"

  def test_str_includes_timeout_info(self) -> None:
    err = MetorialTimeoutError(
      "Timed out",
      timeout_duration=5.0,
      operation="api_call",
    )
    s = str(err)
    assert "5.0" in s
    assert "api_call" in s


class TestMetorialSessionError:
  """Tests for MetorialSessionError."""

  def test_creation(self) -> None:
    err = MetorialSessionError("Session closed", session_id="sess-123")
    assert err.session_id == "sess-123"

  def test_with_deployment_id(self) -> None:
    err = MetorialSessionError(
      "Connection failed",
      deployment_id="deploy-abc",
    )
    assert err.deployment_id == "deploy-abc"


class TestMetorialConfigError:
  """Tests for MetorialConfigError."""

  def test_creation(self) -> None:
    err = MetorialConfigError("Invalid config", config_key="api_key")
    assert err.config_key == "api_key"

  def test_with_value(self) -> None:
    err = MetorialConfigError(
      "Invalid timeout",
      config_key="timeout",
      config_value=-1,
    )
    assert err.config_value == -1


class TestMetorialConnectionError:
  """Tests for MetorialConnectionError."""

  def test_creation(self) -> None:
    err = MetorialConnectionError("Connection refused", host="api.metorial.com")
    assert err.host == "api.metorial.com"

  def test_with_retry_count(self) -> None:
    err = MetorialConnectionError(
      "Failed after retries",
      host="api.example.com",
      retry_count=3,
    )
    assert err.retry_count == 3


class TestMetorialDuplicateToolError:
  """Tests for MetorialDuplicateToolError."""

  def test_creation(self) -> None:
    err = MetorialDuplicateToolError(
      "Duplicate tool name",
      tool_name="search",
    )
    assert err.tool_name == "search"


# =============================================================================
# Utility Function Tests
# =============================================================================


class TestIsMetorialSdkError:
  """Tests for is_metorial_sdk_error utility function."""

  def test_returns_true_for_sdk_error(self) -> None:
    err = MetorialSDKError({"message": "test", "status": 500, "code": "error"})
    assert is_metorial_sdk_error(err) is True

  def test_returns_true_for_api_error(self) -> None:
    err = make_status_error(404, "Not found")
    assert is_metorial_sdk_error(err) is True

  def test_returns_false_for_base_error(self) -> None:
    err = MetorialError("test")
    assert is_metorial_sdk_error(err) is False

  def test_returns_false_for_standard_exception(self) -> None:
    err = ValueError("test")
    assert is_metorial_sdk_error(err) is False

  def test_returns_false_for_none_attribute(self) -> None:
    class FakeError(Exception):
      pass

    err = FakeError("test")
    assert is_metorial_sdk_error(err) is False


# =============================================================================
# MetorialError.is_metorial_error Tests
# =============================================================================


class TestIsMetorialError:
  """Tests for MetorialError.is_metorial_error static method."""

  def test_returns_true_for_metorial_error(self) -> None:
    err = MetorialError("test")
    assert MetorialError.is_metorial_error(err) is True

  def test_returns_true_for_api_error(self) -> None:
    err = make_status_error(400, "Bad request")
    assert MetorialError.is_metorial_error(err) is True

  def test_returns_true_for_tool_error(self) -> None:
    err = MetorialToolError("Failed", tool_name="test")
    assert MetorialError.is_metorial_error(err) is True

  def test_returns_false_for_standard_exception(self) -> None:
    err = ValueError("test")
    assert MetorialError.is_metorial_error(err) is False


# =============================================================================
# Exception Backwards Compatibility Tests
# =============================================================================


class TestBackwardsCompatibility:
  """Tests for backwards compatibility with existing code."""

  def test_metorial_api_error_status_code_attribute(self) -> None:
    """Ensure status_code attribute is available for existing code."""
    err = MetorialAPIError("Test", status_code=404)
    assert err.status_code == 404

  def test_metorial_api_error_response_data_attribute(self) -> None:
    """Ensure response_data attribute is available for existing code."""
    err = MetorialAPIError("Test", response_data={"key": "value"})
    assert err.response_data == {"key": "value"}

  def test_metorial_api_error_status_attribute(self) -> None:
    """Ensure status attribute is available from parent class."""
    err = MetorialAPIError("Test", status_code=500)
    assert err.status == 500

  def test_metorial_sdk_error_data_attribute(self) -> None:
    """Ensure data attribute is available on SDK errors."""
    err = MetorialSDKError({"message": "test", "status": 400, "code": "error"})
    assert err.data["status"] == 400


# =============================================================================
# Edge Cases and Error Scenarios
# =============================================================================


class TestEdgeCases:
  """Tests for edge cases and unusual scenarios."""

  def test_empty_message(self) -> None:
    err = make_status_error(400, "")
    assert err.message == ""

  def test_very_long_message(self) -> None:
    long_msg = "x" * 10000
    err = make_status_error(500, long_msg)
    assert err.message == long_msg

  def test_unicode_message(self) -> None:
    err = make_status_error(400, "Error: 你好世界 🌍")
    assert "你好世界" in err.message
    assert "🌍" in err.message

  def test_none_body(self) -> None:
    err = make_status_error(404, "Not found", body=None)
    assert err.body is None

  def test_empty_dict_body(self) -> None:
    err = make_status_error(400, "Bad request", body={})
    assert err.body == {}

  def test_nested_body(self) -> None:
    body = {
      "errors": [
        {"field": "name", "errors": ["required", "too_short"]},
        {"field": "email", "errors": ["invalid_format"]},
      ],
      "meta": {"request_id": "123"},
    }
    err = make_status_error(422, "Validation failed", body=body)
    assert err.body["errors"][0]["field"] == "name"
    assert err.body["meta"]["request_id"] == "123"

  def test_special_characters_in_request_id(self) -> None:
    req_id = "req_abc-123.xyz/456"
    err = make_status_error(500, "Error", request_id=req_id)
    assert err.request_id == req_id

  def test_exception_can_be_pickled(self) -> None:
    """Ensure exceptions can be pickled for multiprocessing."""
    import pickle

    err = make_status_error(404, "Not found", request_id="req-123")
    pickled = pickle.dumps(err)
    restored = pickle.loads(pickled)
    assert restored.message == "Not found"
    assert restored.status_code == 404
