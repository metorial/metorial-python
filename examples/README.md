# Metorial Python Examples

Use Metorial tools with your favorite Python agent framework.

## v1 vs v2

Examples are organized into two versions:

- **`v2/`** — Magnetar API (current, recommended). Uses `providers=` for session creation.
- **`v1/`** — Pulsar API (legacy). Uses `server_deployments=` for session creation.

## Setup

```bash
cp .env.example .env
# Edit .env with your API keys and deployment IDs
```

## Supported Frameworks

| Framework | v2 Example | v1 Example | Integration Function |
|-----------|-----------|-----------|---------------------|
| [LangChain](v2/langchain/) | `v2/langchain/` | `v1/langchain/` | `create_langchain_tools()` |
| [LangGraph](v2/langgraph/) | `v2/langgraph/` | `v1/langgraph/` | `create_langgraph_tools()` |
| [OpenAI Agents](v2/openai-agents/) | `v2/openai-agents/` | `v1/openai-agents/` | `create_openai_agent_tools()` |
| [PydanticAI](v2/pydantic-ai/) | `v2/pydantic-ai/` | `v1/pydantic-ai/` | `create_pydantic_ai_tools()` |
| [LlamaIndex](v2/llamaindex/) | `v2/llamaindex/` | `v1/llamaindex/` | `create_llamaindex_tools()` |
| [Autogen](v2/autogen/) | `v2/autogen/` | `v1/autogen/` | `create_autogen_tools()` |
| [smolagents](v2/smolagents/) | `v2/smolagents/` | `v1/smolagents/` | `create_smolagents_tools()` |
| [Semantic Kernel](v2/semantic-kernel/) | `v2/semantic-kernel/` | `v1/semantic-kernel/` | `register_metorial_plugin()` |
| [Haystack](v2/haystack/) | `v2/haystack/` | `v1/haystack/` | `create_haystack_tools()` |

## Quick Start (v2 — Magnetar)

```python
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
) as session:
    tools = create_langchain_tools(session)
    # Use tools with your framework
```

## Quick Start (v1 — Pulsar, legacy)

```python
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

async with metorial.v1.provider_session(
    provider="anthropic",
    server_deployments=[os.getenv("EXA_DEPLOYMENT_ID")],
) as session:
    tools = create_langchain_tools(session)
    # Use tools with your framework
```

## Getting Deployment IDs

Find deployment IDs in your [Metorial Dashboard](https://app.metorial.com).
