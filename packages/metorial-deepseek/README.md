# metorial-deepseek

DeepSeek provider integration for Metorial.

## Installation

```bash
pip install metorial-deepseek
# or
uv add metorial-deepseek
# or
poetry add metorial-deepseek
```

## Features

- 🤖 **DeepSeek Integration**: Full support for DeepSeek Chat, DeepSeek Coder, and other models
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ⚡ **Async Support**: Full async/await support

## Supported Models

All DeepSeek models available through their API:

- `deepseek-chat`: General-purpose conversational model
- `deepseek-coder`: Specialized for code-related tasks

## Usage

### Quick Start (Recommended)

```python
import asyncio
from openai import AsyncOpenAI
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  deepseek_client = AsyncOpenAI(
    api_key="...your-deepseek-api-key...", 
    base_url="https://api.deepseek.com"
  )
  
  # One-liner chat with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    deepseek_client,
    model="deepseek-chat",
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

async def streaming_example():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  deepseek_client = AsyncOpenAI(
    api_key="...your-deepseek-api-key...",
    base_url="https://api.deepseek.com"
  )
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      deepseek_client, session, messages, 
      model="deepseek-chat",
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
from openai import OpenAI
from metorial import Metorial
from metorial_deepseek import MetorialDeepSeekSession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  
  # DeepSeek uses OpenAI-compatible client
  deepseek_client = OpenAI(
    api_key="...your-deepseek-api-key...",
    base_url="https://api.deepseek.com"
  )
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create DeepSeek-specific wrapper
    deepseek_session = MetorialDeepSeekSession(session.tool_manager)
    
    messages = [
      {"role": "user", "content": "What are the latest commits?"}
    ]
    
    response = deepseek_client.chat.completions.create(
      model="deepseek-chat",
      messages=messages,
      tools=deepseek_session.tools
    )
    
    # Handle tool calls
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
      tool_responses = await deepseek_session.call_tools(tool_calls)
      
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
from metorial_deepseek import build_deepseek_tools, call_deepseek_tools

async def example_with_functions():
  # Get tools in DeepSeek format
  tools = build_deepseek_tools(tool_manager)
  
  # Call tools from DeepSeek response
  tool_messages = await call_deepseek_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialDeepSeekSession`

Main session class for DeepSeek integration.

```python
session = MetorialDeepSeekSession(tool_manager)
```

**Properties:**
- `tools`: List of tools in OpenAI-compatible format

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return tool messages

### `build_deepseek_tools(tool_mgr)`

Build DeepSeek-compatible tool definitions.

**Returns:** List of tool definitions in OpenAI format

### `call_deepseek_tools(tool_mgr, tool_calls)`

Execute tool calls from DeepSeek response.

**Returns:** List of tool messages

## Tool Format

Tools are converted to OpenAI-compatible format (without strict mode):

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
    }
  }
}
```

## DeepSeek API Configuration

DeepSeek uses the OpenAI-compatible API format. Configure your client like this:

```python
from openai import OpenAI

client = OpenAI(
  api_key="...your-deepseek-api-key...",
  base_url="https://api.deepseek.com"
)
```

## Error Handling

```python
try:
    tool_messages = await deepseek_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
