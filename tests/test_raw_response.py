"""
Tests for RawResponse wrapper class.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest

from metorial._raw_response import RawResponse, RawResponseWrapper

# =============================================================================
# RawResponse Basic Tests
# =============================================================================


class TestRawResponseBasics:
  """Basic tests for RawResponse class."""

  def test_parse_returns_parsed_data(self, mock_http_response: MagicMock) -> None:
    parsed_data = {"id": "123", "name": "test"}
    raw = RawResponse(mock_http_response, parsed_data)
    assert raw.parse() == parsed_data

  def test_status_code(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    assert raw.status_code == 200

  def test_request_id(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    assert raw.request_id == "req-test-123"

  def test_request_id_none_when_missing(self) -> None:
    response = MagicMock()
    response.status_code = 200
    response.headers = {"Content-Type": "application/json"}
    raw = RawResponse(response, {})
    assert raw.request_id is None

  def test_headers(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    headers = raw.headers
    assert headers["X-Request-ID"] == "req-test-123"
    assert headers["Content-Type"] == "application/json"

  def test_content_type(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    assert raw.content_type == "application/json"

  def test_content_type_none_when_missing(self) -> None:
    response = MagicMock()
    response.status_code = 200
    response.headers = {}
    raw = RawResponse(response, {})
    assert raw.content_type is None


# =============================================================================
# RawResponse is_success Tests
# =============================================================================


class TestRawResponseIsSuccess:
  """Tests for is_success property."""

  @pytest.mark.parametrize("status", [200, 201, 202, 203, 204, 205, 206])
  def test_is_success_true_for_2xx(self, status: int) -> None:
    response = MagicMock()
    response.status_code = status
    response.headers = {}
    raw = RawResponse(response, {})
    assert raw.is_success is True

  @pytest.mark.parametrize("status", [100, 101, 102])
  def test_is_success_false_for_1xx(self, status: int) -> None:
    response = MagicMock()
    response.status_code = status
    response.headers = {}
    raw = RawResponse(response, {})
    assert raw.is_success is False

  @pytest.mark.parametrize("status", [300, 301, 302, 303, 304, 307, 308])
  def test_is_success_false_for_3xx(self, status: int) -> None:
    response = MagicMock()
    response.status_code = status
    response.headers = {}
    raw = RawResponse(response, {})
    assert raw.is_success is False

  @pytest.mark.parametrize("status", [400, 401, 403, 404, 422, 429])
  def test_is_success_false_for_4xx(self, status: int) -> None:
    response = MagicMock()
    response.status_code = status
    response.headers = {}
    raw = RawResponse(response, {})
    assert raw.is_success is False

  @pytest.mark.parametrize("status", [500, 501, 502, 503, 504])
  def test_is_success_false_for_5xx(self, status: int) -> None:
    response = MagicMock()
    response.status_code = status
    response.headers = {}
    raw = RawResponse(response, {})
    assert raw.is_success is False


# =============================================================================
# RawResponse __repr__ Tests
# =============================================================================


class TestRawResponseRepr:
  """Tests for __repr__ method."""

  def test_repr(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    repr_str = repr(raw)
    assert "RawResponse" in repr_str
    assert "status_code=200" in repr_str
    assert "request_id='req-test-123'" in repr_str
    assert "content_type='application/json'" in repr_str

  def test_repr_with_none_values(self) -> None:
    response = MagicMock()
    response.status_code = 204
    response.headers = {}
    raw = RawResponse(response, None)
    repr_str = repr(raw)
    assert "status_code=204" in repr_str
    assert "request_id=None" in repr_str
    assert "content_type=None" in repr_str


# =============================================================================
# RawResponse Generic Type Tests
# =============================================================================


class TestRawResponseGenericType:
  """Tests for generic type preservation."""

  def test_dict_type_preserved(self, mock_http_response: MagicMock) -> None:
    data: dict[str, Any] = {"items": [1, 2, 3], "count": 3}
    raw: RawResponse[dict[str, Any]] = RawResponse(mock_http_response, data)
    result = raw.parse()
    assert result["items"] == [1, 2, 3]
    assert result["count"] == 3

  def test_list_type_preserved(self, mock_http_response: MagicMock) -> None:
    data = [{"id": 1}, {"id": 2}, {"id": 3}]
    raw: RawResponse[list[dict[str, int]]] = RawResponse(mock_http_response, data)
    result = raw.parse()
    assert len(result) == 3
    assert result[0]["id"] == 1

  def test_string_type_preserved(self, mock_http_response: MagicMock) -> None:
    data = "plain text response"
    raw: RawResponse[str] = RawResponse(mock_http_response, data)
    result = raw.parse()
    assert result == "plain text response"

  def test_none_type_preserved(self, mock_http_response: MagicMock) -> None:
    raw: RawResponse[None] = RawResponse(mock_http_response, None)
    result = raw.parse()
    assert result is None

  def test_custom_object_type_preserved(self, mock_http_response: MagicMock) -> None:
    class User:
      def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    user = User(id=123, name="Test")
    raw: RawResponse[User] = RawResponse(mock_http_response, user)
    result = raw.parse()
    assert result.id == 123
    assert result.name == "Test"


# =============================================================================
# RawResponse with Different Response Types Tests
# =============================================================================


class TestRawResponseWithDifferentResponseTypes:
  """Tests for RawResponse with different HTTP response implementations."""

  def test_with_dict_like_headers(self) -> None:
    """Test with a response that has dict-like headers."""
    response = MagicMock()
    response.status_code = 200
    response.headers = {
      "X-Request-ID": "req-dict-123",
      "Content-Type": "text/plain",
      "X-Custom-Header": "custom-value",
    }
    raw = RawResponse(response, "data")
    assert raw.request_id == "req-dict-123"
    assert raw.content_type == "text/plain"
    assert raw.headers["X-Custom-Header"] == "custom-value"

  def test_with_case_sensitive_headers(self) -> None:
    """Test header access is case-sensitive by default."""
    response = MagicMock()
    response.status_code = 200
    response.headers = {
      "X-Request-ID": "req-123",
      "x-request-id": "req-456",  # Different case
    }
    raw = RawResponse(response, {})
    # Should get the exact case match
    assert raw.request_id == "req-123"


# =============================================================================
# RawResponseWrapper Tests
# =============================================================================


class TestRawResponseWrapper:
  """Tests for RawResponseWrapper class."""

  def test_to_raw_creates_raw_response(self, mock_http_response: MagicMock) -> None:
    parsed = {"key": "value"}
    wrapper = RawResponseWrapper(parsed, mock_http_response)
    raw = wrapper.to_raw()
    assert isinstance(raw, RawResponse)
    assert raw.parse() == parsed
    assert raw.status_code == 200

  def test_wrapper_preserves_parsed_data(self, mock_http_response: MagicMock) -> None:
    parsed = [1, 2, 3]
    wrapper = RawResponseWrapper(parsed, mock_http_response)
    raw = wrapper.to_raw()
    assert raw.parse() == [1, 2, 3]

  def test_wrapper_preserves_response(self, mock_http_response: MagicMock) -> None:
    parsed = "test"
    wrapper = RawResponseWrapper(parsed, mock_http_response)
    raw = wrapper.to_raw()
    assert raw.request_id == "req-test-123"


# =============================================================================
# RawResponse Edge Cases Tests
# =============================================================================


class TestRawResponseEdgeCases:
  """Tests for edge cases and unusual scenarios."""

  def test_empty_dict_data(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    assert raw.parse() == {}

  def test_empty_list_data(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, [])
    assert raw.parse() == []

  def test_empty_string_data(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, "")
    assert raw.parse() == ""

  def test_zero_value_data(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, 0)
    assert raw.parse() == 0

  def test_false_value_data(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, False)
    assert raw.parse() is False

  def test_deeply_nested_data(self, mock_http_response: MagicMock) -> None:
    data = {"level1": {"level2": {"level3": {"level4": [1, 2, {"level5": "deep"}]}}}}
    raw = RawResponse(mock_http_response, data)
    result = raw.parse()
    assert result["level1"]["level2"]["level3"]["level4"][2]["level5"] == "deep"

  def test_large_data(self, mock_http_response: MagicMock) -> None:
    data = {"items": list(range(10000))}
    raw = RawResponse(mock_http_response, data)
    result = raw.parse()
    assert len(result["items"]) == 10000

  def test_unicode_data(self, mock_http_response: MagicMock) -> None:
    data = {"message": "Hello 世界 🌍 مرحبا"}
    raw = RawResponse(mock_http_response, data)
    result = raw.parse()
    assert "世界" in result["message"]
    assert "🌍" in result["message"]

  def test_binary_like_data(self, mock_http_response: MagicMock) -> None:
    data = b"binary content"
    raw = RawResponse(mock_http_response, data)
    assert raw.parse() == b"binary content"


# =============================================================================
# RawResponse Headers Tests
# =============================================================================


class TestRawResponseHeaders:
  """Tests for headers access."""

  def test_headers_returns_dict(self, mock_http_response: MagicMock) -> None:
    raw = RawResponse(mock_http_response, {})
    headers = raw.headers
    assert isinstance(headers, dict)

  def test_headers_is_copy(self, mock_http_response: MagicMock) -> None:
    """Modifying returned headers should not affect the response."""
    raw = RawResponse(mock_http_response, {})
    headers = raw.headers
    headers["New-Header"] = "new-value"
    # Original response headers should not be modified
    assert "New-Header" not in mock_http_response.headers

  def test_multiple_headers_access(self, mock_http_response: MagicMock) -> None:
    """Multiple calls to headers should return consistent data."""
    raw = RawResponse(mock_http_response, {})
    headers1 = raw.headers
    headers2 = raw.headers
    assert headers1 == headers2

  def test_special_header_values(self) -> None:
    """Test headers with special characters in values."""
    response = MagicMock()
    response.status_code = 200
    response.headers = {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-cache, no-store, must-revalidate",
      "Link": '<https://api.example.com/next>; rel="next"',
    }
    raw = RawResponse(response, {})
    assert raw.content_type == "application/json; charset=utf-8"
    assert raw.headers["Cache-Control"] == "no-cache, no-store, must-revalidate"


# =============================================================================
# RawResponse Immutability Tests
# =============================================================================


class TestRawResponseImmutability:
  """Tests to ensure RawResponse behaves correctly with data."""

  def test_parse_returns_same_object(self, mock_http_response: MagicMock) -> None:
    """Multiple calls to parse() should return the same object."""
    data = {"key": "value"}
    raw = RawResponse(mock_http_response, data)
    result1 = raw.parse()
    result2 = raw.parse()
    assert result1 is result2

  def test_modifying_parsed_data_affects_future_calls(
    self, mock_http_response: MagicMock
  ) -> None:
    """Modifying parsed data affects future parse() calls (same reference)."""
    data: dict[str, Any] = {"key": "value"}
    raw = RawResponse(mock_http_response, data)
    result = raw.parse()
    result["new_key"] = "new_value"
    # Should see the modification
    assert raw.parse()["new_key"] == "new_value"


# =============================================================================
# RawResponse with Real-world-like Scenarios
# =============================================================================


class TestRawResponseRealWorldScenarios:
  """Tests simulating real-world usage scenarios."""

  def test_api_list_response(self) -> None:
    """Test handling of paginated list response."""
    response = MagicMock()
    response.status_code = 200
    response.headers = {
      "X-Request-ID": "req-list-123",
      "Content-Type": "application/json",
      "X-Total-Count": "100",
      "X-Page": "1",
      "X-Per-Page": "10",
    }
    data = {
      "items": [{"id": i} for i in range(10)],
      "total": 100,
      "page": 1,
      "per_page": 10,
    }
    raw = RawResponse(response, data)

    assert raw.is_success
    assert raw.request_id == "req-list-123"
    assert len(raw.parse()["items"]) == 10
    assert raw.headers["X-Total-Count"] == "100"

  def test_api_create_response(self) -> None:
    """Test handling of resource creation response."""
    response = MagicMock()
    response.status_code = 201
    response.headers = {
      "X-Request-ID": "req-create-456",
      "Content-Type": "application/json",
      "Location": "https://api.example.com/resources/new-123",
    }
    data = {
      "id": "new-123",
      "name": "New Resource",
      "created_at": "2024-01-15T10:30:00Z",
    }
    raw = RawResponse(response, data)

    assert raw.is_success
    assert raw.status_code == 201
    assert raw.parse()["id"] == "new-123"
    assert raw.headers["Location"] == "https://api.example.com/resources/new-123"

  def test_api_delete_response(self) -> None:
    """Test handling of deletion response (204 No Content)."""
    response = MagicMock()
    response.status_code = 204
    response.headers = {
      "X-Request-ID": "req-delete-789",
    }
    raw = RawResponse(response, None)

    assert raw.is_success
    assert raw.status_code == 204
    assert raw.parse() is None

  def test_error_response_parsing(self) -> None:
    """Test handling of error response for debugging."""
    response = MagicMock()
    response.status_code = 422
    response.headers = {
      "X-Request-ID": "req-error-abc",
      "Content-Type": "application/json",
    }
    data = {
      "error": "validation_error",
      "message": "Validation failed",
      "details": [
        {"field": "email", "error": "Invalid email format"},
        {"field": "age", "error": "Must be positive"},
      ],
    }
    raw = RawResponse(response, data)

    assert not raw.is_success
    assert raw.status_code == 422
    assert raw.request_id == "req-error-abc"
    errors = raw.parse()
    assert errors["error"] == "validation_error"
    assert len(errors["details"]) == 2
