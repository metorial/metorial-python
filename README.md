# Metorial Python SDK

Connect AI agents to MCP servers. Metorial provides the tools—use them with any AI provider or framework.

## Installation

```bash
pip install metorial
```

## Quick Start

Get tools and call them directly—no AI client needed:

```python
import asyncio
from metorial import Metorial

metorial = Metorial(api_key="your-api-key")

async def main():
    async with metorial.provider_session(
        provider="openai",  # Tool format: "openai", "anthropic", "google", etc.
        server_deployments=["your-deployment-id"],
    ) as session:
        # See your available tools
        for tool in session.tools:
            print(f"- {tool['function']['name']}")

        # Call a tool directly
        result = await session.call_tool("search", {"query": "python news"})
        print(result)

asyncio.run(main())
```

## Works With Any AI Provider

Metorial provides tools formatted for your provider. Use them with any client library:

```python
# Get tools formatted for your provider
tools = session.tools

# Execute tool calls from any provider's response
results = await session.call_tools(tool_calls)
```

| Provider | Format | Client Library |
|----------|--------|----------------|
| OpenAI | `provider="openai"` | `openai` |
| Anthropic | `provider="anthropic"` | `anthropic` |
| Google Gemini | `provider="google"` | `google-generativeai` |
| Mistral | `provider="mistral"` | `mistralai` |
| DeepSeek | `provider="deepseek"` | `openai` (compatible) |
| Together AI | `provider="togetherai"` | `openai` (compatible) |
| xAI (Grok) | `provider="xai"` | `openai` (compatible) |

All providers use OpenAI-style tool format. The `provider` parameter customizes tool call/result handling for each provider's specific requirements.

## Provider Examples

<details open>
<summary><strong>OpenAI</strong></summary>

```python
import asyncio
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial()
openai = AsyncOpenAI()

async def main():
    async with metorial.provider_session(
        provider="openai",
        server_deployments=["your-deployment-id"],
    ) as session:
        messages = [{"role": "user", "content": "What's trending on Hacker News?"}]

        response = await openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=session.tools,
        )

        if response.choices[0].message.tool_calls:
            results = await session.call_tools(response.choices[0].message.tool_calls)
            # Add results to messages and continue conversation...

asyncio.run(main())
```

</details>

<details>
<summary><strong>Anthropic</strong></summary>

```python
import asyncio
from metorial import Metorial
from anthropic import AsyncAnthropic

metorial = Metorial()
anthropic = AsyncAnthropic()

async def main():
    async with metorial.provider_session(
        provider="anthropic",
        server_deployments=["your-deployment-id"],
    ) as session:
        response = await anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            tools=session.tools,
            messages=[{"role": "user", "content": "What's trending on Hacker News?"}],
        )

        if response.stop_reason == "tool_use":
            tool_calls = [b for b in response.content if b.type == "tool_use"]
            results = await session.call_tools(tool_calls)
            # Add results to messages and continue conversation...

asyncio.run(main())
```

</details>

<details>
<summary><strong>Google Gemini</strong></summary>

```python
import asyncio
import google.generativeai as genai
from metorial import Metorial

metorial = Metorial()
genai.configure(api_key="your-google-api-key")

async def main():
    async with metorial.provider_session(
        provider="google",
        server_deployments=["your-deployment-id"],
    ) as session:
        model = genai.GenerativeModel("gemini-1.5-pro", tools=session.tools)
        chat = model.start_chat()
        response = chat.send_message("What's trending on Hacker News?")

        for part in response.parts:
            if fn := part.function_call:
                result = await session.call_tool(fn.name, dict(fn.args))
                # Continue conversation with result...

asyncio.run(main())
```

</details>

<details>
<summary><strong>Mistral</strong></summary>

```python
import asyncio
from metorial import Metorial
from mistralai import Mistral

metorial = Metorial()
mistral = Mistral(api_key="your-mistral-api-key")

async def main():
    async with metorial.provider_session(
        provider="mistral",
        server_deployments=["your-deployment-id"],
    ) as session:
        response = await mistral.chat.complete_async(
            model="mistral-large-latest",
            tools=session.tools,
            messages=[{"role": "user", "content": "What's trending on Hacker News?"}],
        )

        if response.choices[0].message.tool_calls:
            results = await session.call_tools(response.choices[0].message.tool_calls)
            # Add results to messages and continue conversation...

asyncio.run(main())
```

</details>

<details>
<summary><strong>DeepSeek (OpenAI-compatible)</strong></summary>

```python
import asyncio
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial()
deepseek = AsyncOpenAI(
    api_key="your-deepseek-api-key",
    base_url="https://api.deepseek.com/v1",
)

async def main():
    async with metorial.provider_session(
        provider="openai",
        server_deployments=["your-deployment-id"],
    ) as session:
        response = await deepseek.chat.completions.create(
            model="deepseek-chat",
            tools=session.tools,
            messages=[{"role": "user", "content": "What's trending on Hacker News?"}],
        )

        if response.choices[0].message.tool_calls:
            results = await session.call_tools(response.choices[0].message.tool_calls)
            # Add results to messages and continue conversation...

asyncio.run(main())
```

</details>

<details>
<summary><strong>Together AI (OpenAI-compatible)</strong></summary>

```python
import asyncio
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial()
together = AsyncOpenAI(
    api_key="your-together-api-key",
    base_url="https://api.together.xyz/v1",
)

async def main():
    async with metorial.provider_session(
        provider="openai",
        server_deployments=["your-deployment-id"],
    ) as session:
        response = await together.chat.completions.create(
            model="meta-llama/Llama-3-70b-chat-hf",
            tools=session.tools,
            messages=[{"role": "user", "content": "What's trending on Hacker News?"}],
        )

        if response.choices[0].message.tool_calls:
            results = await session.call_tools(response.choices[0].message.tool_calls)
            # Add results to messages and continue conversation...

asyncio.run(main())
```

