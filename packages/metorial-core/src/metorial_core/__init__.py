"""
Metorial Core SDK - Internal implementation
Generally not for public use: use 'metorial' package instead
"""

import logging

# Enable logging with: logging.getLogger('metorial_core').setLevel(logging.DEBUG)

# Automatically apply safe cleanup to prevent AsyncIO warnings in simple usage
try:
    from .lib.safe_cleanup import install_warning_filters, attach_noise_filters
    # Apply safe cleanup automatically - no opt-in needed for basic usage
    install_warning_filters()
    attach_noise_filters()
except ImportError:
    pass  # Safe cleanup not available

_metorial_logger_prefixes = ["metorial", "mcp", "httpx", "urllib3"]


def _configure_sdk_logging():
  """Configure SDK logging to be silent by default."""

  # Set all loggers with our prefixes to CRITICAL level
  for name, logger in logging.Logger.manager.loggerDict.items():
    if isinstance(logger, logging.Logger):
      for prefix in _metorial_logger_prefixes:
        if name.startswith(prefix):
          logger.setLevel(logging.CRITICAL)
          logger.propagate = False

  # Explicitly silence critical loggers that generate noise
  critical_loggers = [
    "metorial_core",
    "metorial_core.base",
    "metorial_core.lib.clients.async_client",
    "metorial_core.lib.clients.sync_client",
    "metorial_mcp_session",
    "metorial_mcp_session.mcp_session",
    "metorial_mcp_session.mcp_client",
    "metorial.mcp.client",
    "mcp.client.sse",
    "httpx",
    "urllib3",
  ]

  for logger_name in critical_loggers:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.CRITICAL)
    logger.propagate = False

    # Also silence any child loggers
    for name in logging.Logger.manager.loggerDict:
      if name.startswith(logger_name + "."):
        child_logger = logging.getLogger(name)
        if isinstance(child_logger, logging.Logger):
          child_logger.setLevel(logging.CRITICAL)
          child_logger.propagate = False


_configure_sdk_logging()


def _ensure_quiet_logging():
  _configure_sdk_logging()


# Import everything from main module
from .main import (
  Metorial,
  MetorialSync,
  MetorialBase,
  MetorialError,
  MetorialSDKError,
  MetorialAPIError,
  MetorialToolError,
  MetorialTimeoutError,
  MetorialDuplicateToolError,
  StreamEvent,
  StreamEventType,
  ChatMetrics,
  ToolManager,
  CacheInfo,
  ToolStatistics,
  OpenAITool,
  MetorialTool,
  MetorialSession,
  SessionFactory,
  ToolFormatAdapter,
  ToolSanitizer,
  MetorialConfig,
  ProviderConfig,
  load_config_from_env,
  get_provider_config,
  validate_config,
  print_config_status,
  ProviderAdapter,
  ChatMessage,
  ChatResponse,
  OpenAIAdapter,
  AnthropicAdapter,
  GoogleAdapter,
  MistralAdapter,
  DeepSeekAdapter,
  TogetherAIAdapter,
  XAIAdapter,
  OpenAICompatibleAdapter,
  create_provider_adapter,
  infer_provider_type,
  MetorialSDKBuilder,
  SDKConfig,
  SDK,
  create_metorial_sdk,
  create_auth_headers,
  TypedMetorialServersEndpoint,
  TypedMetorialSessionsEndpoint,
)

# Import types
from .types import RunResult, DictAttributeAccess

# Import Group classes separately to avoid circular imports
from .sdk import (
  ServersGroup,
  SessionsGroup,
  ProviderOauthGroup,
  ProviderOauthConnectionsGroup,
  RunsGroup,
)

# Import additional typed endpoints
from .typed_endpoints import (
  TypedMetorialProviderOauthEndpoint,
  TypedMetorialProviderOauthConnectionsEndpoint,
)

__version__ = "1.0.0"

__all__ = [
  "Metorial",
  "MetorialSync",
  "MetorialBase",
  "MetorialError",
  "MetorialSDKError",
  "MetorialAPIError",
  "MetorialToolError",
  "MetorialTimeoutError",
  "MetorialDuplicateToolError",
  "StreamEvent",
  "StreamEventType",
  "ChatMetrics",
  "ToolManager",
  "CacheInfo",
  "ToolStatistics",
  "OpenAITool",
  "MetorialTool",
  "MetorialSession",
  "SessionFactory",
  "ToolFormatAdapter",
  "ToolSanitizer",
  "MetorialConfig",
  "ProviderConfig",
  "load_config_from_env",
  "get_provider_config",
  "validate_config",
  "print_config_status",
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
  "create_provider_adapter",
  "infer_provider_type",
  "MetorialSDKBuilder",
  "SDKConfig",
  "SDK",
  "create_metorial_sdk",
  "create_auth_headers",
  # Result types
  "RunResult",
  "DictAttributeAccess",
  # Group classes for type checking
  "ServersGroup",
  "SessionsGroup",
  "ProviderOauthGroup",
  "ProviderOauthConnectionsGroup",
  "RunsGroup",
  # Typed endpoint classes
  "TypedMetorialServersEndpoint",
  "TypedMetorialSessionsEndpoint",
  "TypedMetorialProviderOauthEndpoint",
  "TypedMetorialProviderOauthConnectionsEndpoint",
  "__version__",
]
