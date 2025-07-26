# metorial

The main Python client for Metorial - The open source integration platform for agentic AI. This is the primary package that provides the core client and session management functionality.

## Installation

```bash
pip install metorial
# or
uv add metorial
# or
poetry add metorial
```

## Features

- 🔧 **Multi-Provider Support**: Use the same tools across different AI providers
- 🚀 **Easy Integration**: Simple async/await interface
- 📡 **Session Management**: Automatic session lifecycle handling
- 🛠️ **Tool Discovery**: Automatic tool detection and formatting
- 🔄 **Format Conversion**: Provider-specific tool format conversion

## Supported Providers

- ✅ OpenAI (GPT-4, GPT-3.5)
- ✅ Anthropic (Claude)
- ✅ Google (Gemini)
- ✅ Mistral AI
- ✅ DeepSeek
- ✅ Together AI
- ✅ XAI (Grok)

## Usage

### Basic Usage

```python
import asyncio
from metorial import Metorial

async def main():
    # Initialize Metorial client
    metorial = Metorial(api_key="your-metorial-api-key")
    
    # Create session with your server deployments
    async with metorial.session(["your-server-deployment-id"]) as session:
        # Access tool manager
        tool_manager = session.tool_manager
        
        # Use with provider-specific packages
        # See provider packages for specific integrations

asyncio.run(main())
```

### With Provider Packages

Use metorial with provider-specific packages:

```python
import asyncio
from metorial import Metorial
from metorial_openai import MetorialOpenAISession
from openai import OpenAI

async def main():
    # Initialize clients
    metorial = Metorial(api_key="your-metorial-api-key")
    openai_client = OpenAI(api_key="your-openai-api-key")
    
    # Create session
    async with metorial.session(["deployment-id"]) as session:
        # Use with OpenAI
        openai_session = MetorialOpenAISession(session.tool_manager)
        
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Help me"}],
            tools=openai_session.tools
        )
        
        # Handle tool calls
        if response.choices[0].message.tool_calls:
            tool_responses = await openai_session.call_tools(
                response.choices[0].message.tool_calls
            )

asyncio.run(main())
```

## API Reference

### `Metorial`

Main client class for Metorial.

```python
client = Metorial(api_key="your-api-key")
```

**Parameters:**
- `api_key`: Your Metorial API key

**Methods:**
- `async session(deployment_ids)`: Create a session with specified deployments

### Session Context Manager

```python
async with metorial.session(["deployment-id"]) as session:
    # session.tool_manager provides access to tools
```

**Properties:**
- `tool_manager`: Manager for executing tools

## Provider Integration

This package works with provider-specific packages:

- `metorial-openai`: OpenAI integration
- `metorial-anthropic`: Anthropic (Claude) integration  
- `metorial-google`: Google (Gemini) integration
- `metorial-mistral`: Mistral AI integration
- `metorial-xai`: XAI (Grok) integration
- `metorial-deepseek`: DeepSeek integration
- `metorial-togetherai`: Together AI integration

## Error Handling

```python
from metorial import MetorialAPIError

try:
    async with metorial.session(["deployment-id"]) as session:
        # Your code here
        pass
except MetorialAPIError as e:
    print(f"API Error: {e.message} (Status: {e.status})")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Configuration

### Environment Variables

You can also configure the client using environment variables:

```bash
export METORIAL_API_KEY="your-api-key"
```

```python
# Will use METORIAL_API_KEY if no api_key provided
metorial = Metorial()
```

## Dependencies

- `metorial-core>=1.0.0`
- `metorial-mcp-session>=1.0.0`
- `typing-extensions>=4.0.0`

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
