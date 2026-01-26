"""
Metorial Python SDK

The official Python SDK for Metorial - The open source integration platform for agentic AI.
"""

# Configure SDK logging to be quiet by default
import logging as _logging

# SDK Builder and endpoint groups
from ._base import OAuthWithWaitForCompletion

# Core client classes
from ._client import Metorial, ProviderSession

# Configuration
from ._config import (
  MetorialConfig,
  ProviderConfig,
  get_provider_config,
  load_config_from_env,
  validate_config,
)

# Raw response wrapper
from ._raw_response import RawResponse
from ._sdk import (
  SDK,
  ProviderOauthGroup,
  RunsGroup,
  SDKConfig,
  ServersGroup,
  SessionsGroup,
  create_metorial_sdk,
)

# Session management
from ._session import MetorialSession, SessionFactory

# Streaming types
from ._streaming import StreamEvent, StreamEventType
from ._sync_client import MetorialSync
from ._tool_adapters import (
  MetorialTool,
  OpenAITool,
  ToolFormatAdapter,
  ToolResult,
  ToolSanitizer,
  ToolStatistics,
)

# Tool management
from ._tool_manager import CacheInfo, ToolManager

# Types
from ._types import (
  DictAttributeAccess,
  MetorialClient,
  OAuthSession,
  ServerDeployment,
  ServerDeployments,
)
from ._version import __version__

# Adapters
from .adapters import (
  AnthropicAdapter,
  ChatMessage,
  ChatResponse,
  DeepSeekAdapter,
  GoogleAdapter,
  MistralAdapter,
  OpenAIAdapter,
  OpenAICompatibleAdapter,
  ProviderAdapter,
  TogetherAIAdapter,
  XAIAdapter,
  create_provider_adapter,
  infer_provider_type,
)

# Exceptions
from .exceptions import (
  AuthenticationError,
  BadRequestError,
  ConflictError,
  InternalServerError,
  MetorialAPIError,
  MetorialDuplicateToolError,
  MetorialError,
  MetorialSDKError,
  MetorialTimeoutError,
  MetorialToolError,
  NotFoundError,
  OAuthRequiredError,
  PermissionDeniedError,
  RateLimitError,
  UnprocessableEntityError,
  is_metorial_sdk_error,
  make_status_error,
)

# MCP Session (public)
from .mcp import (
  MetorialMcpClient,
  MetorialMcpSession,
  MetorialMcpSessionInit,
  MetorialMcpTool,
  MetorialMcpToolManager,
)

# Provider sessions (public)
from .providers import (
  MetorialAnthropicSession,
  MetorialDeepSeekSession,
  MetorialGoogleSession,
  MetorialMistralSession,
  MetorialOpenAICompatibleSession,
  MetorialOpenAISession,
  MetorialTogetherAISession,
  MetorialXAISession,
  build_openai_tools,
  call_openai_tools,
)


def _configure_sdk_logging() -> None:
  """Configure SDK logging to be quiet by default."""
  _noisy_loggers = [
    "metorial._base",
    "metorial._client",
    "metorial._sync_client",
    "metorial.mcp.mcp_session",
    "metorial.mcp.client",
    "mcp.client.sse",
    "aiohttp_sse_client",
    "httpx",
    "httpcore",
    "anyio",
  ]
  for logger_name in _noisy_loggers:
    logger = _logging.getLogger(logger_name)
    logger.setLevel(_logging.WARNING)
    logger.propagate = False


_configure_sdk_logging()


__all__ = [
  # Version
  "__version__",
  # Core clients
  "Metorial",
  "MetorialSync",
  "ProviderSession",
  # Configuration
  "MetorialConfig",
  "ProviderConfig",
  "load_config_from_env",
  "get_provider_config",
  "validate_config",
  # Session
  "MetorialSession",
  "SessionFactory",
  # Tool management
  "ToolManager",
  "CacheInfo",
  "OpenAITool",
  "MetorialTool",
  "ToolResult",
  "ToolStatistics",
  "ToolFormatAdapter",
  "ToolSanitizer",
  # Exceptions
  "MetorialError",
  "MetorialSDKError",
  "MetorialAPIError",
  "BadRequestError",
  "AuthenticationError",
  "PermissionDeniedError",
  "NotFoundError",
  "ConflictError",
  "UnprocessableEntityError",
  "RateLimitError",
  "InternalServerError",
  "OAuthRequiredError",
  "make_status_error",
  "MetorialToolError",
  "MetorialTimeoutError",
  "MetorialDuplicateToolError",
  "is_metorial_sdk_error",
  # Raw response
  "RawResponse",
  # Streaming
  "StreamEvent",
  "StreamEventType",
  # Types
  "DictAttributeAccess",
  "ServerDeployment",
  "OAuthSession",
  "ServerDeployments",
  "MetorialClient",
  # Adapters
  "ProviderAdapter",
  "ChatMessage",
  "ChatResponse",
  "OpenAIAdapter",
  "AnthropicAdapter",
  "GoogleAdapter",
  "MistralAdapter",
  "DeepSeekAdapter",
  "TogetherAIAdapter",
  "XAIAdapter",
  "OpenAICompatibleAdapter",
  "infer_provider_type",
  "create_provider_adapter",
  # SDK
  "SDK",
  "SDKConfig",
  "create_metorial_sdk",
  "ServersGroup",
  "SessionsGroup",
  "ProviderOauthGroup",
  "RunsGroup",
  "OAuthWithWaitForCompletion",
  # MCP
  "MetorialMcpSession",
  "MetorialMcpSessionInit",
  "MetorialMcpToolManager",
  "MetorialMcpTool",
  "MetorialMcpClient",
  # Provider sessions
  "MetorialOpenAISession",
  "MetorialAnthropicSession",
  "MetorialGoogleSession",
  "MetorialMistralSession",
  "MetorialDeepSeekSession",
  "MetorialTogetherAISession",
  "MetorialXAISession",
  "MetorialOpenAICompatibleSession",
  "build_openai_tools",
  "call_openai_tools",
]
