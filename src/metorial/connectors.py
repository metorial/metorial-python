"""
Helpers for the adapter-first `metorial.connect(...)` API.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any, Generic, Protocol, TypeVar, cast

from metorial._session import MetorialSession
from metorial._tool_manager import ToolManager
from metorial.integrations.autogen import create_autogen_tools
from metorial.integrations.crewai import create_crewai_tools
from metorial.integrations.google_adk import create_google_adk_tools
from metorial.integrations.haystack import create_haystack_tools
from metorial.integrations.langchain import create_langchain_tools
from metorial.integrations.langgraph import create_langgraph_tools
from metorial.integrations.llamaindex import create_llamaindex_tools
from metorial.integrations.openai_agents import create_openai_agent_tools
from metorial.integrations.pydantic_ai import create_pydantic_ai_tools
from metorial.providers.anthropic import MetorialAnthropicSession
from metorial.providers.deepseek import MetorialDeepSeekSession
from metorial.providers.google import MetorialGoogleSession
from metorial.providers.mistral import MetorialMistralSession
from metorial.providers.openai import MetorialOpenAISession, build_openai_tools
from metorial.providers.openai_compatible import MetorialOpenAICompatibleSession
from metorial.providers.togetherai import MetorialTogetherAISession
from metorial.providers.xai import MetorialXAISession

TResolved = TypeVar("TResolved")
TResolved_co = TypeVar("TResolved_co", covariant=True)
TTools = TypeVar("TTools")


class MetorialAdapter(Protocol[TResolved_co]):
  async def __resolve(self, session: MetorialSession) -> TResolved_co: ...


@dataclass
class _Adapter(Generic[TResolved]):
  resolver: Callable[[MetorialSession], Awaitable[TResolved]]

  def __post_init__(self) -> None:
    setattr(self, "__resolve", self._resolve)

  async def _resolve(self, session: MetorialSession) -> TResolved:
    return await self.resolver(session)


class ConnectedSession(Generic[TTools]):
  """Resolved `connect()` handle returned by first-party adapters."""

  def __init__(
    self,
    session: MetorialSession,
    tools: TTools,
    call_tools: Callable[[Any], Awaitable[Any]] | None = None,
  ) -> None:
    self._session = session
    self._tools = tools
    self._call_tools = call_tools

  def tools(self) -> TTools:
    return self._tools

  async def call_tools(self, tool_calls: Any) -> Any:
    if self._call_tools is None:
      raise RuntimeError("This adapter does not expose call_tools().")
    return await self._call_tools(tool_calls)

  async def callTools(self, tool_calls: Any) -> Any:
    return await self.call_tools(tool_calls)

  async def get_tool_manager(self) -> ToolManager:
    return await self._session.get_tool_manager()

  async def close(self) -> None:
    return None

  async def __aenter__(self) -> ConnectedSession[TTools]:
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: object,
  ) -> None:
    await self.close()


class _IntegrationSessionView:
  """Thin session shim so connect adapters can reuse existing integrations."""

  def __init__(
    self,
    session: MetorialSession,
    tool_manager: ToolManager,
    tool_defs: list[dict[str, Any]],
  ) -> None:
    self._session = session
    self.tool_manager = tool_manager
    self._tool_defs = tool_defs

  def get_tools(self) -> list[dict[str, Any]]:
    return self._tool_defs

  async def call_tool(self, tool_name: str, kwargs: dict[str, Any]) -> Any:
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    result = await self.tool_manager.execute_tool(tool_name, filtered_kwargs)
    return result

  async def close(self) -> None:
    await self._session.close()


def create_mcp_sdk(
  handler: Callable[[MetorialSession], Awaitable[TResolved]],
) -> Callable[[], MetorialAdapter[TResolved]]:
  def factory() -> MetorialAdapter[TResolved]:
    return cast(MetorialAdapter[TResolved], _Adapter(handler))

  return factory


async def _resolve_provider_session(
  session: MetorialSession,
  provider_factory: Callable[[MetorialSession], Any],
) -> ConnectedSession[Any]:
  provider_session = provider_factory(session)
  await provider_session
  return ConnectedSession(
    session=session,
    tools=provider_session.tools,
    call_tools=provider_session.call_tools,
  )


async def _resolve_integration_tools(
  session: MetorialSession,
  integration_factory: Callable[[Any], TTools],
) -> ConnectedSession[TTools]:
  tool_manager = await session.get_tool_manager()
  session_view = _IntegrationSessionView(
    session=session,
    tool_manager=tool_manager,
    tool_defs=build_openai_tools(tool_manager),
  )
  return ConnectedSession(session=session, tools=integration_factory(session_view))


async def _resolve_openai(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialOpenAISession)


async def _resolve_anthropic(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialAnthropicSession)


async def _resolve_google(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialGoogleSession)


async def _resolve_mistral(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialMistralSession)


async def _resolve_deepseek(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialDeepSeekSession)


async def _resolve_togetherai(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialTogetherAISession)


async def _resolve_xai(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_provider_session(session, MetorialXAISession)


async def _resolve_openai_compatible(
  session: MetorialSession,
  *,
  with_strict: bool,
) -> ConnectedSession[Any]:
  return await _resolve_provider_session(
    session,
    lambda current_session: MetorialOpenAICompatibleSession(
      current_session,
      with_strict=with_strict,
    ),
  )


async def _resolve_pydantic_ai(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_pydantic_ai_tools)


async def _resolve_autogen(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_autogen_tools)


async def _resolve_langchain(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_langchain_tools)


async def _resolve_langgraph(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_langgraph_tools)


async def _resolve_llamaindex(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_llamaindex_tools)


async def _resolve_openai_agents(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_openai_agent_tools)


async def _resolve_crewai(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_crewai_tools)


async def _resolve_google_adk(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_google_adk_tools)


async def _resolve_haystack(session: MetorialSession) -> ConnectedSession[Any]:
  return await _resolve_integration_tools(session, create_haystack_tools)


metorial_openai = create_mcp_sdk(_resolve_openai)
metorial_anthropic = create_mcp_sdk(_resolve_anthropic)
metorial_google = create_mcp_sdk(_resolve_google)
metorial_mistral = create_mcp_sdk(_resolve_mistral)
metorial_deepseek = create_mcp_sdk(_resolve_deepseek)
metorial_togetherai = create_mcp_sdk(_resolve_togetherai)
metorial_xai = create_mcp_sdk(_resolve_xai)
metorial_pydantic_ai = create_mcp_sdk(_resolve_pydantic_ai)
metorial_autogen = create_mcp_sdk(_resolve_autogen)
metorial_langchain = create_mcp_sdk(_resolve_langchain)
metorial_langgraph = create_mcp_sdk(_resolve_langgraph)
metorial_llamaindex = create_mcp_sdk(_resolve_llamaindex)
metorial_openai_agents = create_mcp_sdk(_resolve_openai_agents)
metorial_crewai = create_mcp_sdk(_resolve_crewai)
metorial_google_adk = create_mcp_sdk(_resolve_google_adk)
metorial_haystack = create_mcp_sdk(_resolve_haystack)


def metorial_openai_compatible(
  *,
  with_strict: bool = False,
) -> MetorialAdapter[ConnectedSession[Any]]:
  return cast(
    MetorialAdapter[ConnectedSession[Any]],
    _Adapter(
      lambda session: _resolve_openai_compatible(session, with_strict=with_strict)
    ),
  )


__all__ = [
  "ConnectedSession",
  "MetorialAdapter",
  "create_mcp_sdk",
  "metorial_anthropic",
  "metorial_autogen",
  "metorial_crewai",
  "metorial_deepseek",
  "metorial_google",
  "metorial_google_adk",
  "metorial_haystack",
  "metorial_langchain",
  "metorial_langgraph",
  "metorial_llamaindex",
  "metorial_mistral",
  "metorial_openai",
  "metorial_openai_agents",
  "metorial_openai_compatible",
  "metorial_pydantic_ai",
  "metorial_togetherai",
  "metorial_xai",
]
