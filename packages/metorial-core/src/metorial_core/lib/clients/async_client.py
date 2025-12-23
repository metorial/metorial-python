import asyncio
import time
from typing import Dict, Any, List, Optional, Callable, Union, AsyncGenerator
from ...base import MetorialBase
from ...session import MetorialSession
from ...adapters import ProviderAdapter, ChatMessage, create_provider_adapter
from metorial_exceptions import MetorialAPIError
from ..metrics import ChatMetrics
from ..streaming import StreamEvent, StreamEventType
from ...adapters.factory import infer_provider_type
from ...types import RunResult


class Metorial(MetorialBase):
  def _detect_provider_type(self, client: Any) -> str:
    return infer_provider_type(client)

  def _normalize_server_deployments(
    self, server_deployments: Union[List[str], List[Dict[str, str]]]
  ) -> List[Dict[str, str]]:
    """Normalize server deployments to handle both string and object formats."""
    normalized = []

    for deployment in server_deployments:
      if isinstance(deployment, str):
        # Simple string format -> convert to object
        normalized.append({"serverDeploymentId": deployment})
      elif isinstance(deployment, dict):
        # Already object format -> validate and use as-is
        if "serverDeploymentId" in deployment:
          normalized.append(deployment)
        elif "id" in deployment:
          converted = {"serverDeploymentId": deployment["id"]}
          if "oauthSessionId" in deployment:
            converted["oauthSessionId"] = deployment["oauthSessionId"]
          normalized.append(converted)
        else:
          raise ValueError(f"Invalid deployment object format: {deployment}")
      else:
        raise ValueError(
          f"Invalid deployment type: {type(deployment)} - must be string or dict"
        )

    return normalized

  async def create_mcp_connection(self, init: Dict[str, Any]):
    for attempt in range(self._config["maxRetries"]):
      try:
        session = self.create_mcp_session(init)
        deployments = await session.get_server_deployments()
        return await session.get_client({"deploymentId": deployments[0]["id"]})
      except Exception as e:
        if attempt == self._config["maxRetries"] - 1:
          raise MetorialAPIError(
            f"Failed to create MCP connection after {self._config['maxRetries']} attempts: {e}"
          )
        await asyncio.sleep(2**attempt)

  async def with_session(
    self,
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable[[MetorialSession], Any],
  ):
    if isinstance(init, str):
      init = {"serverDeployments": [init]}
    elif isinstance(init, list):
      init = {"serverDeployments": init}

    session = self.create_mcp_session(init)
    try:
      return await action(session)
    except Exception as e:
      self.logger.error(f"Session action failed: {e}")
      raise

  async def with_provider_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable,
  ):
    if isinstance(init, str):
      init = {"serverDeployments": [init]}
    elif isinstance(init, list):
      init = {"serverDeployments": init}

    # Check if streaming mode is enabled
    streaming = init.get("streaming", False) if isinstance(init, dict) else False

    if streaming:
      return await self._with_streaming_session(provider, init, action)

    async def session_action(session: MetorialSession):
      try:
        provider_data = await provider(session)

        simplified_session = {
          "tools": provider_data.get("tools"),
          "callTools": provider_data.get("callTools") or (lambda tool_calls: session.execute_tools(tool_calls)),
          "getToolManager": lambda: session.get_tool_manager(),
          "session": session,
          "closeSession": session.close
          if hasattr(session, "close")
          else lambda: session._mcp_session.close(),
          "getSession": session.get_session
          if hasattr(session, "get_session")
          else lambda: session._mcp_session.get_session(),
          "getCapabilities": session.get_capabilities
          if hasattr(session, "get_capabilities")
          else lambda: session._mcp_session.get_capabilities(),
          "getClient": session.get_client
          if hasattr(session, "get_client")
          else lambda opts: session._mcp_session.get_client(opts),
          "getServerDeployments": session.get_server_deployments
          if hasattr(session, "get_server_deployments")
          else lambda: session._mcp_session.get_server_deployments(),
          **provider_data,
        }

        return await action(simplified_session)

      except Exception as e:
        self.logger.error(f"Error in provider session: {e}")
        raise

    # Automatically apply safe cleanup for provider sessions
    try:
      from ..safe_cleanup import quiet_asyncio_shutdown, drain_pending_tasks
    except ImportError:
      from contextlib import nullcontext as quiet_asyncio_shutdown
      async def drain_pending_tasks(): pass

    with quiet_asyncio_shutdown():
      try:
        return await self.with_session(init, session_action)
      finally:
        # Ensure cleanup happens automatically
        await asyncio.create_task(self.close())
        await drain_pending_tasks(timeout=0.2)

  async def _with_streaming_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: Dict[str, Any],
    action: Callable,
  ):
    """
    Streaming session that requires manual closeSession() call.
    Used when streaming: True is set in the init config.
    """
    session = self.create_mcp_session(init)
    session_closed = False

    async def close_session():
      nonlocal session_closed
      if not session_closed:
        session_closed = True
        self.logger.debug("[Metorial] Closing streaming session")
        if hasattr(session, "close"):
          await session.close()
        else:
          await session._mcp_session.close()
        await self.close()

    try:
      provider_data = await provider(session)

      simplified_session = {
        "tools": provider_data.get("tools"),
        "callTools": provider_data.get("callTools") or (lambda tool_calls: session.execute_tools(tool_calls)),
        "getToolManager": lambda: session.get_tool_manager(),
        "session": session,
        "closeSession": close_session,
        "getSession": session.get_session
        if hasattr(session, "get_session")
        else lambda: session._mcp_session.get_session(),
        "getCapabilities": session.get_capabilities
        if hasattr(session, "get_capabilities")
        else lambda: session._mcp_session.get_capabilities(),
        "getClient": session.get_client
        if hasattr(session, "get_client")
        else lambda opts: session._mcp_session.get_client(opts),
        "getServerDeployments": session.get_server_deployments
        if hasattr(session, "get_server_deployments")
        else lambda: session._mcp_session.get_server_deployments(),
        **provider_data,
      }

      result = await action(simplified_session)

      # Safety timeout: close session after 30 seconds if user forgot
      async def safety_close():
        await asyncio.sleep(30)
        if not session_closed:
          self.logger.warning("[Metorial] Streaming session not closed by user, closing automatically")
          await close_session()

      asyncio.create_task(safety_close())

      return result

    except Exception as e:
      self.logger.error(f"Error in streaming session: {e}")
      if not session_closed:
        await close_session()
      raise

  async def with_oauth_session(
    self,
    oauth_session_id: str,
    deployment_id: str,
    action: Callable[[MetorialSession], Any],
  ):
    import httpx

    try:
      self.logger.debug(
        f"Creating MCP session with OAuth authentication: {oauth_session_id}"
      )

      async with httpx.AsyncClient() as client:
        response = await client.post(
          f"{self._config['apiHost']}/sessions",
          headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._config['apiKey']}",
          },
          json={
            "server_deployments": [
              {
                "server_deployment_id": deployment_id,
                "oauth_session_id": oauth_session_id,
                "config": {},
              }
            ],
            "client": {"name": "metorial-python", "version": "1.0.0"},
          },
        )

        if response.status_code not in [200, 201]:
          self.logger.error(
            f"Failed to create session: {response.status_code} - {response.text}"
          )
          raise MetorialAPIError(
            f"Failed to create MCP session with OAuth: {response.status_code}"
          )

        session_data = response.json()
        self.logger.debug(f"✅ Created MCP session: {session_data.get('id')}")

      from metorial_mcp_session import MetorialMcpSession
      from ...session import SessionFactory

      mcp_init = {
        "serverDeployments": [deployment_id],
        "client": {"name": "metorial-python", "version": "1.0.0"},
      }

      mcp_session = MetorialMcpSession(sdk=self, init=mcp_init)
      mcp_session._session = session_data

      session = SessionFactory.create_session(mcp_session)

      return await action(session)

    except Exception as e:
      self.logger.error(f"OAuth session action failed: {e}")
      raise
    finally:
      if "session" in locals():
        try:
          await session.close()
        except Exception as e:
          self.logger.warning(f"Failed to close OAuth session: {e}")

  async def run(
    self,
    *,
    message: str,
    server_deployments: Union[List[str], List[Dict[str, str]]],
    client: Any,
    model: str,
    max_steps: int = 10,
    tools: Optional[List[str]] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
  ) -> RunResult:
    metrics = ChatMetrics(start_time=time.time())

    try:
      provider_type = self._detect_provider_type(client)
      self.logger.debug(f"🔍 Provider type detected: {provider_type}")

      normalized_deployments = self._normalize_server_deployments(server_deployments)
      self.logger.debug(f"📋 Server deployments: {normalized_deployments}")
      self.logger.debug(f"🤖 Model: {model}")
      if tools:
        self.logger.debug(f"🔧 Tool filtering enabled: {tools}")

      async def chat_action(session):
        self.logger.debug("📡 Getting tool manager...")
        tool_manager = await session.get_tool_manager()
        self.logger.debug(f"🔧 Tool manager type: {type(tool_manager)}")

        if tool_manager is not None:
          available_tools = tool_manager.get_tools()
          self.logger.debug(f"🛠️ Available tools: {[t.name for t in available_tools]}")
        else:
          self.logger.debug("⚠️ Tool manager is None")

        if tools is not None and tool_manager is not None:
          filtered_tools = []
          for tool in available_tools:
            if tool.name in tools or tool.id in tools:
              filtered_tools.append(tool)

          self.logger.debug(f"🎯 Filtered tools: {[t.name for t in filtered_tools]}")

          class FilteredToolManager:
            def __init__(self, filtered_tools):
              self._tools = filtered_tools

            def get_tools(self):
              return self._tools

            def get_tool(self, id_or_name):
              for tool in self._tools:
                if tool.name == id_or_name or tool.id == id_or_name:
                  return tool
              return None

            async def call_tool(self, id_or_name, args):
              tool = self.get_tool(id_or_name)
              if tool is None:
                raise KeyError(f"Tool not found: {id_or_name}")
              return await tool.call(args)

          tool_manager = FilteredToolManager(filtered_tools)

        self.logger.debug(f"🔗 Creating adapter for {provider_type}")
        adapter = create_provider_adapter(provider_type, client, tool_manager)
        self.logger.debug(f"✅ Adapter created: {type(adapter)}")

        messages = [ChatMessage(role="user", content=message)]
        chat_kwargs = {"model": model}
        if temperature is not None:
          chat_kwargs["temperature"] = temperature
        if max_tokens is not None:
          chat_kwargs["max_tokens"] = max_tokens

        self.logger.debug(f"🎯 Chat kwargs: {chat_kwargs}")
        self.logger.debug(f"🚀 Starting chat loop with max_steps: {max_steps}")

        result = await self._chat_loop_new(
          adapter, messages, max_steps, metrics, **chat_kwargs
        )
        return result

      if not normalized_deployments:
        raise ValueError("server_deployments must contain at least one deployment")

      # Create single session with ALL deployments like TypeScript
      # Convert to the format expected by session creation
      session_deployments = []
      for deployment in normalized_deployments:
        deployment_config = {"id": deployment["serverDeploymentId"]}
        if "oauthSessionId" in deployment:
          deployment_config["oauthSessionId"] = deployment["oauthSessionId"]
        session_deployments.append(deployment_config)

      # Use single session with all deployments (TypeScript approach)
      session_init = {"serverDeployments": session_deployments}
      result = await self.with_session(session_init, chat_action)

      metrics.end_time = time.time()

      return RunResult(text=result, steps=metrics.iterations)

    except Exception as e:
      metrics.error = str(e)
      metrics.end_time = time.time()
      self.logger.error(f"Quick chat failed after {metrics.duration:.2f}s: {e}")
      raise

  # run_oauth method removed - deprecated, use metorial.run with OAuth session IDs instead

  async def chat_loop(self, *args, **kwargs) -> str:
    if len(args) >= 3 and not isinstance(args[0], ProviderAdapter):
      return await self._chat_loop_legacy(*args, **kwargs)
    else:
      return await self._chat_loop_new(*args, **kwargs)

  async def _chat_loop_new(
    self,
    adapter: ProviderAdapter,
    messages: List[ChatMessage],
    max_iterations: int = 10,
    metrics: Optional[ChatMetrics] = None,
    **chat_kwargs,
  ) -> str:
    if metrics is None:
      metrics = ChatMetrics(start_time=time.time())

    self.logger.debug(f"🔄 Starting chat loop: max_iterations={max_iterations}")
    for i in range(max_iterations):
      metrics.iterations = i + 1
      self.logger.debug(f"🔄 Chat loop iteration {i + 1}")

      try:
        self.logger.debug(f"🛠️ Getting tools from adapter...")
        tools = adapter.get_tools_for_provider()
        self.logger.debug(f"📋 Got {len(tools)} tools for provider")

        self.logger.debug(f"🤖 Creating chat completion with kwargs: {chat_kwargs}")
        response = await adapter.create_chat_completion(
          messages=messages, tools=tools, **chat_kwargs
        )

        if response.usage:
          metrics.tokens_used = response.usage.get("total_tokens", 0)

        if not response.tool_calls:
          self.logger.debug("✅ No tool calls - returning final response")
          metrics.end_time = time.time()
          return response.content or ""

        self.logger.debug(f"🔧 Executing {len(response.tool_calls)} tool calls")
        tool_responses = await adapter.call_tools(response.tool_calls)
        metrics.tool_calls += len(response.tool_calls)
        self.logger.debug(
          f"✅ Tool execution completed, got {len(tool_responses)} responses"
        )

        # Add assistant message with content for Anthropic format
        assistant_content = (
          response.content or f"I'll call {len(response.tool_calls)} tool(s)"
        )
        messages.append(
          ChatMessage(
            role="assistant", content=assistant_content, tool_calls=response.tool_calls
          )
        )
        messages.extend(tool_responses)
        self.logger.debug(f"📝 Updated message history: {len(messages)} messages")

      except Exception as e:
        self.logger.error(f"❌ Chat loop iteration {i + 1} failed: {e}")
        raise MetorialAPIError(f"Chat loop failed at iteration {i + 1}: {e}")

    self.logger.error(
      f"❌ Chat loop exhausted: {max_iterations} iterations without final response"
    )
    raise MetorialAPIError(
      f"No final response received after {max_iterations} iterations"
    )

  async def stream(
    self,
    adapter: ProviderAdapter,
    messages: List[ChatMessage],
    max_iterations: int = 10,
  ) -> AsyncGenerator[StreamEvent, None]:
    metrics = ChatMetrics(start_time=time.time())

    try:
      for i in range(max_iterations):
        metrics.iterations = i + 1

        tools = adapter.get_tools_for_provider()

        stream = await adapter.create_chat_completion_stream(
          messages=messages, tools=tools
        )

        full_response = ""
        tool_calls = []

        async for chunk in stream:
          if chunk["type"] == "content":
            content = chunk["content"]
            full_response += content
            yield StreamEvent(
              type=StreamEventType.CONTENT,
              content=content,
              metadata={"iteration": i + 1},
            )

          elif chunk["type"] == "tool_call":
            tool_calls.append(chunk["tool_call"])
            yield StreamEvent(
              type=StreamEventType.TOOL_CALL,
              tool_calls=[chunk["tool_call"]],
              metadata={"iteration": i + 1},
            )

        if tool_calls:
          try:
            tool_responses = await adapter.call_tools(tool_calls)
            metrics.tool_calls += len(tool_calls)

            messages.append(
              ChatMessage(
                role="assistant", content=full_response, tool_calls=tool_calls
              )
            )
            messages.extend(tool_responses)

          except Exception as e:
            yield StreamEvent(
              type=StreamEventType.ERROR,
              error=f"Tool execution failed: {e}",
              metadata={"iteration": i + 1},
            )
            raise
        else:
          yield StreamEvent(
            type=StreamEventType.COMPLETE,
            content=full_response,
            metadata={
              "iteration": i + 1,
              "duration": time.time() - metrics.start_time,
              "tool_calls": metrics.tool_calls,
            },
          )
          return

      yield StreamEvent(
        type=StreamEventType.ERROR,
        error=f"No final response received after {max_iterations} iterations",
      )

    except Exception as e:
      yield StreamEvent(
        type=StreamEventType.ERROR,
        error=str(e),
        metadata={"iteration": metrics.iterations},
      )
      raise

  async def __aenter__(self):
    return self

  async def __aexit__(self, exc_type, exc_val, exc_tb):
    await self.close()
