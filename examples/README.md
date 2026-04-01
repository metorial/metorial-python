# Metorial Python Examples

All examples use **Metorial Search** by default — a built-in web search provider that requires no setup. Each example folder includes a `.env.example` and `requirements.txt`, so you can install and run it in place.

See the [main README](../README.md) for docs on authentication, OAuth, session templates, and provider configuration.

## Running an Example

```bash
cd examples/pydantic-ai
cp .env.example .env
pip install -r requirements.txt
python example.py
```

## Examples

| Example | Framework | Description |
|---------|-----------|-------------|
| [`autogen`](autogen/) | AutoGen + OpenAI | AutoGen assistant with tool calls |
| [`crewai`](crewai/) | CrewAI + OpenAI | CrewAI agent with Metorial tools |
| [`google-adk`](google-adk/) | Google ADK + Gemini | Google ADK agent with async tool calls |
| [`llamaindex`](llamaindex/) | LlamaIndex + OpenAI | FunctionAgent with tool calls |
| [`pydantic-ai`](pydantic-ai/) | PydanticAI + Anthropic | PydanticAI agent with tool calls |
| [`langchain`](langchain/) | LangChain + Anthropic | LangChain agent with react pattern |
| [`langgraph`](langgraph/) | LangGraph + Anthropic | LangGraph streaming agent |
| [`openai-agents`](openai-agents/) | OpenAI Agents SDK | OpenAI Agents with tool calls |
| [`haystack`](haystack/) | Haystack + OpenAI | Haystack pipeline with tools |
