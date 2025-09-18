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
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ⚡ **Async Support**: Full async/await support

## Usage

### Quick Start (Recommended)

This package serves as a base for provider-specific implementations. For end-user usage, use the specific provider packages like `metorial-xai`, `metorial-deepseek`, or `metorial-togetherai`.

### Direct Usage (Advanced)

```python
import asyncio
from openai import AsyncOpenAI
from metorial import Metorial
from metorial_openai_compatible import MetorialOpenAICompatibleSession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  compatible_client = AsyncOpenAI(
    api_key="...your-provider-api-key...", 
    base_url="https://your-provider-url/v1"
  )
  
  # Run with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    compatible_client,
    model="your-model-name",
    max_iterations=25
  )
  
  print("Response:", response)

asyncio.run(main())
```

### Streaming Chat

```python
import asyncio
from openai import AsyncOpenAI
from metorial import Metorial
from metorial.types import StreamEventType

async def example():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  compatible_client = AsyncOpenAI(
    api_key="...your-provider-api-key...",
    base_url="https://your-provider-url/v1"
  )
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      compatible_client, session, messages, 
      model="your-model-name",
      max_iterations=25
    ):
      if event.type == StreamEventType.CONTENT:
        print(f"🤖 {event.content}", end="", flush=True)
      elif event.type == StreamEventType.TOOL_CALL:
        print(f"\n🔧 Executing {len(event.tool_calls)} tool(s)...")
      elif event.type == StreamEventType.COMPLETE:
        print(f"\n✅ Complete!")
  
  await metorial.with_session("...your-server-deployment-id...", stream_action)

asyncio.run(example())
```

### Advanced Usage with Session Management

```python
import asyncio
from metorial import Metorial
from metorial_openai_compatible import MetorialOpenAICompatibleSession

async def main():
  # Initialize Metorial
  metorial = Metorial(api_key="...your-metorial-api-key...")
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
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

async def example():
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

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
