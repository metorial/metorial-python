# metorial-xai

XAI (Grok) provider integration for Metorial.

## Installation

```bash
pip install metorial-xai
# or
uv add metorial-xai
# or
poetry add metorial-xai
```

## Features

- 🤖 **Grok Integration**: Full support for Grok models
- 📡 **Session Management**: Automatic tool lifecycle handling
- ✅ **Strict Mode**: Built-in strict parameter validation
- ⚡ **Async Support**: Full async/await support

## Supported Models

All XAI Grok models that support function calling:

- `grok-beta`: Latest Grok model with enhanced reasoning
- `grok-2-1212`: Grok 2.0 December 2024 release
- `grok-2-vision-1212`: Grok 2.0 with vision capabilities

## Usage

### Quick Start (Recommended)

```python
import asyncio
from openai import AsyncOpenAI
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  xai_client = AsyncOpenAI(
    api_key="...your-xai-api-key...", 
    base_url="https://api.x.ai/v1"
  )
  
  # Run with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    xai_client,
    model="grok-beta",
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

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  xai_client = AsyncOpenAI(
    api_key="...your-xai-api-key...",
    base_url="https://api.x.ai/v1"
  )
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      xai_client, session, messages, 
      model="grok-beta",
      max_iterations=25
    ):
      if event.type == StreamEventType.CONTENT:
        print(f"🤖 {event.content}", end="", flush=True)
      elif event.type == StreamEventType.TOOL_CALL:
        print(f"\n🔧 Executing {len(event.tool_calls)} tool(s)...")
      elif event.type == StreamEventType.COMPLETE:
        print(f"\n✅ Complete!")
  
  await metorial.with_session("...your-server-deployment-id...", stream_action)

asyncio.run(main())
```

### Advanced Usage with Session Management

```python
import asyncio
from openai import OpenAI
from metorial import Metorial
from metorial_xai import MetorialXAISession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  
  # XAI uses OpenAI-compatible client
  xai_client = OpenAI(
    api_key="...your-xai-api-key...",
    base_url="https://api.x.ai/v1"
  )
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create XAI-specific wrapper
    xai_session = MetorialXAISession(session.tool_manager)
    
    messages = [
      {"role": "user", "content": "What are the latest commits?"}
    ]
    
    response = xai_client.chat.completions.create(
      model="grok-beta",
      messages=messages,
      tools=xai_session.tools
    )
    
    # Handle tool calls
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
      tool_responses = await xai_session.call_tools(tool_calls)
      
      # Add to conversation
      messages.append({
        "role": "assistant",
        "tool_calls": tool_calls
      })
      messages.extend(tool_responses)
      
      # Continue conversation...

asyncio.run(main())
```

### Using Convenience Functions

```python
from metorial_xai import build_xai_tools, call_xai_tools

async def example():
  # Get tools in XAI format
  tools = build_xai_tools(tool_manager)
  
  # Call tools from XAI response
  tool_messages = await call_xai_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialXAISession`

Main session class for XAI integration.

```python
session = MetorialXAISession(tool_manager)
```

**Properties:**
- `tools`: List of tools in OpenAI-compatible format with strict mode

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return tool messages

### `build_xai_tools(tool_mgr)`

Build XAI-compatible tool definitions.

**Returns:** List of tool definitions in OpenAI format with strict mode

### `call_xai_tools(tool_mgr, tool_calls)`

Execute tool calls from XAI response.

**Returns:** List of tool messages

## Tool Format

Tools are converted to OpenAI-compatible format with strict mode enabled:

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
    "strict": True
  }
}
```

## XAI API Configuration

XAI uses the OpenAI-compatible API format. Configure your client like this:

```python
from openai import OpenAI

client = OpenAI(
  api_key="...your-xai-api-key...",
  base_url="https://api.x.ai/v1"
)
```

## Error Handling

```python
try:
  response = await metorial.run(
    "Your query", "...deployment-id...", xai_client, 
    model="grok-beta", max_iterations=25
  )
except Exception as e:
  print(f"Request failed: {e}")
```

Tool errors are automatically handled and returned as error messages.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
