# metorial-togetherai

Together AI provider integration for Metorial.

## Installation

```bash
pip install metorial-togetherai
# or
uv add metorial-togetherai
# or
poetry add metorial-togetherai
```

## Features

- 🤖 **Together AI Integration**: Full support for Llama, Mixtral, and other Together AI models
- 🛠️ **Function Calling**: OpenAI-compatible function calling support
- 📡 **Session Management**: Automatic tool lifecycle handling
- ⚡ **Async Support**: Full async/await support

## Supported Models

Popular models available through Together AI:

- `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo`: Llama 3.1 70B
- `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`: Llama 3.1 8B  
- `mistralai/Mixtral-8x7B-Instruct-v0.1`: Mixtral 8x7B
- `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`: Nous Hermes 2
- And many more...

## Usage

### Quick Start (Recommended)

```python
import asyncio
from openai import AsyncOpenAI
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  together_client = AsyncOpenAI(
    api_key="...your-together-api-key...", 
    base_url="https://api.together.xyz/v1"
  )
  
  # One-liner chat with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    together_client,
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
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
  together_client = AsyncOpenAI(
    api_key="...your-together-api-key...",
    base_url="https://api.together.xyz/v1"
  )
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      together_client, session, messages, 
      model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
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
from openai import OpenAI
from metorial import Metorial
from metorial_togetherai import MetorialTogetherAISession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  
  # Together AI uses OpenAI-compatible client
  together_client = OpenAI(
    api_key="...your-together-api-key...",
    base_url="https://api.together.xyz/v1"
  )
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create Together AI-specific wrapper
    together_session = MetorialTogetherAISession(session.tool_manager)
    
    messages = [
      {"role": "user", "content": "What are the latest commits?"}
    ]
    
    response = together_client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      messages=messages,
      tools=together_session.tools
    )
    
    # Handle tool calls
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
      tool_responses = await together_session.call_tools(tool_calls)
      
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
from metorial_togetherai import build_togetherai_tools, call_togetherai_tools

async def example():
  # Get tools in Together AI format
  tools = build_togetherai_tools(tool_manager)
  
  # Call tools from Together AI response
  tool_messages = await call_togetherai_tools(tool_manager, tool_calls)
```

## API Reference

### `MetorialTogetherAISession`

Main session class for Together AI integration.

```python
session = MetorialTogetherAISession(tool_manager)
```

**Properties:**
- `tools`: List of tools in OpenAI-compatible format

**Methods:**
- `async call_tools(tool_calls)`: Execute tool calls and return tool messages

### `build_togetherai_tools(tool_mgr)`

Build Together AI-compatible tool definitions.

**Returns:** List of tool definitions in OpenAI format

### `call_togetherai_tools(tool_mgr, tool_calls)`

Execute tool calls from Together AI response.

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

## Together AI API Configuration

Together AI uses the OpenAI-compatible API format. Configure your client like this:

```python
from openai import OpenAI

client = OpenAI(
  api_key="...your-together-api-key...",
  base_url="https://api.together.xyz/v1"
)
```

## Error Handling

```python
try:
    tool_messages = await together_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
