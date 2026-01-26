"""
Unified Metorial Exception Classes
"""

from typing import Any


class MetorialError(Exception):
  """
  Base error for Metorial SDK. Use MetorialError.is_metorial_error(error) to check.
  """

  __typename = "metorial.error"
  __is_metorial_error = True

  def __init__(
    self,
    message: str,
    error_code: str | None = None,
    details: dict[str, Any] | None = None,
  ):
    Exception.__init__(self, f"[METORIAL ERROR]: {message}")
    self._message = message
    self.error_code = error_code
    self.details = details or {}
    # Set instance attributes for error detection
    self.__is_metorial_error = True
    self.__typename = "metorial.error"

  @property
  def message(self) -> str:
    return self._message

  def __str__(self) -> str:
    if self.error_code:
      return f"[{self.error_code}] {self._message}"
    return self._message

  @staticmethod
  def is_metorial_error(error: Exception) -> bool:
    return getattr(error, "_MetorialError__is_metorial_error", False)


class MetorialSDKError(MetorialError):
  """Unified error that carries HTTP/status info and the raw payload."""

  __typename = "metorial.sdk.error"

  def __init__(self, data: dict[str, Any]) -> None:
    self.data = data

    self.status: int = int(data.get("status", 0))
    code = data.get("code", "unknown_error")
    message = data.get("message", "Unknown error")

    super().__init__(message, error_code=code, details=data)
    # Override typename for SDK errors
    self.__typename = "metorial.sdk.error"

  @property
  def code(self) -> str:
    """Error code returned by the API or synthesized locally."""
    return str(self.data.get("code", "unknown_error"))

  @property
  def message(self) -> str:
    """Human readable error message."""
    return str(self.data.get("message", "Unknown error"))

  @property
  def hint(self) -> str | None:
    """Optional hint for resolving the error."""
    return self.data.get("hint")

  @property
  def description(self) -> str | None:
    """Detailed error description."""
    return self.data.get("description")

  @property
  def reason(self) -> str | None:
    """Reason for the error."""
    return self.data.get("reason")

  @property
  def validation_errors(self) -> list[dict[str, str]] | None:
    """Validation errors if this is a validation error."""
    return self.data.get("errors")

  @property
  def entity(self) -> str | None:
    """Entity related to the error."""
    return self.data.get("entity")

  @property
  def response(self) -> dict[str, Any]:
    """Legacy property for backward compatibility."""
    return self.data

  def __str__(self) -> str:
    base_msg = super().__str__()
    if self.status:
      return f"{base_msg} (HTTP {self.status})"
    return base_msg


class MetorialAPIError(MetorialSDKError):
  """Base API error with request context.

  Provides structured error information including HTTP status codes,
  request IDs for debugging, and response body content.
  """

  def __init__(
    self,
    message: str,
    status_code: int | None = None,
    response_data: dict[str, Any] | None = None,
    request_id: str | None = None,
    body: dict[str, Any] | str | None = None,
  ):
    data = {"message": message, "status": status_code or 0, "code": "API_ERROR"}
    if response_data:
      data.update(response_data)
    super().__init__(data)
    # Add attributes for backward compatibility with tests
    self.status_code = status_code
    self.response_data = response_data or {}
    # New attributes for request context (Knock pattern)
    self.request_id = request_id
    self.body = body

  def __str__(self) -> str:
    parts = [self._message]
    if self.status:
      parts.append(f"status={self.status}")
    if self.request_id:
      parts.append(f"request_id={self.request_id}")
    return " ".join(parts)


# HTTP status-specific exceptions (Knock pattern)
class BadRequestError(MetorialAPIError):
  """HTTP 400 Bad Request - The request was malformed or invalid."""


class AuthenticationError(MetorialAPIError):
  """HTTP 401 Unauthorized - Invalid or missing API key."""


class PermissionDeniedError(MetorialAPIError):
  """HTTP 403 Forbidden - Insufficient permissions for the requested action."""


class NotFoundError(MetorialAPIError):
  """HTTP 404 Not Found - The requested resource does not exist."""


class ConflictError(MetorialAPIError):
  """HTTP 409 Conflict - The request conflicts with current state."""


class UnprocessableEntityError(MetorialAPIError):
  """HTTP 422 Unprocessable Entity - Request validation failed."""


class RateLimitError(MetorialAPIError):
  """HTTP 429 Too Many Requests - Rate limit exceeded."""


class InternalServerError(MetorialAPIError):
  """HTTP 5xx Server Error - An error occurred on the server."""


class OAuthRequiredError(MetorialAPIError):
  """OAuth authentication required - Server deployment requires OAuth session.

  This error is raised when connecting to an MCP server that requires OAuth
  authentication, but no OAuth session was provided in the server_deployments.

  To fix this, create an OAuth session and include it in your deployment:

      oauth = metorial.oauth.sessions.create(server_deployment_id="your-deployment")
      print(f"Authorize at: {oauth.url}")
      await metorial.oauth.wait_for_completion([oauth])

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[
              {"server_deployment_id": "your-deployment", "oauth_session_id": oauth.id}
          ],
      ) as session:
          ...
  """

  def __init__(
    self,
    message: str,
    deployment_id: str | None = None,
    status_code: int | None = None,
    request_id: str | None = None,
    body: dict[str, Any] | str | None = None,
  ):
    super().__init__(
      message,
      status_code=status_code or 401,
      request_id=request_id,
      body=body,
    )
    self.deployment_id = deployment_id


