# Metorial Python SDK

The official Python SDK for [Metorial](https://metorial.com).

## Available Providers

| Provider   | Import                | Format                       | Description                   |
| ---------- | --------------------- | ---------------------------- | ----------------------------- |
| OpenAI     | `metorial_openai`     | OpenAI function calling      | GPT-4, GPT-3.5, etc.          |
| Anthropic  | `metorial_anthropic`  | Claude tool format           | Claude 3.5, Claude 3, etc.    |
| Google     | `metorial_google`     | Gemini function declarations | Gemini Pro, Gemini Flash      |
| Mistral    | `metorial_mistral`    | Mistral function calling     | Mistral Large, Codestral      |
| DeepSeek   | `metorial_deepseek`   | OpenAI-compatible            | DeepSeek Chat, DeepSeek Coder |
| TogetherAI | `metorial_togetherai` | OpenAI-compatible            | Llama, Mixtral, etc.          |
| XAI        | `metorial_xai`        | OpenAI-compatible            | Grok models                   |
| AI SDK     | `metorial_ai_sdk`     | Framework tools              | Vercel AI SDK, etc.           |

## Installation

```bash
# Install core metorial package (includes all provider adapters)
pip install metorial

# Install with specific providers (includes provider client libraries)
pip install metorial[openai,anthropic,google,mistral,deepseek,togetherai,xai]

# Or install individual providers
pip install metorial[openai]      # Includes openai client
pip install metorial[anthropic]   # Includes anthropic client
# ... etc
```

## Quick Start
```python
import asyncio
from metorial import Metorial
from openai import AsyncOpenAI

async def main():
  metorial = Metorial(api_key="your-metorial-api-key")
  openai_client = AsyncOpenAI(api_key="your-openai-api-key")
  
  response = await metorial.run(
    "What are the latest commits in the metorial/websocket-explorer repository?",
    "your-server-deployment-id",  # can also be a list
    openai_client,
    model="gpt-4o",
    max_iterations=25
  )
  
  print("Response:", response)

asyncio.run(main())
```

That's it! `metorial.run()` automatically:
- Creates a session with your MCP server
- Formats tools for your AI provider
- Handles the execution loop
- Manages tool execution
- Returns the final response

### Synchronous Usage

For synchronous applications, use `MetorialSync`:

```python
from metorial import MetorialSync
from openai import OpenAI

metorial = MetorialSync(api_key="your-metorial-api-key")
openai_client = OpenAI(api_key="your-openai-api-key")

response = metorial.run(
  "What are the latest commits in the metorial/websocket-explorer repository?",
  "your-server-deployment-id",  # can also be a list
  openai_client,
  model="gpt-4o",
  max_iterations=25
)

print("Response:", response)
```

## Provider Examples

Metorial works with all major AI providers. Here are examples using `metorial.run()`:

### OpenAI (GPT-4, GPT-3.5)

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
openai_client = AsyncOpenAI(api_key="your-openai-api-key")

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id",
  openai_client,
  model="gpt-4o"
)
```

### Anthropic (Claude)

```python
from metorial import Metorial
import anthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic_client = anthropic.AsyncAnthropic(api_key="your-anthropic-api-key")

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id", 
  anthropic_client,
  model="claude-3-5-sonnet-20241022"
)
```

### Google (Gemini)

```python
from metorial import Metorial
import google.generativeai as genai

metorial = Metorial(api_key="your-metorial-api-key")
genai.configure(api_key="your-google-api-key")
google_client = genai.GenerativeModel('gemini-pro')

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id",
  google_client,
  model="gemini-pro"
)
```

### Mistral AI

```python
from metorial import Metorial
from mistralai import AsyncMistral

metorial = Metorial(api_key="your-metorial-api-key")
mistral_client = AsyncMistral(api_key="your-mistral-api-key")

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id",
  mistral_client,
  model="mistral-large-latest"
)
```

### DeepSeek

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
deepseek_client = AsyncOpenAI(
  api_key="your-deepseek-api-key",
  base_url="https://api.deepseek.com"
)

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id",
  deepseek_client,
  model="deepseek-chat"
)
```

