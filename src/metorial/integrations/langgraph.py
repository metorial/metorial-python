"""LangGraph integration for Metorial."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def create_langgraph_tools(session: "ProviderSession") -> list[Any]:
  """
  Convert Metorial session tools to LangGraph-compatible tools.

  LangGraph uses the same tool format as LangChain, so this is an alias
  for the LangChain integration with additional LangGraph-specific helpers.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of LangChain/LangGraph StructuredTool objects

  Example:
      ```python
      from langgraph.prebuilt import create_react_agent
      from langchain_openai import ChatOpenAI
      from metorial import Metorial
      from metorial.integrations.langgraph import create_langgraph_tools

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[deployment_id],
      ) as session:
          tools = create_langgraph_tools(session)
          llm = ChatOpenAI(model="gpt-4o")
          agent = create_react_agent(llm, tools)

          async for event in agent.astream(
              {"messages": [("user", "Search for Python news")]}
          ):
              print(event)
      ```
  """
  # LangGraph uses the same tools as LangChain
  from metorial.integrations.langchain import create_langchain_tools

  return create_langchain_tools(session)


def create_langgraph_tool_node(session: "ProviderSession") -> Any:
  """
  Create a LangGraph ToolNode with Metorial tools.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      A LangGraph ToolNode configured with Metorial tools

  Example:
      ```python
      from langgraph.graph import StateGraph, MessagesState
      from metorial.integrations.langgraph import create_langgraph_tool_node

      async with metorial.provider_session(...) as session:
          tool_node = create_langgraph_tool_node(session)

          graph = StateGraph(MessagesState)
          graph.add_node("tools", tool_node)
          # ... configure rest of graph
      ```
  """
  try:
    from langgraph.prebuilt import ToolNode
  except ImportError as e:
    raise ImportError(
      "LangGraph is required for this integration. "
      "Install it with: pip install langgraph"
    ) from e

  tools = create_langgraph_tools(session)
  return ToolNode(tools)
