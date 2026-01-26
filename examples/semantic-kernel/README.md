# Metorial + Microsoft Semantic Kernel

Build enterprise AI orchestration with MCP tools.

## Installation

```bash
pip install metorial semantic-kernel python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.semantic_kernel import register_metorial_plugin
import semantic_kernel as sk

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    kernel = sk.Kernel()
    register_metorial_plugin(kernel, session)

    # Use tools with Semantic Kernel
```

## Examples

- [example.py](example.py) - Python script with Semantic Kernel orchestration
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The `register_metorial_plugin()` function registers MCP tools as a Semantic Kernel plugin, making them available for:

- Function calling with any LLM
- Planner integration
- Enterprise AI workflows

## Links

- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Metorial Dashboard](https://app.metorial.com)
