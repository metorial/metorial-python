# metorial-google

Google (Gemini) provider integration for Metorial - enables using Metorial tools with Google's Gemini models through function calling.

## Installation

```bash
pip install metorial-google
# or
uv add metorial-google
# or
poetry add metorial-google
```

## Features

- 🤖 **Gemini Integration**: Full support for Gemini Pro, Gemini Flash, and other Google AI models
- 🛠️ **Function Calling**: Native Google function calling support
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to Google function declaration format
- ⚡ **Async Support**: Full async/await support

## Usage

### Basic Usage

```python
import asyncio
import google.generativeai as genai
from metorial import Metorial
from metorial_google import MetorialGoogleSession

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    genai.configure(api_key="your-google-api-key")
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
        # Create Google-specific wrapper
        google_session = MetorialGoogleSession(session.tool_manager)
        
        model = genai.GenerativeModel(
            model_name="gemini-pro",
            tools=google_session.tools
        )
        
        response = model.generate_content("What can you help me with?")
        
        # Handle function calls if present
        if response.candidates[0].content.parts:
            function_calls = [
                part.function_call for part in response.candidates[0].content.parts
                if hasattr(part, 'function_call') and part.function_call
            ]
            
            if function_calls:
                tool_response = await google_session.call_tools(function_calls)
                # Continue conversation with tool_response

asyncio.run(main())
```

### Using Convenience Functions

```python
from metorial_google import build_google_tools, call_google_tools

async def example_with_functions():
    # Get tools in Google format
    tools = build_google_tools(tool_manager)
    
    # Call tools from Google response
    response = await call_google_tools(tool_manager, function_calls)
```

## API Reference

### `MetorialGoogleSession`

Main session class for Google integration.

```python
session = MetorialGoogleSession(tool_manager)
```

**Properties:**
- `tools`: List of tools in Google function declaration format

**Methods:**
- `async call_tools(function_calls)`: Execute function calls and return user content

### `build_google_tools(tool_mgr)`

Build Google-compatible tool definitions.

**Returns:** List of tool definitions in Google format

### `call_google_tools(tool_mgr, function_calls)`

Execute function calls from Google response.

**Returns:** User content with function responses

## Tool Format

Tools are converted to Google's function declaration format:

```python
[{
    "function_declarations": [
        {
            "name": "tool_name",
            "description": "Tool description",
            "parameters": {
                "type": "object",
                "properties": {...},
                "required": [...]
            }
        }
    ]
}]
```

## Error Handling

```python
try:
    response = await google_session.call_tools(function_calls)
except Exception as e:
    print(f"Tool execution failed: {e}")
```

Tool errors are returned as error objects in the response format.

## Dependencies

- `google-generativeai>=0.3.0`
- `metorial-mcp-session>=1.0.0`
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
