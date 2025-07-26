# metorial-openai

OpenAI provider integration for Metorial - enables using Metorial tools with OpenAI's language models through function calling.

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
- 🛠️ **Function Calling**: Native OpenAI function calling support
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to OpenAI function format
- ✅ **Strict Mode**: Optional strict parameter validation
- ⚡ **Async Support**: Full async/await support

## Usage

### Basic Usage

```python
import asyncio
from openai import OpenAI
from metorial import Metorial
from metorial_openai import MetorialOpenAISession

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    openai_client = OpenAI(api_key="your-openai-api-key")
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
        # Create OpenAI-specific wrapper
        openai_session = MetorialOpenAISession(session.tool_manager)
        
        messages = [
            {"role": "user", "content": "What are the latest commits?"}
        ]
        
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            tools=openai_session.tools
        )
        
        # Handle tool calls
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            tool_responses = await openai_session.call_tools(tool_calls)
            
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
- `tools`: List of tools in OpenAI function calling format

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

## Supported Models

All OpenAI models that support function calling:

- `gpt-4o`: Latest GPT-4 Omni model
- `gpt-4o-mini`: Smaller, faster GPT-4 Omni model
- `gpt-4-turbo`: GPT-4 Turbo
- `gpt-4`: Standard GPT-4
- `gpt-3.5-turbo`: GPT-3.5 Turbo
- And other function calling enabled models

## Error Handling

```python
try:
    tool_messages = await openai_session.call_tools(tool_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as tool messages with error content.

## Dependencies

- `openai>=1.0.0`
- `metorial-mcp-session>=1.0.0`  
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
