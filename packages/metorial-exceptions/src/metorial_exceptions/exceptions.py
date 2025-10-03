"""
Unified Metorial Exception Classes
"""

from typing import Dict, Any, Optional


class MetorialError(Exception):
  """
  Base error for Metorial SDK. Use MetorialError.is_metorial_error(error) to check.
  """

  __typename = "metorial.error"
  __is_metorial_error = True

  def __init__(
    self,
    message: str,
    error_code: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
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

  def __init__(self, data: dict):
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
  def hint(self):
    """Optional hint for resolving the error."""
    return self.data.get("hint")

  @property
  def description(self):
    """Detailed error description."""
    return self.data.get("description")

  @property
  def reason(self):
    """Reason for the error."""
    return self.data.get("reason")

  @property
  def validation_errors(self):
    """Validation errors if this is a validation error."""
    return self.data.get("errors")

  @property
  def entity(self):
    """Entity related to the error."""
    return self.data.get("entity")

  @property
  def response(self):
    """Legacy property for backward compatibility."""
    return self.data

  def __str__(self) -> str:
    base_msg = super().__str__()
    if self.status:
      return f"{base_msg} (HTTP {self.status})"
    return base_msg


class MetorialAPIError(MetorialSDKError):
  """API-related errors - alias for MetorialSDKError for backward compatibility"""

  def __init__(
    self,
    message: str,
    status_code: Optional[int] = None,
    response_data: Optional[Dict[str, Any]] = None,
  ):
    data = {"message": message, "status": status_code or 0, "code": "API_ERROR"}
    if response_data:
      data.update(response_data)
    super().__init__(data)
    # Add attributes for backward compatibility with tests
    self.status_code = status_code
    self.response_data = response_data or {}


class MetorialToolError(MetorialError):
  """Tool execution errors"""

  def __init__(
    self,
    message: str,
    tool_name: Optional[str] = None,
    tool_args: Optional[Dict[str, Any]] = None,
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
    timeout_duration: Optional[float] = None,
    operation: Optional[str] = None,
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

  def __init__(self, message: str, tool_name: Optional[str] = None):
    super().__init__(
      message, error_code="DUPLICATE_TOOL_ERROR", details={"tool_name": tool_name}
    )
    self.tool_name = tool_name


def is_metorial_sdk_error(error: Exception) -> bool:
  """Check if an error is a MetorialSDKError"""
  return getattr(error, "_MetorialSDKError__typename", None) == "metorial.sdk.error"
