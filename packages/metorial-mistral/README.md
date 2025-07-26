# metorial-mistral

Mistral AI provider integration for Metorial - enables using Metorial tools with Mistral's language models through function calling.

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
- 🛠️ **Function Calling**: Native Mistral function calling support
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to Mistral function format
- ✅ **Strict Mode**: Built-in strict parameter validation
- ⚡ **Async Support**: Full async/await support

## Usage

### Basic Usage

```python
import asyncio
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from metorial import Metorial
from metorial_mistral import MetorialMistralSession

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    mistral = MistralClient(api_key="your-mistral-api-key")
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
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

## Dependencies

- `mistralai>=1.0.0`
- `metorial-mcp-session>=1.0.0`
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
