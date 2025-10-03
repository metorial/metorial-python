"""
Metorial Sync Client
"""

import asyncio
import time
from typing import Dict, Any, List, Optional, Callable, Union
from ...base import MetorialBase
from ...session import MetorialSession
from ...adapters import ProviderAdapter, ChatMessage, create_provider_adapter
from metorial_exceptions import MetorialAPIError
from ..metrics import ChatMetrics


class MetorialSync(MetorialBase):
  """Synchronous Metorial client with enhanced error handling"""

  def create_mcp_connection(self, init: Dict[str, Any]):
    """Synchronous wrapper for create_mcp_connection with retry logic"""
    return asyncio.run(self._create_mcp_connection_async(init))

  async def _create_mcp_connection_async(self, init: Dict[str, Any]):
    for attempt in range(self._config["maxRetries"]):
      try:
        session = self.create_mcp_session(init)  # type: ignore[arg-type]
        deployments = await session.get_server_deployments()
        return await session.get_client({"deploymentId": deployments[0]["id"]})
      except Exception as e:
        if attempt == self._config["maxRetries"] - 1:
          raise MetorialAPIError(
            f"Failed to create MCP connection after {self._config['maxRetries']} attempts: {e}"
          )
        await asyncio.sleep(2**attempt)

  def with_session(
    self,
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable[[MetorialSession], Any],
  ):
    """Synchronous wrapper for with_session"""

    async def async_action_wrapper(session):
      if asyncio.iscoroutinefunction(action):
        return await action(session)
      else:
        return action(session)

    return asyncio.run(self._with_session_async(init, async_action_wrapper))

  async def _with_session_async(
    self,
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable[[MetorialSession], Any],
  ):
    session = None
    try:
      # Convert string or list of strings to proper init format
      if isinstance(init, str):
        init = {"serverDeployments": [init]}
      elif isinstance(init, list):
        init = {"serverDeployments": init}

      session = self.create_mcp_session(init)  # type: ignore[arg-type]
      return await action(session)
    except Exception as e:
      self.logger.error(f"Session action failed: {e}")
      raise
    finally:
      if session:
        try:
          await session.close()
        except Exception as e:
          self.logger.warning(f"Failed to close session: {e}")

  def with_provider_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable,
  ):
    """Synchronous wrapper for with_provider_session"""
    return asyncio.run(self._with_provider_session_async(provider, init, action))

  async def _with_provider_session_async(
    self,
    provider: Callable[[MetorialSession], Any],
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable,
  ):
    if isinstance(init, str):
      init = {"serverDeployments": [init]}
    elif isinstance(init, list):
      init = {"serverDeployments": init}

    async def session_action(session: MetorialSession):
      try:
        provider_data = await provider(session)

        simplified_session = {
          "tools": provider_data.get("tools"),
          "callTools": lambda tool_calls: session.execute_tools(tool_calls),
          "getToolManager": lambda: session.get_tool_manager(),
          **provider_data,
        }

        return action(simplified_session)

      except Exception as e:
        self.logger.error(f"Error in provider session: {e}")
        raise

    return await self._with_session_async(init, session_action)

  def run(
    self,
    message: str,
    deployment_id: Union[str, List[str]],
    provider_client,
    provider_type: Optional[str] = None,
    max_iterations: int = 5,
  ) -> str:
    """Quick one-liner for simple sync chat testing with metrics - now provider-agnostic!

    Args:
      message: The user message to send
      deployment_id: Metorial server deployment ID(s)
      provider_client: AI provider client (OpenAI, Anthropic, Google, etc.)
      provider_type: Provider type - auto-inferred from client if None
      max_iterations: Maximum number of chat iterations
    """
    metrics = ChatMetrics(start_time=time.time())

    try:

      async def chat_action(session):
        tool_manager = await session.get_tool_manager()
        adapter = create_provider_adapter(provider_type, provider_client, tool_manager)

        messages = [ChatMessage(role="user", content=message)]
        return self.chat_loop(adapter, messages, max_iterations, metrics)

      result = self.with_session(deployment_id, chat_action)

      metrics.end_time = time.time()
      self.logger.info(
        f"Quick chat (sync) completed in {metrics.duration:.2f}s, {metrics.iterations} iterations, {metrics.tool_calls} tool calls"
      )

      return result  # type: ignore[no-any-return]

    except Exception as e:
      metrics.error = str(e)
      metrics.end_time = time.time()
      self.logger.error(f"Quick chat (sync) failed after {metrics.duration:.2f}s: {e}")
      raise

  def chat_loop(
    self,
    adapter: ProviderAdapter,
    messages: List[ChatMessage],
    max_iterations: int = 10,
    metrics: Optional[ChatMetrics] = None,
  ) -> str:
    """New synchronous provider-agnostic chat loop implementation"""
    if metrics is None:
      metrics = ChatMetrics(start_time=time.time())

    async def async_chat_loop():
      for i in range(max_iterations):
        metrics.iterations = i + 1

        try:
          # Get tools formatted for this provider
          tools = adapter.get_tools_for_provider()

          # Create chat completion using the adapter
          response = await adapter.create_chat_completion(
            messages=messages, tools=tools
          )

          # Track token usage if available
          if response.usage:
            metrics.tokens_used = response.usage.get("total_tokens", 0)

          # No more tool calls -> we have the final response
          if not response.tool_calls:
            metrics.end_time = time.time()
            return response.content or ""

          # Execute tool calls using the adapter
          tool_responses = await adapter.call_tools(response.tool_calls)
          metrics.tool_calls += len(response.tool_calls)

          # Add assistant message with tool calls and tool responses to the message history
          messages.append(ChatMessage(role="assistant", tool_calls=response.tool_calls))
          messages.extend(tool_responses)

        except Exception as e:
          self.logger.error(f"Chat loop iteration {i + 1} failed: {e}")
          raise MetorialAPIError(f"Chat loop failed at iteration {i + 1}: {e}")

      raise MetorialAPIError(
        f"No final response received after {max_iterations} iterations"
      )

    try:
      # We're in an async context, use ThreadPoolExecutor
      import concurrent.futures

      with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(asyncio.run, async_chat_loop())
        return future.result()  # type: ignore[no-any-return]
    except RuntimeError:
      # No running loop, we can use asyncio.run
      return asyncio.run(async_chat_loop())  # type: ignore[no-any-return]

  def batch_run(
    self,
    messages: List[str],
    deployment_id: Union[str, List[str]],
    provider_client,
    provider_type: Optional[str] = None,
    max_iterations: int = 5,
  ) -> List[str]:
    """Process multiple chat messages concurrently (sync version) - now provider-agnostic!"""

    async def async_batch_chat():
      async def process_single_chat(message: str) -> str:
        return self.run(
          message, deployment_id, provider_client, provider_type, max_iterations
        )

      return await asyncio.gather(
        *[process_single_chat(message) for message in messages]
      )

    try:
      results = asyncio.run(async_batch_chat())
      self.logger.info(
        f"Batch chat (sync) completed: {len(messages)} messages processed"
      )
      return results  # type: ignore[no-any-return]
    except Exception as e:
      self.logger.error(f"Batch chat (sync) failed: {e}")
      raise MetorialAPIError(f"Batch chat processing failed: {e}")

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    asyncio.run(self.close())
