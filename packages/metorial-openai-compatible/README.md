# metorial-openai-compatible

Base package for OpenAI-compatible provider integrations for Metorial. This package provides shared functionality for providers that use OpenAI's function calling format.

## Installation

```bash
pip install metorial-openai-compatible
# or
uv add metorial-openai-compatible
# or
poetry add metorial-openai-compatible
```

## Features

- 🔧 **OpenAI Format**: Standard OpenAI function calling format
- ✅ **Strict Mode**: Configurable strict parameter validation
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ⚡ **Async Support**: Full async/await support
- 🏗️ **Base Class**: Foundation for provider-specific implementations

## Usage

### Direct Usage

```python
import asyncio
from metorial import Metorial
from metorial_openai_compatible import MetorialOpenAICompatibleSession

async def main():
    # Initialize Metorial
    metorial = Metorial(api_key="your-metorial-api-key")
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
        # Create OpenAI-compatible wrapper
        openai_session = MetorialOpenAICompatibleSession(
            session.tool_manager,
            with_strict=True  # Enable strict mode
        )
        
        # Use with any OpenAI-compatible client
        tools = openai_session.tools
        
        # Handle tool calls from response
        tool_responses = await openai_session.call_tools(tool_calls)

asyncio.run(main())
```

### As Base Class

This package is primarily used as a base for provider-specific packages:

```python
from metorial_openai_compatible import MetorialOpenAICompatibleSession

class MyProviderSession(MetorialOpenAICompatibleSession):
    def __init__(self, tool_mgr):
        # Configure strict mode based on provider capabilities
        super().__init__(tool_mgr, with_strict=False)
```

### Using Convenience Functions

```python
from metorial_openai_compatible import build_openai_compatible_tools, call_openai_compatible_tools

async def example_with_functions():
    # Get tools in OpenAI format
    tools = build_openai_compatible_tools(tool_manager, with_strict=True)
    
    # Call tools from OpenAI-compatible response
    tool_messages = await call_openai_compatible_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialOpenAICompatibleSession`

Main session class for OpenAI-compatible integration.

```python
session = MetorialOpenAICompatibleSession(tool_manager, with_strict=False)
```

**Parameters:**
- `tool_manager`: Metorial tool manager instance
- `with_strict`: Enable strict parameter validation (default: False)

**Properties:**
- `tools`: List of tools in OpenAI function calling format

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return tool messages

### `build_openai_compatible_tools(tool_mgr, with_strict=False)`

Build OpenAI-compatible tool definitions.

**Parameters:**
- `tool_mgr`: Tool manager instance
- `with_strict`: Enable strict mode (default: False)

**Returns:** List of tool definitions in OpenAI format

### `call_openai_compatible_tools(tool_mgr, tool_calls)`

Execute tool calls from OpenAI-compatible response.

**Returns:** List of tool messages

## Tool Format

Tools are converted to OpenAI's function calling format:

```python
{
    "type": "function",
    "function": {
        "name": "tool_name",
        "description": "Tool description",
        "parameters": {
            "type": "object",
            "properties": {...},
            "required": [...]
        },
        "strict": True  # Only if with_strict=True
    }
}
```

## Strict Mode

When `with_strict=True`, the `strict` field is added to function definitions for providers that support strict parameter validation (like OpenAI and XAI).

## Provider Implementations

This package serves as the base for:

- **metorial-xai**: XAI (Grok) with strict mode enabled
- **metorial-deepseek**: DeepSeek without strict mode
- **metorial-togetherai**: Together AI without strict mode

## Error Handling

```python
try:
    tool_messages = await session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## Dependencies

- `metorial-mcp-session>=1.0.0`
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
