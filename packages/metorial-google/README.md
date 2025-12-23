# metorial-google

Google (Gemini) provider integration for Metorial.

## Installation

```bash
pip install metorial google-generativeai
```

## Quick Start

```python
import asyncio
from metorial import Metorial, MetorialGoogle
import google.generativeai as genai

metorial = Metorial(api_key="your-metorial-api-key")
genai.configure(api_key="your-google-api-key")

async def main():
    async def session_handler(session):
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            tools=session["tools"]
        )

        response = await model.generate_content_async("What's the latest news?")

        # Handle function calls if present
        # ... tool call handling logic

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialGoogle,
        {"serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}]},
        session_handler
    )

asyncio.run(main())
```

## Streaming

```python
import asyncio
from metorial import Metorial, MetorialGoogle
import google.generativeai as genai

metorial = Metorial(api_key="your-metorial-api-key")
genai.configure(api_key="your-google-api-key")

async def main():
    async def session_handler(session):
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            tools=session["tools"]
        )

        response = await model.generate_content_async(
            "What's the latest news?",
            stream=True
        )

        async for chunk in response:
            print(chunk.text, end="", flush=True)

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialGoogle,
        {
            "serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}],
            "streaming": True,  # Required for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

## Supported Models

- `gemini-2.5-pro`: Most capable Gemini model
- `gemini-2.5-flash`: Fast Gemini model
- `gemini-pro`: Gemini Pro

## Session Object

```python
async def session_handler(session):
    tools = session["tools"]           # Tool definitions in Gemini format
    call_tools = session["callTools"]  # Execute tools and get responses
    close_session = session["closeSession"]  # Close the session when done
```

## Error Handling

```python
from metorial import MetorialAPIError

try:
    await metorial.with_provider_session(...)
except MetorialAPIError as e:
    print(f"API Error: {e.message} (Status: {e.status})")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
