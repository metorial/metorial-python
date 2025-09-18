"""
Metorial Python SDK

A comprehensive, async-first Python SDK for building AI-powered applications. Supports
multiple AI providers including OpenAI, Anthropic, Google, Mistral, and more.

For more information, visit: https://metorial.com/docs
"""

# Core imports - always available
from metorial_core import (
  # Core clients
  Metorial,  # defaults to async
  MetorialSync,
  MetorialBase,  # same as Metorial
  # Exceptions
  MetorialError,
  MetorialAPIError,
  MetorialToolError,
  MetorialTimeoutError,
  MetorialDuplicateToolError,
  # Tool management
  ToolManager,
  CacheInfo,
  ToolStatistics,
  OpenAITool,
  MetorialTool,
  # Session management
  MetorialSession,
  SessionFactory,
  # Tool adapters
  ToolFormatAdapter,
  ToolSanitizer,
  # Configuration
  MetorialConfig,
  ProviderConfig,
  load_config_from_env,
  get_provider_config,
  validate_config,
  print_config_status,
  # Provider adapters
  ProviderAdapter,
  ChatMessage,
  ChatResponse,
  OpenAIAdapter,
  AnthropicAdapter,
  GoogleAdapter,
  create_provider_adapter,
  infer_provider_type,
  # SDK builder and configuration
  MetorialSDKBuilder,
  SDKConfig,
  SDK,
  create_metorial_sdk,
  # MCP session types (imported via wildcard import below)
  # Utility endpoint types (imported via wildcard import below)
  # Typed endpoint classes (imported via wildcard import below)
  # Streaming types
  StreamEvent,
  StreamEventType,
  ChatMetrics,
)

# Import MCP session types
try:
  from metorial_mcp_session import (
    MetorialMcpSession,
    MetorialMcpSessionInit,
    MetorialMcpToolManager,
    MetorialMcpTool,
    MetorialMcpClient,
  )
except ImportError:
  # MCP session types not available
  pass

# Import utility endpoint types
try:
  from metorial_util_endpoint import (
    MetorialSDKError,
    MetorialRequest,
    MetorialEndpointManager,
    BaseMetorialEndpoint,
  )
except ImportError:
  # Utility endpoint types not available
  pass

# Import typed endpoint classes
try:
  from metorial_core.typed_endpoints import (
    TypedMetorialServersEndpoint,
    TypedMetorialSessionsEndpoint,
  )
except ImportError:
  # Typed endpoint classes not available
  pass

# Import key generated SDK types from metorial-generated
try:
  from mt_2025_01_01_pulsar import *  # noqa: F403
except ImportError:
  # Pulsar SDK types not available
  pass

try:
  from mt_2025_01_01_dashboard import *  # noqa: F403
except ImportError:
  # Dashboard SDK types not available
  pass

# Generated API endpoints are now imported via wildcard imports above

# Generated API types are already available through the types module
# No need for explicit imports since they're included via metorial_core import

# Provider availability tracking
_AVAILABLE_PROVIDERS = {}


def _check_provider_available(provider_name: str, extra_name: str) -> None:
  """Check if a provider is available, raise helpful error if not."""
  if provider_name not in _AVAILABLE_PROVIDERS:
    try:
      if provider_name == "openai":
        import metorial_openai

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "anthropic":
        import metorial_anthropic

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "google":
        import metorial_google

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "mistral":
        import metorial_mistral

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "deepseek":
        import metorial_deepseek

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "togetherai":
        import metorial_togetherai

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "xai":
        import metorial_xai

        _AVAILABLE_PROVIDERS[provider_name] = True
      elif provider_name == "openai_compatible":
        import metorial_openai_compatible

        _AVAILABLE_PROVIDERS[provider_name] = True
    except ImportError:
      _AVAILABLE_PROVIDERS[provider_name] = False

  if not _AVAILABLE_PROVIDERS.get(provider_name, False):
    raise ImportError(
      f"Metorial {provider_name} integration not available. "
      f"Install with: pip install metorial[{extra_name}]"
    )


# Lazy imports using __getattr__ (PEP 562)


def __getattr__(name: str):
  """Lazy import for optional provider integrations."""
  if name == "MetorialOpenAI":
    _check_provider_available("openai", "openai")
    from metorial_openai import MetorialOpenAISession

    return MetorialOpenAISession
  elif name == "MetorialAnthropic":
    _check_provider_available("anthropic", "anthropic")
    from metorial_anthropic import MetorialAnthropicSession

    return MetorialAnthropicSession
  elif name == "MetorialGoogle":
    _check_provider_available("google", "google")
    from metorial_google import MetorialGoogleSession

    return MetorialGoogleSession
  elif name == "MetorialMistral":
    _check_provider_available("mistral", "mistral")
    from metorial_mistral import MetorialMistralSession

    return MetorialMistralSession
  elif name == "MetorialDeepSeek":
    _check_provider_available("deepseek", "deepseek")
    from metorial_deepseek import MetorialDeepSeekSession

    return MetorialDeepSeekSession
  elif name == "MetorialTogetherAI":
    _check_provider_available("togetherai", "togetherai")
    from metorial_togetherai import MetorialTogetherAISession

    return MetorialTogetherAISession
  elif name == "MetorialXAI":
    _check_provider_available("xai", "xai")
    from metorial_xai import MetorialXAISession

    return MetorialXAISession
  elif name == "MetorialOpenAICompatible":
    _check_provider_available("openai_compatible", "openai-compatible")
    from metorial_openai_compatible import MetorialOpenAICompatibleSession

    return MetorialOpenAICompatibleSession
  else:
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__version__ = "1.0.0"

