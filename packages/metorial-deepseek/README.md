# metorial-deepseek

DeepSeek provider integration for Metorial - enables using Metorial tools with DeepSeek's language models through OpenAI-compatible function calling.

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
- 🛠️ **Function Calling**: OpenAI-compatible function calling support
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ⚡ **Async Support**: Full async/await support

## Usage

### Basic Usage

```python
import asyncio
from openai import OpenAI
from metorial import Metorial
from metorial_deepseek import MetorialDeepSeekSession

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    
    # DeepSeek uses OpenAI-compatible client
    deepseek_client = OpenAI(
        api_key="your-deepseek-api-key",
        base_url="https://api.deepseek.com"
    )
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
        # Create DeepSeek-specific wrapper
        deepseek_session = MetorialDeepSeekSession(session.tool_manager)
        
        messages = [
            {"role": "user", "content": "Help me analyze this code"}
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
    api_key="your-deepseek-api-key",
    base_url="https://api.deepseek.com"
)
```

## Supported Models

- `deepseek-chat`: General-purpose conversational model
- `deepseek-coder`: Specialized for code-related tasks

## Error Handling

```python
try:
    tool_messages = await deepseek_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## Dependencies

- `metorial-openai-compatible>=1.0.0`
- `metorial-mcp-session>=1.0.0`
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
