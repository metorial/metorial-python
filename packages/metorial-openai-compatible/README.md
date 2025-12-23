# metorial-openai-compatible

OpenAI-compatible provider integration for Metorial. Works with any API that follows the OpenAI chat completions format.

## Installation

```bash
pip install metorial openai
```

## Quick Start

```python
import asyncio
from metorial import Metorial, MetorialOpenAICompatible
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")

# Works with any OpenAI-compatible API
client = AsyncOpenAI(
    api_key="your-api-key",
    base_url="https://your-api-endpoint.com/v1"
)

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news?"}]

        for _ in range(10):
            response = await client.chat.completions.create(
                model="your-model",
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
        MetorialOpenAICompatible.chat_completions,
        {"serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}]},
        session_handler
    )

asyncio.run(main())
```

## Streaming

```python
import asyncio
from metorial import Metorial, MetorialOpenAICompatible
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
client = AsyncOpenAI(
    api_key="your-api-key",
    base_url="https://your-api-endpoint.com/v1"
)

async def main():
    async def session_handler(session):
        messages = [{"role": "user", "content": "What's the latest news?"}]

        stream = await client.chat.completions.create(
            model="your-model",
            messages=messages,
            tools=session["tools"],
            stream=True
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

        await session["closeSession"]()

    await metorial.with_provider_session(
        MetorialOpenAICompatible.chat_completions,
        {
            "serverDeployments": [{"serverDeploymentId": "your-server-deployment-id"}],
            "streaming": True,  # Required for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

## Compatible Providers

Any provider with an OpenAI-compatible API:

- DeepSeek (`https://api.deepseek.com`)
- Together AI (`https://api.together.xyz/v1`)
- XAI (`https://api.x.ai/v1`)
- Groq (`https://api.groq.com/openai/v1`)
- And many more...

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