def make_status_error(
  status: int,
  message: str,
  request_id: str | None = None,
  body: dict[str, Any] | str | None = None,
) -> MetorialAPIError:
  """Factory to create appropriate exception for HTTP status code.

  Args:
      status: HTTP status code
      message: Error message
      request_id: Optional request ID from X-Request-ID header
      body: Optional response body

  Returns:
      The appropriate MetorialAPIError subclass for the status code
  """
  error_map: dict[int, type[MetorialAPIError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableEntityError,
    429: RateLimitError,
  }

  if status >= 500:
    return InternalServerError(
      message, status_code=status, request_id=request_id, body=body
    )

  error_cls = error_map.get(status, MetorialAPIError)
  return error_cls(message, status_code=status, request_id=request_id, body=body)


class MetorialToolError(MetorialError):
  """Tool execution errors"""

  def __init__(
    self,
    message: str,
    tool_name: str | None = None,
    tool_args: dict[str, Any] | None = None,
  ):
    super().__init__(
      message,
      error_code="TOOL_ERROR",
      details={"tool_name": tool_name, "tool_args": tool_args or {}},
    )
    self.tool_name = tool_name
    self.tool_args = tool_args or {}

  def __str__(self) -> str:
    base_msg = super().__str__()
    if self.tool_name:
      return f"{base_msg} (Tool: {self.tool_name})"
    return base_msg


class MetorialTimeoutError(MetorialError):
  """Timeout errors"""

  def __init__(
    self,
    message: str,
    timeout_duration: float | None = None,
    operation: str | None = None,
  ):
    super().__init__(
      message,
      error_code="TIMEOUT_ERROR",
      details={"timeout_duration": timeout_duration, "operation": operation},
    )
    self.timeout_duration = timeout_duration
    self.operation = operation

  def __str__(self) -> str:
    base_msg = super().__str__()
    if self.timeout_duration and self.operation:
      return (
        f"{base_msg} (Operation: {self.operation}, Timeout: {self.timeout_duration}s)"
      )
    elif self.timeout_duration:
      return f"{base_msg} (Timeout: {self.timeout_duration}s)"
    return base_msg


class MetorialDuplicateToolError(MetorialError):
  """Error for duplicate tool names"""

  def __init__(self, message: str, tool_name: str | None = None):
    super().__init__(
      message, error_code="DUPLICATE_TOOL_ERROR", details={"tool_name": tool_name}
    )
    self.tool_name = tool_name


class MetorialSessionError(MetorialError):
  """Session-related errors (connection, lifecycle, cleanup)"""

  def __init__(
    self,
    message: str,
    session_id: str | None = None,
    deployment_id: str | None = None,
  ):
    super().__init__(
      message,
      error_code="SESSION_ERROR",
      details={"session_id": session_id, "deployment_id": deployment_id},
    )
    self.session_id = session_id
    self.deployment_id = deployment_id

  def __str__(self) -> str:
    base_msg = super().__str__()
    if self.session_id:
      return f"{base_msg} (Session: {self.session_id})"
    if self.deployment_id:
      return f"{base_msg} (Deployment: {self.deployment_id})"
    return base_msg


class MetorialConfigError(MetorialError):
  """Configuration-related errors (missing keys, invalid values)"""

  def __init__(
    self,
    message: str,
    config_key: str | None = None,
    config_value: Any | None = None,
  ):
    super().__init__(
      message,
      error_code="CONFIG_ERROR",
      details={"config_key": config_key, "config_value": config_value},
    )
    self.config_key = config_key
    self.config_value = config_value

  def __str__(self) -> str:
    base_msg = super().__str__()
    if self.config_key:
      return f"{base_msg} (Key: {self.config_key})"
    return base_msg


class MetorialConnectionError(MetorialError):
  """Connection-related errors (network, transport)"""

  def __init__(
    self,
    message: str,
    host: str | None = None,
    retry_count: int | None = None,
  ):
    super().__init__(
      message,
      error_code="CONNECTION_ERROR",
      details={"host": host, "retry_count": retry_count},
    )
    self.host = host
    self.retry_count = retry_count

  def __str__(self) -> str:
    base_msg = super().__str__()
    parts = []
    if self.host:
      parts.append(f"Host: {self.host}")
    if self.retry_count is not None:
      parts.append(f"Retries: {self.retry_count}")
    if parts:
      return f"{base_msg} ({', '.join(parts)})"
    return base_msg


def is_metorial_sdk_error(error: Exception) -> bool:
  """Check if an error is a MetorialSDKError"""
  return getattr(error, "_MetorialSDKError__typename", None) == "metorial.sdk.error"


__all__ = [
  # Base errors
  "MetorialError",
  "MetorialSDKError",
  "MetorialAPIError",
  # HTTP status-specific errors
  "BadRequestError",
  "AuthenticationError",
  "PermissionDeniedError",
  "NotFoundError",
  "ConflictError",
  "UnprocessableEntityError",
  "RateLimitError",
  "InternalServerError",
  "OAuthRequiredError",
  # Factory function
  "make_status_error",
  # Domain-specific errors
  "MetorialToolError",
  "MetorialTimeoutError",
  "MetorialDuplicateToolError",
  "MetorialSessionError",
  "MetorialConfigError",
  "MetorialConnectionError",
  # Utilities
  "is_metorial_sdk_error",
]
