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

## Setting Up Server Deployments

Server deployments are configured at [app.metorial.com](https://app.metorial.com). When you create a session from a deployment, we spin up an isolated serverless instance isolated to that user.

### Types of Deployments

1. **Standard Deployments** (e.g., Exa or Tavily for web search)
   - API key-based authentication
   - Can be shared across all users
   - No user authorization required

2. **OAuth-Enabled Deployments** (e.g., Slack, GitHub, SAP)
   - Requires user authorization
   - Each user completes OAuth once
   - Session is isolated per user

### Enterprise: Bring Your Own (BYO) Credentials

For enterprise deployments, you have flexible options:

- **Shared deployment**: Deploy once and share with all users (works well for API key-based servers like Exa, Tavily)
- **BYO OAuth**: For services like SAP, enterprises can bring their own OAuth app credentials
- **Dynamic deployments**: Create server deployments programmatically via the [Server Deployment API](http://metorial.com/api/server-deployment)

## OAuth Integration

When working with services that require user authentication (like Google Calendar, Slack, etc.), Metorial provides OAuth session management to handle the authentication flow:

```python
import asyncio
from metorial import Metorial, MetorialAnthropic
from anthropic import AsyncAnthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic = AsyncAnthropic(api_key="your-anthropic-api-key")

async def main():
    # Create OAuth sessions for services that require user authentication
    # this just needs to be done once per user
    google_cal_oauth_session = metorial.oauth.sessions.create(
      server_deployment_id="your-google-calendar-server-deployment-id"
      # Optional: callback_uri="https://your-app.com/oauth/callback"
    )
    
    slack_oauth_session = metorial.oauth.sessions.create(
      server_deployment_id="your-slack-server-deployment-id"
      # Optional: callback_uri="https://your-app.com/oauth/callback"
    )

    # Give user OAuth URLs for authentication
    print("OAuth URLs for user authentication:")
    print(f"   Google Calendar: {google_cal_oauth_session.url}")
    print(f"   Slack: {slack_oauth_session.url}")

    # Wait for user to complete OAuth flow
    await metorial.oauth.wait_for_completion([google_cal_oauth_session, slack_oauth_session])

    print("OAuth sessions completed!")

    # Now use the authenticated sessions
    async def session_handler(session):
        tools = session["tools"]
        call_tools = session["callTools"]
        close_session = session["closeSession"]

        messages = [
            {
                "role": "user",
                "content": """Look in Slack for mentions of potential partners. Use Exa to research their background, 
                company, and email. Schedule a 30-minute intro call with them for an open slot on Dec 13th, 2025 
                SF time and send me the calendar link."""
            }
        ]

        # Dedupe tools by name
        unique_tools = list({t["name"]: t for t in tools}.values())

        for i in range(10):
            response = await anthropic.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                messages=messages,
                tools=unique_tools
            )

            tool_calls = [block for block in response.content if block.type == "tool_use"]

            if not tool_calls:
                final_text = "".join(
                    block.text for block in response.content if block.type == "text"
                )
                print(final_text)
                await close_session()
                return

            tool_responses = await call_tools(tool_calls)
            messages.append({"role": "assistant", "content": response.content})
            messages.append(tool_responses)

        await close_session()

    await metorial.with_provider_session(
        MetorialAnthropic,
        {
            "serverDeployments": [
                {
                    "serverDeploymentId": "your-google-calendar-server-deployment-id",
                    "oauthSessionId": google_cal_oauth_session.id
                },
                {
                    "serverDeploymentId": "your-slack-server-deployment-id",
                    "oauthSessionId": slack_oauth_session.id
                },
                {
                    "serverDeploymentId": "your-exa-server-deployment-id"  # No OAuth needed for Exa
                }
            ],
            # "streaming": True,  # Optional: enable for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

### OAuth Flow Explained

1. **Create OAuth Sessions**: Call `metorial.oauth.sessions.create()` for each service requiring user authentication (only once per user)
2. **Send URLs**: Show the OAuth URLs to users so they can authenticate in their browser
3. **Wait for Completion**: Use `metorial.oauth.wait_for_completion()` to wait for users to complete the OAuth flow
4. **Use Authenticated Sessions**: Pass the `oauthSessionId` when configuring `serverDeployments`

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

Always close your session when done to free up resources. The `closeSession` callback is provided in the session handler:

```python
async def session_handler(session):
    tools = session["tools"]
    close_session = session["closeSession"]

    # Use tools...

    # When finished, close the session
    await close_session()
```

## Examples

Check out the `examples/` directory for more comprehensive examples:

- [`examples/python-anthropic/`](examples/python-anthropic/) - Anthropic integration (recommended)
- [`examples/python-openai/`](examples/python-openai/) - OpenAI integration
- [`examples/python-google/`](examples/python-google/) - Google Gemini integration
- [`examples/python-deepseek/`](examples/python-deepseek/) - DeepSeek integration

## Provider Examples

### Anthropic (Claude)

```python
import asyncio
from metorial import Metorial, MetorialAnthropic
from anthropic import AsyncAnthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic = AsyncAnthropic(api_key="your-anthropic-api-key")

async def main():
    async def session_handler(session):
        tools = session["tools"]
        call_tools = session["callTools"]
        close_session = session["closeSession"]

        messages = [
            {"role": "user", "content": "Help me with this GitHub task: ..."}
        ]

        # Dedupe tools by name
        unique_tools = list({t["name"]: t for t in tools}.values())

        response = await anthropic.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=messages,
            tools=unique_tools
        )

        # Handle tool calls
        tool_calls = [block for block in response.content if block.type == "tool_use"]

        if tool_calls:
            tool_responses = await call_tools(tool_calls)
            messages.append({"role": "assistant", "content": response.content})
            messages.append(tool_responses)

        await close_session()  # Close session when done

    await metorial.with_provider_session(
        MetorialAnthropic,
        {
            "serverDeployments": ["your-server-deployment-id"],
            # "streaming": True,  # Optional: enable for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

### Google (Gemini)

```python
import asyncio
from metorial import Metorial, MetorialGoogle
import google.generativeai as genai

metorial = Metorial(api_key="your-metorial-api-key")
genai.configure(api_key="your-google-api-key")

async def main():
    async def session_handler(session):
        tools = session["tools"]
        close_session = session["closeSession"]

        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            tools=tools
        )

        response = await model.generate_content_async("What can you help me with?")

        # Handle function calls if present
        # ... tool call handling logic

        await close_session()  # Close session when done

    await metorial.with_provider_session(
        MetorialGoogle,
        {
            "serverDeployments": ["your-server-deployment-id"],
            # "streaming": True,  # Optional: enable for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

### OpenAI-Compatible (DeepSeek, TogetherAI, XAI)

```python
import asyncio
from metorial import Metorial, MetorialDeepSeek
from openai import AsyncOpenAI

# Works with any OpenAI-compatible API
deepseek_client = AsyncOpenAI(
    api_key="your-deepseek-key",
    base_url="https://api.deepseek.com"
)

metorial = Metorial(api_key="your-metorial-api-key")

async def main():
    async def session_handler(session):
        tools = session["tools"]
        close_session = session["closeSession"]

        response = await deepseek_client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": "Help me code"}],
            tools=tools
        )
        # ... handle response

        await close_session()  # Close session when done

    await metorial.with_provider_session(
        MetorialDeepSeek.chat_completions,
        {
            "serverDeployments": ["your-server-deployment-id"],
            # "streaming": True,  # Optional: enable for streaming with tool calls
        },
        session_handler
    )

asyncio.run(main())
```

## Core API

### Metorial Class

```python
from metorial import Metorial

metorial = Metorial(api_key="your-api-key")
```

### Session Management

```python
# Provider session (recommended)
await metorial.with_provider_session(
    provider.chat_completions,
    {
        "serverDeployments": ["deployment-id"],
        # "streaming": True,  # Optional: enable for streaming with tool calls
    },
    session_handler
)

# Direct session management
await metorial.with_session(["deployment-id"], session_handler)
```

### Session Object

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
