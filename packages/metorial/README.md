# Metorial Python SDK

The official Python SDK for [Metorial](https://metorial.com) - Connect your AI agents to any MCP server with a single line of code. Deploy tools like Slack, GitHub, SAP, and hundreds more without managing infrastructure.

[Sign up for a free account](https://app.metorial.com) to get started.

## Complete API Documentation
**[API Documentation](https://metorial.com/api)** - Complete API reference and guides

## Available Providers

| Provider          | Import                      | Format                       | Models (non-exhaustive)                      |
| ----------------- | --------------------------- | ---------------------------- | -------------------------------------------- |
| OpenAI            | `MetorialOpenAI`            | OpenAI function calling      | `gpt-4.1`, `gpt-4o`, `o1`, `o3`              |
| Anthropic         | `MetorialAnthropic`         | Claude tool format           | `claude-sonnet-4-5`, `claude-opus-4`         |
| Google            | `MetorialGoogle`            | Gemini function declarations | `gemini-2.5-pro`, `gemini-2.5-flash`         |
| Mistral           | `MetorialMistral`           | Mistral function calling     | `mistral-large-latest`, `codestral-latest`   |
| DeepSeek          | `MetorialDeepSeek`          | OpenAI-compatible            | `deepseek-chat`, `deepseek-reasoner`         |
| TogetherAI        | `MetorialTogetherAI`        | OpenAI-compatible            | `Llama-4`, `Qwen-3`                          |
| XAI               | `MetorialXAI`               | OpenAI-compatible            | `grok-3`, `grok-3-mini`                      |
| LangChain         | `MetorialLangChain`         | LangChain tools              | Any model via LangChain                      |
| OpenAI-Compatible | `MetorialOpenAICompatible`  | OpenAI-compatible            | Any OpenAI-compatible API                    |

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

MIT License - see [LICENSE](LICENSE) file for details.

## Support

[Documentation](https://metorial.com/docs) · [GitHub Issues](https://github.com/metorial/metorial-python/issues) · [Email Support](mailto:support@metorial.com)
