"""LlamaIndex integration for Metorial."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def create_llamaindex_tools(session: "ProviderSession") -> list[Any]:
  """
  Convert Metorial session tools to LlamaIndex FunctionTool objects.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of LlamaIndex FunctionTool objects

  Example:
      ```python
      from llama_index.core.agent import ReActAgent
      from llama_index.llms.openai import OpenAI
      from metorial import Metorial
      from metorial.integrations.llamaindex import create_llamaindex_tools

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[deployment_id],
      ) as session:
          tools = create_llamaindex_tools(session)
          llm = OpenAI(model="gpt-4o")
          agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
          response = agent.chat("Search for Python news")
      ```
  """
  try:
    from llama_index.core.tools import FunctionTool, ToolMetadata
  except ImportError as e:
    raise ImportError(
      "LlamaIndex is required for this integration. "
      "Install it with: pip install llama-index"
    ) from e

  tools = []
  metorial_tools = session.get_tools()

  for tool in metorial_tools:
    # Handle OpenAI-style format (type: function, function: {name, ...})
    if "function" in tool:
      fn = tool["function"]
      tool_name = fn.get("name", "")
      tool_description = fn.get("description", "")
      input_schema = fn.get("parameters", {})
    else:
      # Handle direct format (name, description, inputSchema)
      tool_name = tool.get("name", "")
      tool_description = tool.get("description", "")
      input_schema = tool.get("inputSchema", {})

    # Create the tool function with proper name
    tool_fn = _create_tool_function(session, tool_name)

    # Create the Pydantic model for parameters
    fn_schema = _convert_json_schema_to_pydantic(tool_name, input_schema)

    # Create metadata explicitly
    metadata = ToolMetadata(
      name=tool_name,
      description=tool_description,
      fn_schema=fn_schema,
    )

    # Create FunctionTool with explicit metadata
    fn_tool = FunctionTool(
      fn=tool_fn,
      metadata=metadata,
    )
    tools.append(fn_tool)

  return tools


def _create_tool_function(session: "ProviderSession", tool_name: str):
  """Create a tool function for LlamaIndex."""
  import asyncio

  def tool_fn(**kwargs: Any) -> str:
    async def call():
      # Filter out None values
      filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
      result = await session.call_tool(tool_name, filtered_kwargs)
      if isinstance(result, dict):
        content = result.get("content", [])
        if isinstance(content, list):
          texts = []
          for item in content:
            if isinstance(item, dict) and "text" in item:
              texts.append(item["text"])
          return "\n".join(texts) if texts else str(result)
        return str(content)
      return str(result)

    try:
      asyncio.get_running_loop()
      import concurrent.futures

      with concurrent.futures.ThreadPoolExecutor() as pool:
        future = pool.submit(asyncio.run, call())
        return future.result()
    except RuntimeError:
      return asyncio.run(call())

  # Set function name for better debugging
  tool_fn.__name__ = tool_name
  return tool_fn


def _convert_json_schema_to_pydantic(name: str, schema: dict[str, Any]) -> Any:
  """Convert JSON schema to a Pydantic model for LlamaIndex."""
  try:
    from pydantic import Field, create_model
  except ImportError:
    return None

  properties = schema.get("properties", {})
  required = set(schema.get("required", []))

  fields = {}
  for prop_name, prop_schema in properties.items():
    prop_type = prop_schema.get("type", "string")
    prop_desc = prop_schema.get("description", "")

    python_type: Any = str
    if prop_type == "integer":
      python_type = int
    elif prop_type == "number":
      python_type = float
    elif prop_type == "boolean":
      python_type = bool
    elif prop_type == "array":
      python_type = list
    elif prop_type == "object":
      python_type = dict

    if prop_name in required:
      fields[prop_name] = (python_type, Field(description=prop_desc))
    else:
      fields[prop_name] = (
        python_type | None,
        Field(default=None, description=prop_desc),
      )

  model = create_model(f"{name}Input", **fields)
  return model