</details>

<details>
<summary><strong>xAI (OpenAI-compatible)</strong></summary>

```python
import asyncio
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial()
xai = AsyncOpenAI(
    api_key="your-xai-api-key",
    base_url="https://api.x.ai/v1",
)

async def main():
    async with metorial.provider_session(
        provider="openai",
        server_deployments=["your-deployment-id"],
    ) as session:
        response = await xai.chat.completions.create(
            model="grok-beta",
            tools=session.tools,
            messages=[{"role": "user", "content": "What's trending on Hacker News?"}],
        )

        if response.choices[0].message.tool_calls:
            results = await session.call_tools(response.choices[0].message.tool_calls)
            # Add results to messages and continue conversation...

asyncio.run(main())
```

</details>

## Framework Integrations

For popular frameworks, we provide helper functions that convert tools to the framework's native format:

| Framework | Import | Example |
|-----------|--------|---------|
| LangChain | `from metorial.integrations.langchain import create_langchain_tools` | [example](./examples/langchain/example.py) |
| LangGraph | `from metorial.integrations.langgraph import create_langgraph_tools` | [example](./examples/langgraph/example.py) |
| LlamaIndex | `from metorial.integrations.llamaindex import create_llamaindex_tools` | [example](./examples/llamaindex/example.py) |
| OpenAI Agents | `from metorial.integrations.openai_agents import create_openai_agent_tools` | [example](./examples/openai-agents/example.py) |
| PydanticAI | `from metorial.integrations.pydantic_ai import create_pydantic_ai_tools` | [example](./examples/pydantic-ai/example.py) |
| Haystack | `from metorial.integrations.haystack import create_haystack_tools` | [example](./examples/haystack/example.py) |
| smolagents | `from metorial.integrations.smolagents import create_smolagents_tools` | [example](./examples/smolagents/example.py) |
| Semantic Kernel | `from metorial.integrations.semantic_kernel import create_semantic_kernel_tools` | [example](./examples/semantic-kernel/example.py) |
| AutoGen | `from metorial.integrations.autogen import create_autogen_tools` | [example](./examples/autogen/example.py) |

**Example with LangChain:**

```python
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

metorial = Metorial()

async with metorial.provider_session(
    provider="anthropic",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_langchain_tools(session)
    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    agent = create_react_agent(llm, tools)

    result = await agent.ainvoke({
        "messages": [("user", "What's the latest news?")]
    })
    print(result["messages"][-1].content)
```

## Multiple Server Deployments

Connect to multiple MCP servers in a single session:

```python
async with metorial.provider_session(
    provider="openai",
    server_deployments=[
        "exa-search-deployment",
        "github-deployment",
        "slack-deployment",
    ],
) as session:
    # Tools from all deployments are combined
    tools = session.tools  # Includes tools from all 3 servers
```

## OAuth Authentication

Some MCP servers require user authentication (Gmail, Slack, GitHub, etc.). Metorial handles the OAuth flow:

```python
from metorial import Metorial

metorial = Metorial()

# 1. Create OAuth session
oauth = metorial.oauth.sessions.create(
    server_deployment_id="gmail-deployment"
)

# 2. User authorizes (redirect them to this URL)
print(f"Please authorize: {oauth.url}")

# 3. Wait for completion
await metorial.oauth.wait_for_completion([oauth])

# 4. Use authenticated session
async with metorial.provider_session(
    provider="openai",
    server_deployments=[
        {"server_deployment_id": "gmail-deployment", "oauth_session_id": oauth.id}
    ],
) as session:
    # Now has access to user's Gmail
    tools = session.tools
```

### Multiple OAuth Sessions

You can authenticate with multiple services and combine them with non-OAuth deployments:

```python
# Create OAuth for multiple services
gmail_oauth = metorial.oauth.sessions.create(server_deployment_id="gmail-deployment")
slack_oauth = metorial.oauth.sessions.create(server_deployment_id="slack-deployment")

# Wait for all authorizations
await metorial.oauth.wait_for_completion([gmail_oauth, slack_oauth])

# Use everything in one session
async with metorial.provider_session(
    provider="openai",
    server_deployments=[
        {"server_deployment_id": "gmail-deployment", "oauth_session_id": gmail_oauth.id},
        {"server_deployment_id": "slack-deployment", "oauth_session_id": slack_oauth.id},
        "exa-search-deployment",  # Non-OAuth deployment (just string)
    ],
) as session:
    # Tools from all services available
    tools = session.tools
```

## Error Handling

```python
from metorial import (
    Metorial,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    OAuthRequiredError,
)

metorial = Metorial()

try:
    async with metorial.provider_session(
        provider="openai",
        server_deployments=["your-deployment-id"],
    ) as session:
        tools = session.tools
except AuthenticationError:
    # Invalid API key
    print("Check your METORIAL_API_KEY")
except NotFoundError:
    # Deployment doesn't exist or not accessible
    print("Deployment not found - verify your deployment ID")
except OAuthRequiredError:
    # Server requires OAuth but no session was provided
    print("This server requires OAuth - see the OAuth section above")
except RateLimitError:
    # Too many requests
    print("Rate limited - try again later")
```

## Documentation

- [Full Documentation](https://metorial.com/docs)
- [API Reference](https://metorial.com/api)
- [Examples](./examples)
- [Sign up for free](https://app.metorial.com)

## License

MIT License - see [LICENSE](LICENSE) for details.
