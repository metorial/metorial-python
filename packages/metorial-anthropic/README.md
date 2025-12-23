# metorial-anthropic

Anthropic (Claude) provider integration for Metorial.

## Installation

```bash
pip install metorial anthropic
```

## Quick Start

```python
import asyncio
from metorial import Metorial, MetorialAnthropic
from anthropic import AsyncAnthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic = AsyncAnthropic(api_key="your-anthropic-api-key")

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news?"}]

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

## Streaming

```python
import asyncio
from metorial import Metorial, MetorialAnthropic
from anthropic import AsyncAnthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic = AsyncAnthropic(api_key="your-anthropic-api-key")

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news?"}]

        for _ in range(10):
            async with anthropic.messages.stream(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                messages=messages,
                tools=session["tools"]
            ) as stream:
                async for text in stream.text_stream:
                    print(text, end="", flush=True)
                response = await stream.get_final_message()

            tool_calls = [b for b in response.content if b.type == "tool_use"]
            if not tool_calls:
                print()
                break

            tool_responses = await session["callTools"](tool_calls)
            messages.append({"role": "assistant", "content": response.content})
            messages.append(tool_responses)

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialAnthropic,
        {
            "serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}],
            "streaming": True,  # Required for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

## Supported Models

All Anthropic Claude models that support tool calling:

- `claude-sonnet-4-5`: Latest Claude Sonnet
- `claude-opus-4`: Most capable Claude model
- `claude-3-5-sonnet-20241022`: Claude 3.5 Sonnet
- `claude-3-5-haiku-20241022`: Fastest Claude 3.5 model

## Session Object

```python
async def session_handler(session):
    tools = session["tools"]           # Tool definitions in Anthropic format
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
