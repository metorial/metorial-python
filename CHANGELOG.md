# Changelog

All notable changes to the Metorial Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.0] - 2026-07-05

This release contains breaking API and packaging changes.

### Added

- Added full public-API parity with the Node SDK client surface: new top-level endpoint groups `integrations`, `documents`, `stores`, `files`, `skills`, `callbacks`, `magic_mcp`, and `portals`, plus `providers.triggers`. Every group and its nested sub-endpoints (e.g. `skills.templates.items`, `provider_deployments.auth_configs.imports`, `portals.auth.sso_tenants.connections`, `magic_mcp.servers.providers`) is fully typed.
- Added per-provider optional dependency extras so you install only the provider SDKs you use, mirroring the per-provider packages in the JS SDK: `metorial[openai]`, `metorial[anthropic]`, `metorial[google]`, `metorial[mistral]`, the OpenAI-compatible `metorial[openai-compatible]` / `metorial[deepseek]` / `metorial[xai]` / `metorial[togetherai]`, and `metorial[all]` to install every provider.

### Changed

- Provider LLM SDKs (`openai`, `anthropic`, `google-genai`, `mistralai`) are no longer installed by default. The SDK never imports them itself, so its own flows (`connect()`, provider sessions, tool builders) work without any provider SDK present. Install the relevant extra (or `metorial[all]`) if your own code needs a provider client. This is breaking for clean installs that relied on `pip install metorial` transitively providing a provider SDK; in-place upgrades keep any already-installed provider SDK.
- Reworked the endpoint group classes to subclass their generated base endpoint, giving the entire client tree full static type inference (IDE + mypy strict) with no `Any` and no dynamic attribute delegation. Runtime behavior is unchanged.
- Regenerated the packaged Magnetar client against the current enterprise generator output, so the Python endpoint set now matches the Node SDK.

### Removed

- Removed the non-functional `adapters` module and its exports (`ProviderAdapter`, `ChatMessage`, `ChatResponse`, `OpenAIAdapter`, `AnthropicAdapter`, `GoogleAdapter`, `MistralAdapter`, `DeepSeekAdapter`, `TogetherAIAdapter`, `XAIAdapter`, `OpenAICompatibleAdapter`, `create_provider_adapter`, `infer_provider_type`). These imported provider split-packages that were never published and raised `ImportError` when used; the working equivalents live in `metorial.providers`.
- Removed top-level client endpoints that are not part of the public API surface: `provider_categories`, `provider_collections`, `provider_groups`, `provider_listings`, `custom_providers.commits`, `custom_providers.environments`, `sessions.events`, and `sessions.error_groups`.
- Removed the remaining legacy Pulsar generated tree and its internal helpers (`_sdk.py`, `_typed_endpoints.py`, `_generated/pulsar/`, and the unused `ClientCoreMixin` / server-deployment typed dicts).
- Removed unused exported helpers the SDK never used internally: the config layer (`MetorialConfig`, `ProviderConfig`, `load_config_from_env`, `validate_config`, `get_provider_config`), `RawResponse`, `StreamEvent` / `StreamEventType`, and the provider `chat_completions` helpers (`metorial.providers.openai_chat_completions` / `anthropic_chat_completions` and the per-provider `chat_completions` functions/staticmethods). Use `metorial.connect(...)` and the provider sessions' `tools()` / `call_tools()` instead.

### Fixed

- Fixed the Anthropic provider to parse standardized string tool-call arguments with `json.loads` instead of `eval`.
- Fixed the OpenAI Agents and Haystack integrations to execute tools using the original MCP tool name rather than the sanitized display name.

## [2.3.3] - 2026-06-12

### Changed

- Replaced the deprecated `google-generativeai` dependency with `google-genai`. The old SDK pinned `protobuf < 6`, which caused install conflicts with packages requiring protobuf 6+; `google-genai` has no protobuf dependency. The Google adapter is duck-typed and never imported `google.generativeai` directly, so clients built with either SDK continue to work.

## [2.3.2] - 2026-03-30

### Added

- Added first-party `connect()` adapters, examples, and exports for AutoGen, CrewAI, Google ADK, and LlamaIndex.

### Fixed

- Fixed framework adapter compatibility for Google ADK optional-parameter tool schemas and CrewAI tool execution.
- Fixed smoke-test coverage so local SDK checkouts and published packages can both be exercised from the shared smoke runner.

## [2.3.1] - 2026-03-29

### Fixed

- Fixed MCP tool execution for providers that return `structuredContent` that does not fully match a declared `outputSchema` by preserving raw tool results instead of failing client-side validation.

## [2.3.0] - 2026-03-29

This release contains breaking API and packaging changes.

### Added

- Added the adapter-first `metorial.connect(...)` flow, including typed `ConnectedSession` helpers and first-party adapter factories.
- Added PEP 561 package metadata so installed wheels and sdists ship `py.typed` for downstream IDE and type-checker inference.
- Added targeted transport and connect-path coverage for the new Magnetar-only MCP lifecycle.

### Changed

- Changed `provider_session(...)` to resolve through `connect()` so the compatibility path matches the Node SDK behavior.
- Changed connected-session lifecycle behavior so public `close()` calls are a no-op while the underlying transport is managed internally.
- Regenerated the packaged API surface against the current enterprise generator output.

### Removed

- Removed deprecated `with_provider_session()` usage from the public recommended flow in favor of `connect()`.
- Removed legacy Pulsar support and made the SDK Magnetar-only.
- Removed the synchronous client surface and related helpers, wrappers, exports, and tests.
- Removed public LlamaIndex support, examples, and smoke-test wiring.

### Fixed

- Fixed downstream typing support for installed consumers by explicitly shipping the typed package marker in build artifacts.
- Fixed shutdown behavior around MCP transport ownership without requiring explicit session cleanup from consumers.

## [1.0.0] - 2025-07-12

### Added

- Initial release of Metorial Python SDK
- Multi-provider support for AI models:
  - OpenAI (GPT-4, GPT-3.5)
  - Anthropic (Claude)
  - Google (Gemini)
  - Mistral AI
  - DeepSeek
  - Together AI
  - XAI (Grok)
  - AI SDK frameworks
- Async/await interface for modern Python development
- Automatic session lifecycle handling
- Tool discovery and formatting capabilities
- Provider-specific tool format conversion
- High-performance async HTTP operations with aiohttp
- Comprehensive error handling with `MetorialAPIError`
- Full type hints and mypy support
- Extensive documentation and examples

### Core Features

- `Metorial` class for SDK initialization
- `with_provider_session()` for provider-specific sessions
- `with_session()` for direct session management
- OpenAI-compatible tool interface
- Automatic tool calling and response handling

### Dependencies

- `aiohttp>=3.8.0` for async HTTP requests
- `typing-extensions>=4.0.0` for enhanced type support
- Optional provider-specific SDKs:
  - `openai>=1.0.0` for OpenAI integration
  - `anthropic>=0.3.0` for Anthropic integration

### Development Tools

- Black code formatting
- MyPy type checking
- Pytest for testing
- Flake8 for linting

## [1.0.0-rc.1] - 2025-07-12

- Refactor initial release

### Core Features

- `Metorial` class for SDK initialization
- `with_provider_session()` for provider-specific sessions
- `with_session()` for direct session management
- OpenAI-compatible tool interface
- Automatic tool calling and response handling

### Dependencies

- `aiohttp>=3.8.0` for async HTTP requests
- `typing-extensions>=4.0.0` for enhanced type support
- Optional provider-specific SDKs:
  - `openai>=1.0.0` for OpenAI integration
