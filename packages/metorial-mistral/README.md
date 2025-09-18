# metorial-mistral

Mistral AI provider integration for Metorial.

## Installation

```bash
pip install metorial-mistral
# or
uv add metorial-mistral
# or
poetry add metorial-mistral
```

## Features

- 🤖 **Mistral Integration**: Full support for Mistral Large, Codestral, and other Mistral models
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to Mistral function format
- ⚡ **Async Support**: Full async/await support

## Supported Models

All Mistral AI models that support function calling:

- `mistral-large-latest`: Latest Mistral Large model with enhanced reasoning
- `mistral-large-2411`: Mistral Large November 2024
- `mistral-large-2407`: Mistral Large July 2024
- `mistral-small-latest`: Smaller, faster Mistral model
- `codestral-latest`: Specialized for code generation and analysis

## Usage

### Quick Start (Recommended)

```python
import asyncio
from mistralai.async_client import MistralAsyncClient
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  mistral_client = MistralAsyncClient(
    api_key="...your-mistral-api-key..."
  )
  
  # One-liner chat with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    mistral_client,
    model="mistral-large-latest",
    max_iterations=25
  )
  
  print("Response:", response)

asyncio.run(main())
```

### Streaming Chat

```python
import asyncio
from mistralai.async_client import MistralAsyncClient
from metorial import Metorial
from metorial.types import StreamEventType

async def streaming_example():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  mistral_client = MistralAsyncClient(
    api_key="...your-mistral-api-key..."
  )
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      mistral_client, session, messages, 
      model="mistral-large-latest",
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
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from metorial import Metorial
from metorial_mistral import MetorialMistralSession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  mistral = MistralClient(api_key="...your-mistral-api-key...")
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create Mistral-specific wrapper
    mistral_session = MetorialMistralSession(session.tool_manager)
    
    messages = [
      ChatMessage(role="user", content="What are the latest commits?")
    ]
    
    response = mistral.chat(
      model="mistral-large-latest",
      messages=messages,
      tools=mistral_session.tools
    )
    
    # Handle tool calls
    if response.choices[0].message.tool_calls:
      tool_responses = await mistral_session.call_tools(response.choices[0].message.tool_calls)
      
      # Add assistant message and tool responses
      messages.append(response.choices[0].message)
      messages.extend(tool_responses)
      
      # Continue conversation...

asyncio.run(main())
```

### Using Convenience Functions

```python
from metorial_mistral import build_mistral_tools, call_mistral_tools

async def example_with_functions():
  # Get tools in Mistral format
  tools = build_mistral_tools(tool_manager)
  
  # Call tools from Mistral response
  tool_messages = await call_mistral_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialMistralSession`

Main session class for Mistral integration.

```python
session = MetorialMistralSession(tool_manager)
```

**Properties:**
- `tools`: List of tools in Mistral format

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return tool messages

### `build_mistral_tools(tool_mgr)`

Build Mistral-compatible tool definitions.

**Returns:** List of tool definitions in Mistral format

### `call_mistral_tools(tool_mgr, tool_calls)`

Execute tool calls from Mistral response.

**Returns:** List of tool messages

## Tool Format

Tools are converted to Mistral's function calling format:

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

## Error Handling

```python
try:
    tool_messages = await mistral_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
