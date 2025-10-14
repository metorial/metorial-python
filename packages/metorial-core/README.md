# Metorial Python SDK

The official Python SDK for [Metorial](https://metorial.com).

## Available Providers

| Provider   | Format                       | Description                   |
| ---------- | ---------------------------- | ----------------------------- |
| OpenAI     | OpenAI function calling      | GPT-4, GPT-3.5, etc.          |
| Anthropic  | Claude tool format           | Claude 3.5, Claude 3, etc.    |
| Google     | Gemini function declarations | Gemini Pro, Gemini Flash      |
| Mistral    | Mistral function calling     | Mistral Large, Codestral      |
| DeepSeek   | OpenAI-compatible            | DeepSeek Chat, DeepSeek Coder |
| TogetherAI | OpenAI-compatible            | Llama, Mixtral, etc.          |
| XAI        | OpenAI-compatible            | Grok models                   |
| AI SDK     | Framework tools              | Vercel AI SDK, etc.           |

## Installation

```bash
# Install core metorial package (includes all provider adapters)
pip install metorial

# Install with specific providers (includes provider client libraries)
pip install metorial[openai,anthropic,google,mistral,deepseek,togetherai,xai]
```

## Quick Start

### Simple Usage
```python
import asyncio
from metorial import Metorial
from openai import AsyncOpenAI

async def main():
  metorial = Metorial(api_key="your-metorial-api-key")
  openai = AsyncOpenAI(api_key="your-openai-api-key")
  
  response = await metorial.run(
    message="Search Hackernews for the latest AI discussions.",
    server_deployments=["hacker-news-server-deployment"],
    client=openai,
    model="gpt-4o",
    max_steps=25    # optional
  )
  
  print("Response:", response.text)

asyncio.run(main())
```

> **💡 Tip for Jupyter/Colab Users**: If you're running in a Jupyter notebook or Google Colab, you can skip the `async def main():` wrapper and `asyncio.run()` and just use `await` directly at the top level.

### OAuth + Multiple Deployments
For integrations requiring OAuth authentication (like Google Calendar) and multiple server deployments:

```python
import asyncio
import os
from metorial import Metorial
from anthropic import AsyncAnthropic

async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))
  anthropic = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

  # Create OAuth session for authenticated services
  google_cal_deployment_id = os.getenv("GOOGLE_CALENDAR_DEPLOYMENT_ID")
  
  print("🔗 Creating OAuth session...")
  oauth_session = metorial.oauth.sessions.create(
    server_deployment_id=google_cal_deployment_id
  )

  print("OAuth URLs for user authentication:")
  print(f"   Google Calendar: {oauth_session.url}")

  print("\n⏳ Waiting for OAuth completion...")
  await metorial.oauth.wait_for_completion([oauth_session])
  print("✅ OAuth session completed!")

  # Use multiple server deployments with mixed auth
  hackernews_deployment_id = os.getenv("HACKERNEWS_DEPLOYMENT_ID")
  
  result = await metorial.run(
    message="""Search Hackernews for the latest AI discussions using the available tools. 
    Then create a calendar event using Google Calendar tools with my@email.address for tomorrow at 2pm to discuss AI trends.""",
    server_deployments=[
      { "serverDeploymentId": google_cal_deployment_id, "oauthSessionId": oauth_session.id },
      { "serverDeploymentId": hackernews_deployment_id },
    ],
    client=anthropic,
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    max_steps=25,
  )
  print(result.text)

asyncio.run(main())
```

That's it! `metorial.run()` automatically:
- Creates a session with your MCP server
- Formats tools for your AI provider
- Handles the execution loop
- Manages tool execution
- Returns the final response

### Advanced Usage with Provider Sessions

For more control over the conversation flow, you can use `with_provider_session`:

```python
import asyncio
from metorial import Metorial, MetorialOpenAI
from openai import AsyncOpenAI

async def main():
  metorial = Metorial(api_key="your-metorial-api-key")
  openai = AsyncOpenAI(api_key="your-openai-api-key")

  messages = [
    {"role": "user", "content": "What are the top hackernews posts?"}
  ]

  async def session_action(session):
    for i in range(10):
      response = await openai.chat.completions.create(
        messages=messages,
        model="gpt-4o",
        tools=session["tools"]
      )

      choice = response.choices[0]
      tool_calls = choice.message.tool_calls

      if not tool_calls:
        print(choice.message.content)
        return

      # Execute tools through Metorial
      tool_responses = await session["callTools"](tool_calls)

      # Add to conversation
      messages.append({
        "role": "assistant", 
        "tool_calls": choice.message.tool_calls
      })
      messages.extend(tool_responses)

  await metorial.with_provider_session(
    MetorialOpenAI.chat_completions,
    [{"serverDeploymentId": "your-deployment-id"}],
    session_action
  )

asyncio.run(main())
```

This approach gives you full control over the conversation loop while still benefiting from Metorial's tool management.

## Provider Examples

Metorial works with all major AI providers. Here are examples using `metorial.run()`:

### Example OpenAI (GPT-4, GPT-3.5)

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
openai = AsyncOpenAI(api_key="your-openai-api-key")

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=openai,
  model="gpt-4o"
)
```

### Anthropic (Claude)

```python
from metorial import Metorial
import anthropic

metorial = Metorial(api_key="your-metorial-api-key")
anthropic = anthropic.AsyncAnthropic(api_key="your-anthropic-api-key")

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=anthropic,
  model="claude-3-5-sonnet-20241022"
)
```

### Google (Gemini)

```python
from metorial import Metorial
import google.generativeai as genai

metorial = Metorial(api_key="your-metorial-api-key")
genai.configure(api_key="your-google-api-key")
google = genai.GenerativeModel('gemini-pro')

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=google,
  model="gemini-pro"
)
```

### Mistral AI

```python
from metorial import Metorial
from mistralai import AsyncMistral

metorial = Metorial(api_key="your-metorial-api-key")
mistral = AsyncMistral(api_key="your-mistral-api-key")

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=mistral,
  model="mistral-large-latest"
)
```

### DeepSeek

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
deepseek = AsyncOpenAI(
  api_key="your-deepseek-api-key",
  base_url="https://api.deepseek.com"
)

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=deepseek,
  model="deepseek-chat"
)
```

### Together AI

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
together = AsyncOpenAI(
  api_key="your-together-api-key",
  base_url="https://api.together.xyz/v1"
)

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=together,
  model="meta-llama/Llama-2-70b-chat-hf"
)
```

### XAI (Grok)

```python
from metorial import Metorial
from openai import AsyncOpenAI

metorial = Metorial(api_key="your-metorial-api-key")
xai = AsyncOpenAI(
  api_key="your-xai-api-key",
  base_url="https://api.x.ai/v1"
)

response = await metorial.run(
  message="What are the latest commits?",
  server_deployments=["your-deployment-id"],
  client=xai,
  model="grok-beta"
)
```

## Error Handling

```python
from metorial import MetorialAPIError

try:
  response = await metorial.run(
    message="What are the latest commits?",
    server_deployments=["your-deployment-id"],
    client=openai,
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
