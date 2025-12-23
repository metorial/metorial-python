# metorial-openai

OpenAI provider integration for Metorial.

## Installation

```bash
pip install metorial openai
```

## Quick Start

```python
import asyncio
from metorial import Metorial, MetorialOpenAI
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
openai = AsyncOpenAI(api_key="your-openai-api-key")

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news?"}]

        for _ in range(10):
            response = await openai.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=session["tools"]
            )

            choice = response.choices[0]
            tool_calls = choice.message.tool_calls

            if not tool_calls:
                print(choice.message.content)
                break

            tool_responses = await session["callTools"](tool_calls)
            messages.append({"role": "assistant", "tool_calls": tool_calls})
            messages.extend(tool_responses)

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialOpenAI.chat_completions,
        {"serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}]},
        session_handler
    )

asyncio.run(main())
```

## Streaming

```python
import asyncio
from metorial import Metorial, MetorialOpenAI
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
openai = AsyncOpenAI(api_key="your-openai-api-key")

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news?"}]

        stream = await openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=session["tools"],
            stream=True
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialOpenAI.chat_completions,
        {
            "serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}],
            "streaming": True,  # Required for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

## Supported Models

All OpenAI models that support function calling:

- `gpt-4o`: Latest GPT-4o
- `gpt-4.1`: GPT-4.1
- `o1`: OpenAI o1
- `o3`: OpenAI o3
- `gpt-4-turbo`: GPT-4 Turbo
- `gpt-3.5-turbo`: GPT-3.5 Turbo

## Session Object

```python
async def session_handler(session):
    tools = session["tools"]           # Tool definitions in OpenAI format
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
