# Metorial Python SDK

The official Python SDK for [Metorial](https://metorial.com). Give your AI agents access to tools like Slack, GitHub, SAP, and hundreds more through MCP — without managing servers, auth flows, or infrastructure.

[Sign up for a free account](https://platform.metorial.com) to get started.

## Complete API Documentation

- **[Documentation](https://metorial.com/docs)** - Documentation and guides
- **[API Reference](https://metorial.com/api)** - Complete API reference

## Installation

```bash
pip install metorial
```

## Supported LLM Integrations

This SDK formats MCP tools for each LLM provider. Pass the `provider` parameter to get tools in the right format.

| Provider      | Format                  | Client Library        | Models (non-exhaustive)                    |
| ------------- | ----------------------- | --------------------- | ------------------------------------------ |
| OpenAI        | `provider="openai"`     | `openai`              | `gpt-4.1`, `gpt-4o`, `o1`, `o3`            |
| Anthropic     | `provider="anthropic"`  | `anthropic`           | `claude-sonnet-4-5`, `claude-opus-4`       |
| Google Gemini | `provider="google"`     | `google-generativeai` | `gemini-2.5-pro`, `gemini-2.5-flash`       |
| Mistral       | `provider="mistral"`    | `mistralai`           | `mistral-large-latest`, `codestral-latest` |
| DeepSeek      | `provider="deepseek"`   | `openai` (compatible) | `deepseek-chat`, `deepseek-reasoner`       |
| Together AI   | `provider="togetherai"` | `openai` (compatible) | `Llama-4`, `Qwen-3`                        |
| xAI (Grok)    | `provider="xai"`        | `openai` (compatible) | `grok-3`, `grok-3-mini`                    |

### Framework Integrations

For popular agent frameworks, we provide helper functions that convert tools to the framework's native format:

| Framework     | Import                                                                      | Example                                         |
| ------------- | --------------------------------------------------------------------------- | ------------------------------------------------ |
| PydanticAI    | `from metorial.integrations.pydantic_ai import create_pydantic_ai_tools`    | [example](./examples/pydantic-ai/example.py)     |
| LangChain     | `from metorial.integrations.langchain import create_langchain_tools`        | [example](./examples/langchain/example.py)       |
| LangGraph     | `from metorial.integrations.langgraph import create_langgraph_tools`        | [example](./examples/langgraph/example.py)       |
| OpenAI Agents | `from metorial.integrations.openai_agents import create_openai_agent_tools` | [example](./examples/openai-agents/example.py)   |
| LlamaIndex    | `from metorial.integrations.llamaindex import create_llamaindex_tools`      | [example](./examples/llamaindex/example.py)      |
| Haystack      | `from metorial.integrations.haystack import create_haystack_tools`          | [example](./examples/haystack/example.py)        |

## Quick Start

This example uses **PydanticAI** with **Anthropic Claude** and **Metorial Search**, a built-in web search provider that requires no auth configuration. You just need two environment variables:

- `METORIAL_API_KEY` from [platform.metorial.com](https://platform.metorial.com)
- `ANTHROPIC_API_KEY` from [console.anthropic.com](https://console.anthropic.com)

```bash
pip install metorial pydantic-ai python-dotenv
```

```python
import asyncio
import os

from metorial import Metorial
from metorial.integrations.pydantic_ai import create_pydantic_ai_tools
from pydantic_ai import Agent

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])

async def main():
    deployment = metorial.provider_deployments.create(
        name="Metorial Search",
        provider_id="metorial-search",
    )

    async with metorial.provider_session(
        provider="anthropic",
        providers=[
            {"provider_deployment_id": deployment.id},
        ],
    ) as session:
        tools = create_pydantic_ai_tools(session)

        agent = Agent(
            "anthropic:claude-sonnet-4-20250514",
            system_prompt="You are a helpful research assistant.",
            tools=tools,
        )

        result = await agent.run(
            "Search the web for the latest news about AI agents and summarize the top 3 stories."
        )
        output = getattr(result, "data", None) or getattr(result, "output", str(result))
        print(output)

asyncio.run(main())
```

> See the full runnable example at [`examples/pydantic-ai/`](examples/pydantic-ai/).

## Authenticating MCP Tool Providers

The Quick Start above used Metorial Search, which requires no authentication. Most providers — Slack, GitHub, SAP, and others — require credentials. Here are the options, from simplest to most flexible.

**Key concepts:**

- **Provider** — an MCP tool integration (e.g. Slack, GitHub, Metorial Search). Browse available providers at [platform.metorial.com](https://platform.metorial.com).
- **Provider Deployment** — an instance of a provider configured for your project. You can create deployments in the dashboard or programmatically via `metorial.provider_deployments.create()`.
- **Auth Credentials** — your OAuth app registration (client ID, client secret, scopes).
- **Auth Config** — an already-authenticated connection with a token, service account, or specific user via an OAuth flow.

### Dashboard-Configured Deployments

Some providers (Exa, Tavily) use API keys configured entirely in the [dashboard](https://platform.metorial.com). Just pass the deployment ID — no auth code needed:

```python
providers=[{"provider_deployment_id": "your-exa-deployment-id"}]
```

### Pre-Created Auth Config

An auth config represents an already-authenticated connection to a provider — for example, a user who has completed the OAuth flow for Slack. Once created (via the dashboard or a setup session), reference it by ID:

```python
providers=[
    {
        "provider_deployment_id": "your-slack-deployment-id",
        "provider_auth_config_id": "your-auth-config-id",
    }
]
```

### Inline Credentials

Pass credentials directly without pre-creating them in the dashboard:

```python
providers=[
    {
        "provider_deployment_id": "your-deployment-id",
        "provider_auth_config": {
            "provider_auth_method_id": "your-auth-method-id",
            "credentials": {"access_token": "user-access-token"},
        },
    }
]
```

### OAuth Flow

For services like Slack or GitHub where each end-user authenticates individually, use setup sessions to handle the OAuth flow:

```python
import os
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])

# 1. Create a setup session for the provider
setup_session = metorial.provider_deployments.setup_sessions.create(
    provider_id="your-slack-provider-id",
    provider_auth_method_id="oauth",
    redirect_url="https://yourapp.com/oauth/callback",
)

# 2. Send the OAuth URL to your user
print(f"Authenticate here: {setup_session.url}")

# 3. Wait for the user to complete OAuth
completed = await metorial.wait_for_setup_session([setup_session])

# 4. Use the auth config in a session
async with metorial.provider_session(
    provider="anthropic",
    providers=[
        {
            "provider_deployment_id": "your-slack-deployment-id",
            "provider_auth_config_id": completed[0].auth_config.id,
        }
    ],
) as session:
    tools = session.tools
    # Use tools...
```

### Multiple Providers in One Session

Combine providers freely in a single session — each can use a different auth method:

```python
# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

providers=[
    # Metorial Search (no auth needed)
    {"provider_deployment_id": deployment.id},
    # Dashboard-configured deployment
    {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "slack-auth-config-id"},
    # Inline credentials
    {
        "provider_deployment_id": "your-github-deployment-id",
        "provider_auth_config": {
            "provider_auth_method_id": "github-auth-method-id",
            "credentials": {"access_token": "ghp_..."},
        },
    },
]
```

### Session Templates

Pre-configure provider combinations on the [dashboard](https://platform.metorial.com), then reference them by ID. This is useful when you want to manage which providers and auth configs are used without changing code:

```python
# Reference a session template by ID
async with metorial.provider_session(
    provider="anthropic",
    providers=[
        {"session_template_id": "your-template-id"},
    ],
) as session:
    tools = session.tools
    # All providers from the template are available

# You can also mix session templates with explicit provider deployments
# in the same providers list
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

providers=[
    {"session_template_id": "your-template-id"},
    {"provider_deployment_id": deployment.id},
]
```

### Enterprise: Bring Your Own (BYO) Credentials

For enterprise deployments, you have flexible options:

- **Shared deployment**: Deploy once and share with all users (works well for API key-based tools like Exa, Tavily)
- **BYO OAuth**: For services like SAP, enterprises can register their own OAuth app credentials:

```python
credentials = await metorial.provider_deployments.auth_credentials.create(
    provider_id="your-sap-provider-id",
    name="Our SAP OAuth App",
    config={
        "client_id": "your-client-id",
        "client_secret": "your-client-secret",
        "scopes": ["read", "write"],
    },
)
```

- **Dynamic deployments**: Create provider deployments programmatically via the [Provider Deployment API](https://metorial.com/api/provider-deployment).

## Session Options

- **Closing sessions**: Sessions are automatically closed when the `async with` block exits. You can also call `await session.close()` explicitly.
- **Direct sessions**: Use `metorial.provider_session(provider="anthropic", ...)` for provider-formatted tools, or access the raw MCP session directly.
- **Multiple providers**: Pass multiple entries in the `providers` list to combine tools from different MCP servers.

## Examples

Check out the `examples/` directory for complete working examples:

| Example | Framework | Description |
|---------|-----------|-------------|
| [`pydantic-ai`](examples/pydantic-ai/) | PydanticAI + Anthropic | PydanticAI agent with tool calls |
| [`langchain`](examples/langchain/) | LangChain + Anthropic | LangChain agent with react pattern |
| [`langgraph`](examples/langgraph/) | LangGraph + Anthropic | LangGraph streaming agent |
| [`openai-agents`](examples/openai-agents/) | OpenAI Agents SDK | OpenAI Agents with tool calls |
| [`llamaindex`](examples/llamaindex/) | LlamaIndex + Anthropic | LlamaIndex tool integration |
| [`haystack`](examples/haystack/) | Haystack + OpenAI | Haystack pipeline with tools |

## Provider Examples

All provider integrations follow the same `provider_session` pattern. Below are abbreviated examples — they assume `metorial` is already initialized and use Metorial Search.

<details open>
<summary><strong>OpenAI</strong></summary>

```python
import os
from openai import AsyncOpenAI
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
openai = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="openai",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    messages = [{"role": "user", "content": "Search the web for the latest news about AI agents."}]

    response = await openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=session.tools,
    )

    if response.choices[0].message.tool_calls:
        results = await session.call_tools(response.choices[0].message.tool_calls)
        # Add results to messages and continue conversation...
```

</details>

<details>
<summary><strong>Anthropic</strong></summary>

```python
import os
from anthropic import AsyncAnthropic
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
anthropic = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="anthropic",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    response = await anthropic.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        tools=session.tools,
        messages=[{"role": "user", "content": "Search the web for the latest news about AI agents."}],
    )

    if response.stop_reason == "tool_use":
        tool_calls = [b for b in response.content if b.type == "tool_use"]
        results = await session.call_tools(tool_calls)
        # Add results to messages and continue conversation...
```

</details>

<details>
<summary><strong>Google Gemini</strong></summary>

```python
import os
import google.generativeai as genai
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="google",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    model = genai.GenerativeModel("gemini-2.5-pro", tools=session.tools)
    chat = model.start_chat()
    response = chat.send_message("Search the web for the latest news about AI agents.")

    for part in response.parts:
        if fn := part.function_call:
            result = await session.call_tool(fn.name, dict(fn.args))
            # Continue conversation with result...
```

</details>

<details>
<summary><strong>Mistral</strong></summary>

```python
import os
from mistralai import Mistral
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
mistral = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="mistral",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    response = await mistral.chat.complete_async(
        model="mistral-large-latest",
        tools=session.tools,
        messages=[{"role": "user", "content": "Search the web for the latest news about AI agents."}],
    )

    if response.choices[0].message.tool_calls:
        results = await session.call_tools(response.choices[0].message.tool_calls)
        # Add results to messages and continue conversation...
```

</details>

<details>
<summary><strong>DeepSeek (OpenAI-compatible)</strong></summary>

```python
import os
from openai import AsyncOpenAI
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
deepseek = AsyncOpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/v1",
)

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="openai",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    response = await deepseek.chat.completions.create(
        model="deepseek-chat",
        tools=session.tools,
        messages=[{"role": "user", "content": "Search the web for the latest news about AI agents."}],
    )

    if response.choices[0].message.tool_calls:
        results = await session.call_tools(response.choices[0].message.tool_calls)
        # Add results to messages and continue conversation...
```

</details>

<details>
<summary><strong>Together AI (OpenAI-compatible)</strong></summary>

```python
import os
from openai import AsyncOpenAI
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
together = AsyncOpenAI(
    api_key=os.environ["TOGETHER_API_KEY"],
    base_url="https://api.together.xyz/v1",
)

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="openai",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    response = await together.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        tools=session.tools,
        messages=[{"role": "user", "content": "Search the web for the latest news about AI agents."}],
    )

    if response.choices[0].message.tool_calls:
        results = await session.call_tools(response.choices[0].message.tool_calls)
        # Add results to messages and continue conversation...
```

</details>

<details>
<summary><strong>xAI (OpenAI-compatible)</strong></summary>

```python
import os
from openai import AsyncOpenAI
from metorial import Metorial

metorial = Metorial(api_key=os.environ["METORIAL_API_KEY"])
xai = AsyncOpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1",
)

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="openai",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    response = await xai.chat.completions.create(
        model="grok-3",
        tools=session.tools,
        messages=[{"role": "user", "content": "Search the web for the latest news about AI agents."}],
    )

    if response.choices[0].message.tool_calls:
        results = await session.call_tools(response.choices[0].message.tool_calls)
        # Add results to messages and continue conversation...
```

</details>

## Framework Integration Examples

### LangChain / LangGraph

```python
from metorial.integrations.langchain import create_langchain_tools
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="anthropic",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    tools = create_langchain_tools(session)
    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    agent = create_react_agent(llm, tools)

    result = await agent.ainvoke(
        {"messages": [("user", "Search the web for the latest news about AI agents and summarize the top 3 stories.")]}
    )
    print(result["messages"][-1].content)
```

### PydanticAI

```python
from metorial.integrations.pydantic_ai import create_pydantic_ai_tools
from pydantic_ai import Agent

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

async with metorial.provider_session(
    provider="anthropic",
    providers=[{"provider_deployment_id": deployment.id}],
) as session:
    tools = create_pydantic_ai_tools(session)
    agent = Agent("anthropic:claude-sonnet-4-20250514", tools=tools)

    result = await agent.run("Search the web for the latest news about AI agents and summarize the top 3 stories.")
    print(result.output)
```

<details>
<summary><strong>Migrating from v1</strong></summary>

| v1 (Legacy)                             | v2                                                                  |
| --------------------------------------- | ------------------------------------------------------------------- |
| `server_deployments` list               | `providers` list                                                    |
| `server_deployment_id`                  | `provider_deployment_id`                                            |
| `oauth_session_id`                      | `provider_auth_config_id`                                           |
| `metorial.v1.provider_session()`        | `metorial.provider_session()`                                       |

The v1 API is still accessible via `metorial.v1.*`.

</details>

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
        providers=[{"provider_deployment_id": "your-deployment-id"}],
    ) as session:
        tools = session.tools
except AuthenticationError:
    print("Check your METORIAL_API_KEY")
except NotFoundError:
    print("Deployment not found - verify your deployment ID")
except OAuthRequiredError:
    print("This provider requires OAuth - see the OAuth section above")
except RateLimitError:
    print("Rate limited - try again later")
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Support

[Documentation](https://metorial.com/docs) · [GitHub Issues](https://github.com/metorial/metorial-python/issues) · [Email Support](mailto:support@metorial.com)
