# Changelog

All notable changes to the Metorial Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
