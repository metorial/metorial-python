"""smolagents (Hugging Face) integration for Metorial."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def create_smolagents_tools(session: "ProviderSession") -> list[Any]:
  """
  Convert Metorial session tools to smolagents Tool objects.

  Note: Due to smolagents' requirement for source code inspection,
  this integration creates Tool objects that work with ToolCallingAgent
  but may have limited functionality with CodeAgent.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of smolagents Tool objects

  Example:
      ```python
      from smolagents import ToolCallingAgent, HfApiModel
      from metorial import Metorial
      from metorial.integrations.smolagents import create_smolagents_tools

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[deployment_id],
      ) as session:
          tools = create_smolagents_tools(session)
          model = HfApiModel()
          agent = ToolCallingAgent(tools=tools, model=model)
          result = agent.run("Search for Python news")
      ```
  """
  try:
    from smolagents import Tool  # noqa: F401
  except ImportError as e:
    raise ImportError(
      "smolagents is required for this integration. "
      "Install it with: pip install smolagents"
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

    # Create a smolagents Tool instance
    smolagents_tool = _create_smolagent_tool(
      session, tool_name, tool_description, input_schema
    )
    tools.append(smolagents_tool)

  return tools


def _create_smolagent_tool(
  session: "ProviderSession",
  tool_name: str,
  tool_description: str,
  input_schema: dict[str, Any],
) -> Any:
  """Create a smolagents Tool for a Metorial tool."""
  import asyncio

  from smolagents import Tool

  # Convert JSON schema properties to smolagents input format
  schema_properties = input_schema.get("properties", {})
  schema_required = set(input_schema.get("required", []))

  # Build inputs dict for smolagents
  inputs_dict: dict[str, dict[str, Any]] = {}
  param_names: list[str] = []

  for prop_name, prop_schema in schema_properties.items():
    prop_type = prop_schema.get("type", "string")
    prop_desc = prop_schema.get("description", "")
    param_names.append(prop_name)

    # Map JSON schema types to smolagents types
    type_map = {
      "string": "string",
      "integer": "integer",
      "number": "number",
      "boolean": "boolean",
      "array": "array",
      "object": "object",
    }

    inputs_dict[prop_name] = {
      "type": type_map.get(prop_type, "string"),
      "description": prop_desc,
    }
    # smolagents expects 'nullable' for optional params
    if prop_name not in schema_required:
      inputs_dict[prop_name]["nullable"] = True

  # Create the executor function
  def make_executor():
    def executor(**kwargs: Any) -> str:
      async def call():
        # Filter out None values
        filtered = {k: v for k, v in kwargs.items() if v is not None}
        result = await session.call_tool(tool_name, filtered)
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

    return executor

  executor_fn = make_executor()

  # Build the forward method signature dynamically
  # Required params come first without default, nullable params with default=None
  required_params = [p for p in param_names if p in schema_required]
  nullable_params = [p for p in param_names if p not in schema_required]

  if param_names:
    # Build param string: required first, then nullable with =None
    param_parts = required_params + [f"{p}=None" for p in nullable_params]
    param_str = ", ".join(param_parts)
    call_str = ", ".join(f"{p}={p}" for p in param_names)
    forward_code = f"""
def forward(self, {param_str}) -> str:
    return _executor({call_str})
"""
  else:
    forward_code = """
def forward(self) -> str:
    return _executor()
"""

  # Create the forward method
  local_ns: dict[str, Any] = {"_executor": executor_fn}
  exec(forward_code, local_ns, local_ns)
  forward_method = local_ns["forward"]

  # Create the tool class dynamically
  tool_class = type(
    f"MetorialTool_{tool_name}",
    (Tool,),
    {
      "name": tool_name,
      "description": tool_description,
      "inputs": inputs_dict,
      "output_type": "string",
      "forward": forward_method,
    },
  )

  return tool_class()
