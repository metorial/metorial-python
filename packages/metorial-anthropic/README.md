# metorial-anthropic

Anthropic (Claude) provider integration for Metorial - enables using Metorial tools with Claude models through Anthropic's tool calling API.

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

## Usage

### Basic Usage

```python
import asyncio
from anthropic import Anthropic
from metorial import Metorial
from metorial_anthropic import MetorialAnthropicSession

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    anthropic = Anthropic(api_key="your-anthropic-api-key")
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
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

## Dependencies

- `anthropic>=0.40.0`
- `metorial-mcp-session>=1.0.0`
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