__all__ = [  # noqa: F405
  # Core classes
  "Metorial",  # Async-first (default)
  "MetorialSync",  # Explicit sync
  "MetorialBase",  # Base class
  # Exceptions
  "MetorialError",
  "MetorialAPIError",
  "MetorialToolError",
  "MetorialTimeoutError",
  "MetorialDuplicateToolError",
  # Types and enums
  "StreamEvent",
  "StreamEventType",
  "ChatMetrics",
  # Tool management
  "ToolManager",
  "CacheInfo",
  "ToolStatistics",
  "OpenAITool",
  "MetorialTool",
  # Session management
  "MetorialSession",
  "SessionFactory",
  # Tool adapters
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
  "create_provider_adapter",
  "infer_provider_type",
  # SDK builder and configuration
  "MetorialSDKBuilder",
  "SDKConfig",
  "SDK",
  "create_metorial_sdk",
  # MCP session types
  "MetorialMcpSession",
  "MetorialMcpSessionInit",
  "MetorialMcpToolManager",
  "MetorialMcpTool",
  "MetorialMcpClient",
  # Utility endpoint types
  "MetorialSDKError",
  "MetorialRequest",
  "MetorialEndpointManager",
  "BaseMetorialEndpoint",
  # Typed endpoint classes
  "TypedMetorialServersEndpoint",
  "TypedMetorialSessionsEndpoint",
  # Generated API types (if available)
  # Management endpoints
  "MetorialManagementOrganizationInvitesEndpoint",
  "MetorialManagementInstanceServersVariantsEndpoint",
  "MetorialManagementOrganizationMembersEndpoint",
  "MetorialManagementInstanceLinksEndpoint",
  "MetorialManagementInstanceServersDeploymentsEndpoint",
  "MetorialManagementInstanceSessionsConnectionsEndpoint",
  "MetorialManagementInstanceSessionsMessagesEndpoint",
  "MetorialManagementInstanceServerRunsEndpoint",
  "MetorialManagementInstanceFilesEndpoint",
  "MetorialManagementInstanceServersEndpoint",
  "MetorialManagementInstanceSessionsEventsEndpoint",
  "MetorialManagementInstanceProviderOauthConnectionsProfilesEndpoint",
  "MetorialManagementInstanceServersVersionsEndpoint",
  "MetorialManagementInstanceSecretsEndpoint",
  "MetorialManagementInstanceProviderOauthConnectionsAuthenticationsEndpoint",
  "MetorialManagementInstanceServersImplementationsEndpoint",
  "MetorialManagementInstanceInstanceEndpoint",
  "MetorialManagementInstanceSessionsServerSessionsEndpoint",
  "MetorialManagementOrganizationEndpoint",
  "MetorialManagementOrganizationInstancesEndpoint",
  "MetorialManagementOrganizationProjectsEndpoint",
  "MetorialManagementUserEndpoint",
  "MetorialManagementInstanceServerRunErrorGroupsEndpoint",
  "MetorialManagementInstanceProviderOauthConnectionsEventsEndpoint",
  "MetorialManagementInstanceProviderOauthConnectionsEndpoint",
  # Core endpoints
  "MetorialServersVersionsEndpoint",
  "MetorialProviderOauthConnectionTemplateEndpoint",
  "MetorialProviderOauthConnectionsEventsEndpoint",
  "MetorialProviderOauthEndpoint",
  "MetorialApiKeysEndpoint",
  "MetorialSessionsConnectionsEndpoint",
  "MetorialServerRunErrorsEndpoint",
  "MetorialSessionsEventsEndpoint",
  "MetorialSessionsServerSessionsEndpoint",
  "MetorialSecretsEndpoint",
  "MetorialProviderOauthConnectionsAuthenticationsEndpoint",
  "MetorialServersImplementationsEndpoint",
  "MetorialSessionsMessagesEndpoint",
  "MetorialServerRunsEndpoint",
  "MetorialServersEndpoint",
  "MetorialProviderOauthConnectionsProfilesEndpoint",
  "MetorialServersCapabilitiesEndpoint",
  "MetorialSessionsEndpoint",
  "MetorialFilesEndpoint",
  "MetorialLinksEndpoint",
  "MetorialProviderOauthConnectionsEndpoint",
  "MetorialServersDeploymentsEndpoint",
  "MetorialServersVariantsEndpoint",
  "MetorialInstanceEndpoint",
  # Provider integrations (lazy loaded)
  "MetorialOpenAI",
  "MetorialAnthropic",
  "MetorialGoogle",
  "MetorialMistral",
  "MetorialDeepSeek",
  "MetorialTogetherAI",
  "MetorialXAI",
  "MetorialOpenAICompatible",
]
