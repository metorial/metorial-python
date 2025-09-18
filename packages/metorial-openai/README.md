# metorial-openai

OpenAI provider integration for Metorial.

## Installation

```bash
pip install metorial-openai
# or
uv add metorial-openai
# or
poetry add metorial-openai
```

## Features

- 🤖 **OpenAI Integration**: Full support for GPT-4, GPT-3.5, and other OpenAI models
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ⚡ **Async Support**: Full async/await support

## Supported Models

All OpenAI models that support function calling:

- `gpt-4o`: Latest GPT-4 Omni model
- `gpt-4o-mini`: Smaller, faster GPT-4 Omni model
- `gpt-4-turbo`: GPT-4 Turbo
- `gpt-4`: Standard GPT-4
- `gpt-3.5-turbo`: GPT-3.5 Turbo
- And other function calling enabled models

## Usage

### Quick Start (Recommended)

```python
import asyncio
from openai import OpenAI
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  openai_client = OpenAI(api_key="...your-openai-api-key...")
  
  # One-liner chat with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    openai_client,
    model="gpt-4o",
    max_iterations=25
  )
  
  print("Response:", response)

asyncio.run(main())
```

### Streaming Chat

```python
import asyncio
from openai import OpenAI
from metorial import Metorial
from metorial.types import StreamEventType

async def streaming_example():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  openai_client = OpenAI(api_key="...your-openai-api-key...")
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      openai_client, session, messages, 
      model="gpt-4o",
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
from metorial_openai import MetorialOpenAISession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  openai_client = OpenAI(api_key="...your-openai-api-key...")
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create OpenAI-specific wrapper
    openai_session = MetorialOpenAISession(session.tool_manager)
    
    messages = [
      {"role": "user", "content": "What are the latest commits?"}
    ]
    
    response = openai_client.chat.completions.create(
      model="gpt-4o",
      messages=messages,
      tools=openai_session.tools
    )
    
    # Handle tool calls
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
      tool_responses = await openai_session.call_tools(tool_calls)
      
      # Add assistant message and tool responses
      messages.append(response.choices[0].message)
      messages.extend(tool_responses)
      
      # Continue conversation...

asyncio.run(main())
```

### Using Convenience Functions

```python
from metorial_openai import build_openai_tools, call_openai_tools

async def example_with_functions():
  # Get tools in OpenAI format
  tools = build_openai_tools(tool_manager)
  
  # Call tools from OpenAI response
  tool_messages = await call_openai_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialOpenAISession`

Main session class for OpenAI integration.

```python
session = MetorialOpenAISession(tool_manager)
```

**Properties:**
- `tools`: List of tools in OpenAI format

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return tool messages

### `build_openai_tools(tool_mgr)`

Build OpenAI-compatible tool definitions.

**Returns:** List of tool definitions in OpenAI format

### `call_openai_tools(tool_mgr, tool_calls)`

Execute tool calls from OpenAI response.

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
    }
  }
}
```

## Error Handling

```python
try:
    tool_messages = await openai_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
