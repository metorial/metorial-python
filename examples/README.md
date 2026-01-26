# Metorial Python Examples

Use Metorial tools with your favorite Python agent framework.

## Setup

```bash
cp .env.example .env
# Edit .env with your API keys and deployment IDs
```

## Supported Frameworks

| Framework | Directory | Integration Function |
|-----------|-----------|---------------------|
| [LangChain](langchain/) | `langchain/` | `create_langchain_tools()` |
| [LangGraph](langgraph/) | `langgraph/` | `create_langgraph_tools()` |
| [OpenAI Agents](openai-agents/) | `openai-agents/` | `create_openai_agent_tools()` |
| [PydanticAI](pydantic-ai/) | `pydantic-ai/` | `create_pydantic_ai_tools()` |
| [LlamaIndex](llamaindex/) | `llamaindex/` | `create_llamaindex_tools()` |
| [Autogen](autogen/) | `autogen/` | `create_autogen_tools()` |
| [smolagents](smolagents/) | `smolagents/` | `create_smolagents_tools()` |
| [Semantic Kernel](semantic-kernel/) | `semantic-kernel/` | `register_metorial_plugin()` |
| [Haystack](haystack/) | `haystack/` | `create_haystack_tools()` |

Each directory contains:
- `README.md` - Framework-specific documentation
- `example.py` - Python script
- `example.ipynb` - Jupyter notebook

## Quick Start

All integrations follow the same pattern using the `provider_session` context manager:

```python
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

async with metorial.provider_session(
    provider="anthropic",
    server_deployments=[os.getenv("DEPLOYMENT_ID")],
) as session:
    tools = create_langchain_tools(session)
    # Use tools with your framework
```

## OAuth Flow

For servers requiring OAuth (e.g., Google Calendar, Slack):

```python
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# 1. Create OAuth session (one-time per user)
oauth = metorial.oauth.sessions.create(
    server_deployment_id=deployment_id,
    # redirect_uri="https://your-app.com/oauth/callback",  # Optional
)
print(f"Auth URL: {oauth.url}")

# 2. Wait for user authorization
await metorial.oauth.wait_for_completion([oauth])

# 3. Use with session
async with metorial.provider_session(
    provider="anthropic",
    server_deployments=[{
        "server_deployment_id": deployment_id,
        "oauth_session_id": oauth.id,
    }],
) as session:
    tools = create_langchain_tools(session)
```

## Getting Deployment IDs

Find deployment IDs in your [Metorial Dashboard](https://app.metorial.com).

Format: `svd_xxxxx`
