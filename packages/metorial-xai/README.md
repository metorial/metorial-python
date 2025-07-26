# metorial-xai

XAI (Grok) provider integration for Metorial - enables using Metorial tools with XAI's Grok models through OpenAI-compatible function calling.

## Installation

```bash
pip install metorial-xai
# or
uv add metorial-xai
# or
poetry add metorial-xai
```

## Features

- 🤖 **Grok Integration**: Full support for Grok models through XAI API
- 🛠️ **Function Calling**: OpenAI-compatible function calling support
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ✅ **Strict Mode**: Built-in strict parameter validation
- ⚡ **Async Support**: Full async/await support

## Usage

### Basic Usage

```python
import asyncio
from openai import OpenAI
from metorial import Metorial
from metorial_xai import MetorialXAISession

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    
    # XAI uses OpenAI-compatible client
    xai_client = OpenAI(
        api_key="your-xai-api-key",
        base_url="https://api.x.ai/v1"
    )
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
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

async def example_with_functions():
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
    api_key="your-xai-api-key",
    base_url="https://api.x.ai/v1"
)
```

## Error Handling

```python
try:
    tool_messages = await xai_session.call_tools(tool_calls)
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
