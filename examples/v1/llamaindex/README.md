# Metorial + LlamaIndex

Build LlamaIndex agents with MCP tools.

## Installation

```bash
pip install metorial llama-index llama-index-llms-openai python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.llamaindex import create_llamaindex_tools
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_llamaindex_tools(session)

    llm = OpenAI(model="gpt-4o")
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)

    response = agent.chat("Your query here")
```

## Examples

- [example.py](example.py) - Python script with ReAct agent
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The `create_llamaindex_tools()` function converts MCP tools into LlamaIndex `FunctionTool` objects compatible with:

- `ReActAgent`
- `OpenAIAgent`
- Any LlamaIndex agent implementation

## Links

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Metorial Dashboard](https://app.metorial.com)
