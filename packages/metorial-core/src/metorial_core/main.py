"""
Metorial Core SDK Main Module.
"""

# Core client classes
from .lib.clients.async_client import Metorial
from .lib.clients.sync_client import MetorialSync
from .base import MetorialBase

# Core types and utilities
from metorial_exceptions import (
  MetorialError,
  MetorialSDKError,
  MetorialAPIError,
  MetorialToolError,
  MetorialTimeoutError,
  MetorialDuplicateToolError,
)
from .types import RunResult, DictAttributeAccess
from .lib.streaming import StreamEvent, StreamEventType
from .lib.metrics import ChatMetrics

# Tool management and session handling
from .tool_manager import ToolManager, CacheInfo
from .session import MetorialSession, SessionFactory
from .tool_adapters import (
  ToolFormatAdapter,
  ToolSanitizer,
  OpenAITool,
  MetorialTool,
  ToolStatistics,
)

# Configuration
from .config import (
  MetorialConfig,
  ProviderConfig,
  load_config_from_env,
  get_provider_config,
  validate_config,
  print_config_status,
)

# Provider adapters
from .adapters import (
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
)

# SDK builder
from .sdk import (
  MetorialSDKBuilder,
  SDKConfig,
  SDK,
  create_metorial_sdk,
  create_auth_headers,
)

# Typed endpoints
from .typed_endpoints import TypedMetorialServersEndpoint, TypedMetorialSessionsEndpoint

__all__ = [
  # Main client classes
  "Metorial",
  "MetorialSync",
  "MetorialBase",
  # Exception classes
  "MetorialError",
  "MetorialSDKError",
  "MetorialAPIError",
  "MetorialToolError",
  "MetorialTimeoutError",
  "MetorialDuplicateToolError",
  # Streaming types
  "StreamEvent",
  "StreamEventType",
  # Result types
  "RunResult",
  "DictAttributeAccess",
  # Metrics
  "ChatMetrics",
  # Tool management
  "ToolManager",
  "CacheInfo",
  "ToolStatistics",
  "OpenAITool",
  "MetorialTool",
  "MetorialSession",
  "SessionFactory",
  "ToolFormatAdapter",
  "ToolSanitizer",
  # Configuration
  "MetorialConfig",
  "ProviderConfig",
  "load_config_from_env",
  "get_provider_config",
  "validate_config",
  "print_config_status",
  # Provider adapters
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
  # SDK builder
  "MetorialSDKBuilder",
  "SDKConfig",
  "SDK",
  "create_metorial_sdk",
  "create_auth_headers",
  # Typed endpoints
  "TypedMetorialServersEndpoint",
  "TypedMetorialSessionsEndpoint",
]
