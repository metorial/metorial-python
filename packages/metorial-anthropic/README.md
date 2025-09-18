# metorial-anthropic

Anthropic (Claude) provider integration for Metorial.

## Installation

```bash
pip install metorial-anthropic
# or
uv add metorial-anthropic
# or
poetry add metorial-anthropic
```

## Features

- 🤖 **Claude Integration**: Full support for Claude 3.5, Claude 3, and other Anthropic models
- 🛠️ **Tool Calling**: Native Anthropic tool format support
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to Anthropic tool format
- ⚡ **Async Support**: Full async/await support

## Supported Models

All Anthropic Claude models that support tool calling:

- `claude-3-5-sonnet-20241022`: Latest Claude 3.5 Sonnet with enhanced capabilities
- `claude-3-5-haiku-20241022`: Fastest Claude 3.5 model
- `claude-3-opus-20240229`: Most capable Claude 3 model
- `claude-3-sonnet-20240229`: Balanced Claude 3 model
- `claude-3-haiku-20240307`: Fastest Claude 3 model

## Usage

### Quick Start (Recommended)

```python
import asyncio
from anthropic import AsyncAnthropic
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  anthropic_client = AsyncAnthropic(
    api_key="...your-anthropic-api-key..."
  )
  
  # One-liner chat with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    anthropic_client,
    model="claude-3-5-sonnet-20241022",
    max_iterations=25
  )
  
  print("Response:", response)

asyncio.run(main())
```

### Streaming Chat

```python
import asyncio
from anthropic import AsyncAnthropic
from metorial import Metorial
from metorial.types import StreamEventType

async def streaming_example():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  anthropic_client = AsyncAnthropic(
    api_key="...your-anthropic-api-key..."
  )
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      anthropic_client, session, messages, 
      model="claude-3-5-sonnet-20241022",
      max_iterations=25
    ):
      if event.type == StreamEventType.CONTENT:
        print(f"🤖 {event.content}", end="", flush=True)
      elif event.type == StreamEventType.TOOL_CALL:
        print(f"\n🔧 Executing {len(event.tool_calls)} tool(s)...")
      elif event.type == StreamEventType.COMPLETE:
        print(f"\n✅ Complete!")
  
  await metorial.with_session("...your-server-deployment-id...", stream_action)

asyncio.run(streaming_example())
```

### Advanced Usage with Session Management

```python
import asyncio
from anthropic import Anthropic
from metorial import Metorial
from metorial_anthropic import MetorialAnthropicSession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  anthropic = Anthropic(api_key="...your-anthropic-api-key...")
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create Anthropic-specific wrapper
    anthropic_session = MetorialAnthropicSession(session.tool_manager)
    
    messages = [
      {"role": "user", "content": "What are the latest commits?"}
    ]
    
    # Remove duplicate tools by name (Anthropic requirement)
    unique_tools = list({t["name"]: t for t in anthropic_session.tools}.values())
    
    response = await anthropic.messages.create(
      model="claude-3-5-sonnet-20241022",
      max_tokens=1024,
      messages=messages,
      tools=unique_tools
    )
    
    # Handle tool calls
    tool_calls = [c for c in response.content if c.type == "tool_use"]
    if tool_calls:
      tool_response = await anthropic_session.call_tools(tool_calls)
      messages.append({"role": "assistant", "content": response.content})
      messages.append(tool_response)
      
      # Continue conversation...

asyncio.run(main())
```

### Using Convenience Functions

```python
from metorial_anthropic import build_anthropic_tools, call_anthropic_tools

async def example_with_functions():
  # Get tools in Anthropic format
  tools = build_anthropic_tools(tool_manager)
  
  # Call tools from Anthropic response
  tool_response = await call_anthropic_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialAnthropicSession`

Main session class for Anthropic integration.

```python
session = MetorialAnthropicSession(tool_manager)
```

**Properties:**
- `tools`: List of tools in Anthropic format

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return user message

### `build_anthropic_tools(tool_mgr)`

Build Anthropic-compatible tool definitions.

**Returns:** List of tool definitions in Anthropic format

### `call_anthropic_tools(tool_mgr, tool_calls)`

Execute tool calls from Anthropic response.

**Returns:** User message with tool results

## Tool Format

Tools are converted to Anthropic's format:

```python
{
  "name": "tool_name",
  "description": "Tool description",
  "input_schema": {
    "type": "object",
    "properties": {...},
    "required": [...]
  }
}
```

## Error Handling

```python
try:
    tool_response = await anthropic_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as error messages in the response format.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