### Together AI

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
together_client = AsyncOpenAI(
  api_key="your-together-api-key",
  base_url="https://api.together.xyz/v1"
)

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id",
  together_client,
  model="meta-llama/Llama-2-70b-chat-hf"
)
```

### XAI (Grok)

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
xai_client = AsyncOpenAI(
  api_key="your-xai-api-key",
  base_url="https://api.x.ai/v1"
)

response = await metorial.run(
  "What are the latest commits?",
  "your-deployment-id",
  xai_client,
  model="grok-beta"
)
```

## Advanced Usage

### Session Management

For more control over the conversation flow, use session management directly:

```python
import asyncio
from metorial import Metorial, MetorialOpenAI
from openai import AsyncOpenAI

async def main():
  metorial = Metorial(api_key="your-metorial-api-key")
  openai_client = AsyncOpenAI(api_key="your-openai-api-key")
  
  async def session_callback(session):
    messages = [{"role": "user", "content": "What are the latest commits?"}]
    
    for i in range(10):
      # Call OpenAI with Metorial tools
      response = await openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=session.tools
      )
      
      choice = response.choices[0]
      tool_calls = choice.message.tool_calls
      
      if not tool_calls:
        print(choice.message.content)
        return
      
      # Execute tools through Metorial
      tool_responses = await session.call_tools(tool_calls)
      
      # Add to conversation
      messages.append({
        "role": "assistant",
        "tool_calls": [
          {
            "id": tc.id,
            "type": tc.type,
            "function": {
              "name": tc.function.name,
              "arguments": tc.function.arguments
            }
          } for tc in tool_calls
        ]
      })
      messages.extend(tool_responses)

  await metorial.with_provider_session(
    MetorialOpenAI.chat_completions(openai_client),
    "your-deployment-id",
    session_callback
  )

asyncio.run(main())
```

### Streaming Responses

For real-time streaming responses:

```python
import asyncio
from metorial import Metorial, MetorialOpenAI
from metorial.types import StreamEventType

async def stream_chat():
  metorial = Metorial(api_key="your-metorial-api-key")
  openai_client = AsyncOpenAI(api_key="your-openai-api-key")
  
  async def stream_action(session):
    messages = [{"role": "user", "content": "What are the latest commits?"}]
    
    async for event in metorial.stream(
      openai_client, session, messages, max_iterations=10
    ):
      if event.type == StreamEventType.CONTENT:
        print(f"🤖 {event.content}", end="", flush=True)
      elif event.type == StreamEventType.TOOL_CALL:
        print(f"\n🔧 Executing {len(event.tool_calls)} tool(s)...")
      elif event.type == StreamEventType.COMPLETE:
        print(f"\n✅ Complete! Duration: {event.metadata.get('duration', 0):.2f}s")
      elif event.type == StreamEventType.ERROR:
        print(f"\n❌ Error: {event.error}")
        break
  
  await metorial.with_provider_session(
    MetorialOpenAI.chat_completions(openai_client),
    "your-deployment-id",
    stream_action
  )

asyncio.run(stream_chat())
```

### Batch Processing

Process multiple messages concurrently:

```python
import asyncio

async def batch_example():
  metorial = Metorial(api_key="your-metorial-api-key")
  openai_client = AsyncOpenAI(api_key="your-openai-api-key")
  
  messages = [
    "What are the latest commits?",
    "What are the main features?",
    "How do I get started?"
  ]
  
  results = await metorial.batch_run(
    messages,
    "your-deployment-id",
    openai_client,
    max_iterations=25
  )
  
  for i, result in enumerate(results):
    print(f"Response {i+1}: {result}")

asyncio.run(batch_example())
```

## Error Handling

```python
from metorial import MetorialAPIError

try:
  response = await metorial.run(
    "What are the latest commits?",
    "your-deployment-id",
    openai_client,
    model="gpt-4o"
  )
except MetorialAPIError as e:
  print(f"API Error: {e.message} (Status: {e.status_code})")
except Exception as e:
  print(f"Unexpected error: {e}")
```

## Examples

Check out the `examples/` directory for more comprehensive examples.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](https://docs.metorial.com)
- 🐛 [GitHub Issues](https://github.com/metorial/metorial-python/issues)
- 📧 [Email Support](mailto:support@metorial.com)
