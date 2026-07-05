"""
Metorial Python SDK

The official Python SDK for Metorial - The open source integration platform for agentic AI.
"""

# Configure SDK logging to be quiet by default
import logging as _logging

from ._client import Metorial, ProviderSession
from ._magnetar_sdk import (
  MagnetarCallbacksGroup,
  MagnetarCustomProvidersGroup,
  MagnetarDocumentsGroup,
  MagnetarFilesGroup,
  MagnetarIntegrationsGroup,
  MagnetarMagicMcpGroup,
  MagnetarPortalsGroup,
  MagnetarProviderDeploymentsGroup,
  MagnetarProvidersGroup,
  MagnetarSDK,
  MagnetarSessionsGroup,
  MagnetarSessionTemplatesGroup,
  MagnetarSkillsGroup,
  MagnetarStoresGroup,
  create_magnetar_sdk,
)
from ._sdk_shared import SDKConfig

# Session management
from ._session import MetorialSession, SessionFactory
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
from ._types import DictAttributeAccess, MetorialClient
from ._version import __version__
from .connectors import (
  ConnectedSession,
  MetorialAdapter,
  create_mcp_sdk,
  metorial_anthropic,
  metorial_autogen,
  metorial_crewai,
  metorial_deepseek,
  metorial_google,
  metorial_google_adk,
  metorial_haystack,
  metorial_langchain,
  metorial_langgraph,
  metorial_llamaindex,
  metorial_mistral,
  metorial_openai,
  metorial_openai_agents,
  metorial_openai_compatible,
  metorial_pydantic_ai,
  metorial_togetherai,
  metorial_xai,
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
  MagnetarMcpSessionInit,
  MetorialMagnetarMcpSession,
  MetorialMcpClient,
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
    "metorial.mcp.client",
    "mcp.client.sse",
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
  "ProviderSession",
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
  # Types
  "DictAttributeAccess",
  "MetorialClient",
  # connect() adapters
  "ConnectedSession",
  "MetorialAdapter",
  "create_mcp_sdk",
  "metorial_openai",
  "metorial_openai_compatible",
  "metorial_anthropic",
  "metorial_google",
  "metorial_mistral",
  "metorial_deepseek",
  "metorial_togetherai",
  "metorial_xai",
  "metorial_pydantic_ai",
  "metorial_autogen",
  "metorial_crewai",
  "metorial_google_adk",
  "metorial_langchain",
  "metorial_langgraph",
  "metorial_llamaindex",
  "metorial_openai_agents",
  "metorial_haystack",
  # Magnetar SDK
  "SDKConfig",
  "MagnetarSDK",
  "MagnetarProvidersGroup",
  "MagnetarProviderDeploymentsGroup",
  "MagnetarSessionsGroup",
  "MagnetarSessionTemplatesGroup",
  "MagnetarCustomProvidersGroup",
  "MagnetarIntegrationsGroup",
  "MagnetarDocumentsGroup",
  "MagnetarStoresGroup",
  "MagnetarFilesGroup",
  "MagnetarSkillsGroup",
  "MagnetarCallbacksGroup",
  "MagnetarMagicMcpGroup",
  "MagnetarPortalsGroup",
  "create_magnetar_sdk",
  # MCP
  "MetorialMagnetarMcpSession",
  "MagnetarMcpSessionInit",
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
