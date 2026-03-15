# Metorial Python Examples

All examples use **Metorial Search** by default — a built-in web search provider that requires no setup. Just set your env vars and run.

See the [main README](../README.md) for docs on authentication, OAuth, session templates, and provider configuration.

## Running an Example

```bash
cd examples/pydantic-ai
cp ../.env.example .env  # add your API keys
pip install metorial pydantic-ai python-dotenv
python example.py
```

## Examples

| Example | Framework | Description |
|---------|-----------|-------------|
| [`pydantic-ai`](pydantic-ai/) | PydanticAI + Anthropic | PydanticAI agent with tool calls |
| [`langchain`](langchain/) | LangChain + Anthropic | LangChain agent with react pattern |
| [`langgraph`](langgraph/) | LangGraph + Anthropic | LangGraph streaming agent |
| [`openai-agents`](openai-agents/) | OpenAI Agents SDK | OpenAI Agents with tool calls |
| [`llamaindex`](llamaindex/) | LlamaIndex + Anthropic | LlamaIndex tool integration |
| [`haystack`](haystack/) | Haystack + OpenAI | Haystack pipeline with tools |

Legacy v1 examples are in [`legacy/`](legacy/).
