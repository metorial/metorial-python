# Metorial Python SDK - Core

The core package for the official Python SDK for [Metorial](https://metorial.com) - Connect your AI agents to any MCP server with a single line of code.

[Sign up for a free account](https://app.metorial.com) to get started.

## Installation

```bash
pip install metorial
```

## Quick Start

```bash
pip install metorial anthropic
```

```python
import asyncio
from metorial import Metorial, MetorialAnthropic
from anthropic import AsyncAnthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic = AsyncAnthropic(api_key="your-anthropic-api-key")

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news on Hacker News?"}]

        for _ in range(10):
            response = await anthropic.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                messages=messages,
                tools=session["tools"]
            )

            tool_calls = [b for b in response.content if b.type == "tool_use"]
            if not tool_calls:
                print(response.content[0].text)
                break

            tool_responses = await session["callTools"](tool_calls)
            messages.append({"role": "assistant", "content": response.content})
            messages.append(tool_responses)

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialAnthropic,
        {"serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}]},
        session_handler
    )

asyncio.run(main())
```

## Session Options

### Streaming Mode

When using streaming with tool calls, enable the `streaming` flag:

```python
await metorial.with_provider_session(
    metorial_provider,
    {
        "serverDeployments": [...],
        "streaming": True,  # Required for streaming with tool calls
    },
    session_handler
)
```

### Closing Sessions

Always close your session when done to free up resources:

```python
async def session_handler(session):
    tools = session["tools"]
    close_session = session["closeSession"]

    # Use tools...

    # When finished, close the session
    await close_session()
```

## Session Object

The session object passed to your callback provides:

```python
async def session_handler(session):
    tools = session["tools"]           # Tool definitions formatted for your provider
    call_tools = session["callTools"]  # Execute tools and get responses
    close_session = session["closeSession"]  # Close the session when done (always call this!)
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

## Support

[Documentation](https://metorial.com/docs) · [GitHub Issues](https://github.com/metorial/metorial-python/issues) · [Email Support](mailto:support@metorial.com)
