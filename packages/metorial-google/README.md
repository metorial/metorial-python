# metorial-google

Google (Gemini) provider integration for Metorial.

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
- 📡 **Session Management**: Automatic tool lifecycle handling
- 🔄 **Format Conversion**: Converts Metorial tools to Google function declaration format
- ⚡ **Async Support**: Full async/await support

## Supported Models

All Google Gemini models that support function calling:

- `gemini-1.5-pro`: Most capable Gemini model with 2M context window
- `gemini-1.5-flash`: Fast and efficient Gemini model  
- `gemini-pro`: Standard Gemini Pro model
- `gemini-pro-vision`: Gemini Pro with vision capabilities

## Usage

### Quick Start (Recommended)

```python
import asyncio
import google.generativeai as genai
from metorial import Metorial

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...") # async by default
  genai.configure(api_key="...your-google-api-key...")
  google_client = genai.GenerativeModel('gemini-pro')
  
  # One-liner chat with automatic session management
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "...your-mcp-server-deployment-id...", # can also be list
    google_client,
    model="gemini-pro",
    max_iterations=25
  )
  
  print("Response:", response)

asyncio.run(main())
```

### Streaming Chat

```python
import asyncio
import google.generativeai as genai
from metorial import Metorial
from metorial.types import StreamEventType

async def streaming_example():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  genai.configure(api_key="...your-google-api-key...")
  google_client = genai.GenerativeModel('gemini-pro')
  
  # Streaming chat with real-time responses
  async def stream_action(session):
    messages = [
      {"role": "user", "content": "Explain quantum computing"}
    ]
    
    async for event in metorial.stream(
      google_client, session, messages, 
      model="gemini-pro",
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
import google.generativeai as genai
from metorial import Metorial
from metorial_google import MetorialGoogleSession

async def main():
  # Initialize clients
  metorial = Metorial(api_key="...your-metorial-api-key...")
  genai.configure(api_key="...your-google-api-key...")
  
  # Create session with your server deployments
  async with metorial.session(["...your-server-deployment-id..."]) as session:
    # Create Google-specific wrapper
    google_session = MetorialGoogleSession(session.tool_manager)
    
    model = genai.GenerativeModel(
      model_name="gemini-pro",
      tools=google_session.tools
    )
    
    response = model.generate_content("What are the latest commits?")
    
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

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
