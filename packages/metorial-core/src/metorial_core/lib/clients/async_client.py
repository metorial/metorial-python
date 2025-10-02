"""
Metorial Async Client
"""

import asyncio
import time
from typing import Dict, Any, List, Optional, Callable, Union, AsyncGenerator
from ...base import MetorialBase
from ...session import MetorialSession
from ...adapters import ProviderAdapter, ChatMessage, create_provider_adapter
from ..exceptions import MetorialAPIError
from ..metrics import ChatMetrics
from ..streaming import StreamEvent, StreamEventType


class Metorial(MetorialBase):
  """Async-first Metorial client with streaming and enhanced features"""

  async def create_mcp_connection(self, init: Dict[str, Any]):
    """Create MCP connection with retry logic"""
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
        await asyncio.sleep(2**attempt)  # Exponential backoff

  async def with_session(
    self,
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable[[MetorialSession], Any],
  ):
    """Enhanced session management with error handling"""
    session = None
    try:
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

  async def with_provider_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: Union[Dict[str, Any], str, List[str]],
    action: Callable,
  ):
    # Convert flexible init to proper format
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

        return await action(simplified_session)

      except Exception as e:
        self.logger.error(f"Error in provider session: {e}")
        raise

    return await self.with_session(init, session_action)

  async def with_oauth_session(
    self,
    oauth_session_id: str,
    deployment_id: str,
    action: Callable[[MetorialSession], Any],
  ):
    """OAuth session management - creates a regular session with OAuth authentication"""
    import httpx

    try:
      # Step 1: Create a regular MCP session using the OAuth session for authentication
      # Pass the OAuth session ID as authentication
      self.logger.info(
        f"Creating MCP session with OAuth authentication: {oauth_session_id}"
      )

      async with httpx.AsyncClient() as client:
        # Create a regular session with OAuth session as auth
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
                "config": {},  # Empty config for OAuth
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
        self.logger.info(f"✅ Created MCP session: {session_data.get('id')}")

      # Step 2: Create MCP session wrapper with the created session data
      from metorial_mcp_session import MetorialMcpSession
      from ...session import SessionFactory

      mcp_init = {
        "serverDeployments": [deployment_id],
        "client": {"name": "metorial-python", "version": "1.0.0"},
      }

      mcp_session = MetorialMcpSession(sdk=self, init=mcp_init)  # type: ignore[arg-type]
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

  async def _run_with_oauth(
    self,
    message: str,
    deployment_id: str,
    provider_client,
    provider_type: Optional[str],
    max_iterations: int,
    oauth_session_id: Optional[str],
    oauth_connection_id: Optional[str],
    oauth_metadata: Optional[Dict[str, Any]],
    metrics: ChatMetrics,
  ) -> str:
    """Run chat with OAuth session"""
    import httpx

    # If session ID provided, use it directly
    if oauth_session_id:
      self.logger.info(f"Using existing OAuth session: {oauth_session_id}")
      session_id = oauth_session_id
    else:
      # Create new OAuth session
      if not oauth_connection_id:
        # Auto-detect OAuth connection
        try:
          connections = self.provider_oauth.connections.list()  # type: ignore[attr-defined]
          if not connections.items or len(connections.items) == 0:
            raise MetorialAPIError(
              "No OAuth connections found. Please create one first or provide oauth_connection_id."
            )
          oauth_connection_id = connections.items[0].id
          self.logger.info(f"Auto-detected OAuth connection: {oauth_connection_id}")
        except Exception as e:
          raise MetorialAPIError(f"Failed to get OAuth connections: {e}")

      # Create OAuth session via HTTP
      self.logger.info(f"Creating OAuth session for deployment: {deployment_id}")
      async with httpx.AsyncClient() as client:
        response = await client.post(
          f"{self._config['apiHost']}/provider-oauth/sessions",
          headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self._config['apiKey']}",
          },
          json={
            "server_deployment_id": deployment_id,
            "connection_id": oauth_connection_id,
            "metadata": oauth_metadata or {},
          },
        )

        if response.status_code not in [200, 201]:
          raise MetorialAPIError(
            f"Failed to create OAuth session: {response.status_code} - {response.text}"
          )

        oauth_session = response.json()
        session_id = oauth_session["id"]

        if oauth_session.get("status") == "pending":
          auth_url = oauth_session.get("url")
          self.logger.info(f"OAuth session created: {session_id}")
          self.logger.info(f"Opening browser for authorization...")

          # Automatically open the authorization URL in the browser
          import webbrowser

          webbrowser.open(auth_url)

          # print(f"\n✅ Browser opened for OAuth authorization!")
          # print(f"🔗 URL: {auth_url}")
          # print(f"⏳ Waiting for you to authorize...")
          # print(f"💡 Press Ctrl+C to cancel and retry later with oauth_session_id='{session_id}'\n")

          # Poll the session status to wait for authorization
          max_wait = 120  # Wait up to 2 minutes
          poll_interval = 2  # Check every 2 seconds

          for attempt in range(max_wait // poll_interval):
            await asyncio.sleep(poll_interval)

            # Check session status
            async with httpx.AsyncClient() as check_client:
              status_response = await check_client.get(
                f"{self._config['apiHost']}/provider-oauth/sessions/{session_id}",
                headers={
                  "Accept": "application/json",
                  "Authorization": f"Bearer {self._config['apiKey']}",
                },
              )

              if status_response.status_code == 200:
                session_data = status_response.json()
                if session_data.get("status") in ["active", "completed"]:
                  self.logger.info("✅ OAuth authorization successful!")
                  break

          else:
            # Timeout - authorization not completed
            raise MetorialAPIError(
              f"OAuth authorization timed out after {max_wait}s. "
              f"Please authorize at: {auth_url} "
              f"Then retry with oauth_session_id='{session_id}'"
            )

    # Use the OAuth session with MCP
    async def chat_action(session):
      tool_manager = await session.get_tool_manager()
      adapter = create_provider_adapter(provider_type, provider_client, tool_manager)

      messages = [ChatMessage(role="user", content=message)]
      result = await self.chat_loop(adapter, messages, max_iterations, metrics)
      return result

    result = await self.with_session(
      {"serverDeployments": [deployment_id]}, chat_action
    )

    metrics.end_time = time.time()
    return result  # type: ignore[no-any-return]

  async def run(
    self,
    message: str,
    deployment_id: Union[str, List[str]],
    provider_client,
    provider_type: Optional[str] = None,
    max_iterations: int = 5,
    model: Optional[str] = None,
    tools: Optional[List[Dict[str, Any]]] = None,
    oauth_session_id: Optional[str] = None,
    oauth_connection_id: Optional[str] = None,
    oauth_metadata: Optional[Dict[str, Any]] = None,
  ) -> str:
    metrics = ChatMetrics(start_time=time.time())

    try:
      # If OAuth parameters provided, create OAuth session
      if oauth_session_id or oauth_connection_id or oauth_metadata:
        return await self._run_with_oauth(
          message,
          deployment_id,
          provider_client,
          provider_type,
          max_iterations,
          oauth_session_id,
          oauth_connection_id,
          oauth_metadata,
          metrics,
        )

      # Regular MCP session flow
      async def chat_action(session):
        tool_manager = await session.get_tool_manager()
        adapter = create_provider_adapter(provider_type, provider_client, tool_manager)

        messages = [ChatMessage(role="user", content=message)]
        result = await self.chat_loop(adapter, messages, max_iterations, metrics)
        return result

      result = await self.with_session(deployment_id, chat_action)

      metrics.end_time = time.time()
      # self.logger.info(f"Quick chat completed in {metrics.duration:.2f}s, {metrics.iterations} iterations, {metrics.tool_calls} tool calls")

      return result  # type: ignore[no-any-return]

    except Exception as e:
      metrics.error = str(e)
      metrics.end_time = time.time()
      self.logger.error(f"Quick chat failed after {metrics.duration:.2f}s: {e}")
      raise

  async def run_oauth(
    self,
    message: str,
    deployment_id: str,
    provider_client,
    provider_type: Optional[str] = None,
    max_iterations: int = 5,
    oauth_session_id: Optional[str] = None,
    oauth_connection_id: Optional[str] = None,
    oauth_metadata: Optional[Dict[str, Any]] = None,
    model: Optional[str] = None,
  ) -> str:
    """Run AI task with OAuth session - only for local use.

    This method creates/uses OAuth sessions and automatically handles browser-based authorization.
    """
    import httpx

    metrics = ChatMetrics(start_time=time.time())

    try:
      # Step 1: Get or create OAuth session
      if oauth_session_id:
        self.logger.info(f"Using existing OAuth session: {oauth_session_id}")
        session_id = oauth_session_id
      else:
        # Auto-detect OAuth connection if not provided
        if not oauth_connection_id:
          connections = self.provider_oauth.connections.list()  # type: ignore[attr-defined]
          if not connections.items or len(connections.items) == 0:
            raise MetorialAPIError(
              "No OAuth connections found. Create one first or provide oauth_connection_id."
            )
          oauth_connection_id = connections.items[0].id
          self.logger.info(f"Auto-detected OAuth connection: {oauth_connection_id}")

        # Create OAuth session
        self.logger.info(f"Creating OAuth session for deployment: {deployment_id}")
        async with httpx.AsyncClient() as client:
          response = await client.post(
            f"{self._config['apiHost']}/provider-oauth/sessions",
            headers={
              "Content-Type": "application/json",
              "Authorization": f"Bearer {self._config['apiKey']}",
            },
            json={
              "server_deployment_id": deployment_id,
              "connection_id": oauth_connection_id,
              "metadata": oauth_metadata or {},
            },
          )

          if response.status_code not in [200, 201]:
            raise MetorialAPIError(
              f"Failed to create OAuth session: {response.status_code} - {response.text}"
            )

          oauth_session = response.json()
          session_id = oauth_session["id"]

          # Handle authorization flow
          if oauth_session.get("status") == "pending":
            auth_url = oauth_session.get("url")
            self.logger.info(f"OAuth session created: {session_id}")

            # Open browser
            import webbrowser

            webbrowser.open(auth_url)

            # print(f"\n✅ Browser opened for OAuth authorization!")
            # print(f"🔗 {auth_url}")
            # print(f"⏳ Waiting for authorization...")
            # print(f"💡 Press Ctrl+C to cancel and retry with oauth_session_id='{session_id}'\n")

            # Poll for authorization
            max_wait = 120
            poll_interval = 2

            for attempt in range(max_wait // poll_interval):
              await asyncio.sleep(poll_interval)

              async with httpx.AsyncClient() as check_client:
                status_resp = await check_client.get(
                  f"{self._config['apiHost']}/provider-oauth/sessions/{session_id}",
                  headers={"Authorization": f"Bearer {self._config['apiKey']}"},
                )

                if status_resp.status_code == 200:
                  session_data = status_resp.json()
                  if session_data.get("status") in ["active", "completed"]:
                    self.logger.info("✅ OAuth authorization successful!")
                    # print("✅ Authorization complete!\n")
                    break
            else:
              raise MetorialAPIError(
                f"Authorization timed out. Retry with: oauth_session_id='{session_id}'"
              )

      # Step 2: Use OAuth session directly with with_oauth_session
      async def chat_action(session):
        tool_manager = await session.get_tool_manager()
        adapter = create_provider_adapter(provider_type, provider_client, tool_manager)

        messages = [ChatMessage(role="user", content=message)]
        result = await self.chat_loop(adapter, messages, max_iterations, metrics)
        return result

      result = await self.with_oauth_session(session_id, deployment_id, chat_action)

      metrics.end_time = time.time()
      self.logger.info(f"OAuth chat completed in {metrics.duration:.2f}s")

      return result  # type: ignore[no-any-return]

    except Exception as e:
      metrics.error = str(e)
      metrics.end_time = time.time()
      self.logger.error(f"OAuth chat failed: {e}")
      raise

  async def chat_loop(self, *args, **kwargs) -> str:
    """Enhanced provider-agnostic chat loop with backward compatibility"""
    # Handle backward compatibility
    if len(args) >= 3 and not isinstance(args[0], ProviderAdapter):
      # Old signature: chat_loop(client, session, messages, max_iterations, metrics)
      return await self._chat_loop_legacy(*args, **kwargs)
    else:
      # New signature: chat_loop(adapter, messages, max_iterations, metrics)
      return await self._chat_loop_new(*args, **kwargs)

  async def _chat_loop_new(
    self,
    adapter: ProviderAdapter,
    messages: List[ChatMessage],
    max_iterations: int = 10,
    metrics: Optional[ChatMetrics] = None,
  ) -> str:
    """New provider-agnostic chat loop implementation"""
    if metrics is None:
      metrics = ChatMetrics(start_time=time.time())

    for i in range(max_iterations):
      metrics.iterations = i + 1

      try:
        # Get tools formatted for this provider
        tools = adapter.get_tools_for_provider()

        # Create chat completion using the adapter
        response = await adapter.create_chat_completion(messages=messages, tools=tools)

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

        # Get tools formatted for this provider
        tools = adapter.get_tools_for_provider()

        # Create streaming chat completion using the adapter
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

        # If we have tool calls, execute them
        if tool_calls:
          try:
            tool_responses = await adapter.call_tools(tool_calls)
            metrics.tool_calls += len(tool_calls)

            # Add tool responses to messages
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
          # No tool calls, we're done
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

      # If we get here, we exceeded max_iterations
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

  async def batch_run(
    self,
    messages: List[str],
    deployment_id: Union[str, List[str]],
    provider_client,
    provider_type: Optional[str] = None,
    max_iterations: int = 5,
  ) -> List[str]:
    """Process multiple chat messages concurrently - now provider-agnostic!"""

    async def process_single_chat(message: str) -> str:
      return await self.run(
        message, deployment_id, provider_client, provider_type, max_iterations
      )

    try:
      # Process all messages concurrently using asyncio.gather
      results = await asyncio.gather(
        *[process_single_chat(message) for message in messages]
      )

      self.logger.info(f"Batch chat completed: {len(messages)} messages processed")
      return results

    except Exception as e:
      self.logger.error(f"Batch chat failed: {e}")
      raise MetorialAPIError(f"Batch chat processing failed: {e}")

  # Context manager support
  async def __aenter__(self):
    return self

  async def __aexit__(self, exc_type, exc_val, exc_tb):
    await self.close()
