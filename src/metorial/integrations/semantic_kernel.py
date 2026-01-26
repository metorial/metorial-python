"""Semantic Kernel (Microsoft) integration for Metorial."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def register_metorial_plugin(
  kernel: Any, session: "ProviderSession", plugin_name: str = "metorial"
) -> None:
  """
  Register Metorial tools as a Semantic Kernel plugin.

  Args:
      kernel: A Semantic Kernel instance
      session: An active Metorial ProviderSession
      plugin_name: Name for the plugin (default: "metorial")

  Example:
      ```python
      import semantic_kernel as sk
      from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
      from metorial import Metorial
      from metorial.integrations.semantic_kernel import register_metorial_plugin

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[deployment_id],
      ) as session:
          kernel = sk.Kernel()
          kernel.add_service(OpenAIChatCompletion(service_id="chat"))

          register_metorial_plugin(kernel, session)

          result = await kernel.invoke_prompt(
              "Search for Python news using the available tools"
          )
      ```
  """
  try:
    from semantic_kernel.functions import kernel_function  # noqa: F401
  except ImportError as e:
    raise ImportError(
      "Semantic Kernel is required for this integration. "
      "Install it with: pip install semantic-kernel"
    ) from e

  metorial_tools = session.get_tools()
  functions = []

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

    # Create a kernel function for each tool
    fn = _create_kernel_function(session, tool_name, tool_description, input_schema)
    functions.append((tool_name, fn))

  # Create a plugin class dynamically
  plugin = _create_plugin_class(plugin_name, functions, session)
  kernel.add_plugin(plugin, plugin_name)


def _create_kernel_function(
  session: "ProviderSession",
  tool_name: str,
  tool_description: str,
  input_schema: dict[str, Any],
) -> Any:
  """Create a Semantic Kernel function for a Metorial tool."""
  from semantic_kernel.functions import kernel_function

  properties = input_schema.get("properties", {})

  @kernel_function(name=tool_name, description=tool_description)
  async def tool_fn(**kwargs: Any) -> str:
    # Filter kwargs to only include valid parameters
    valid_kwargs = {k: v for k, v in kwargs.items() if k in properties}
    result = await session.call_tool(tool_name, valid_kwargs)

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

  return tool_fn


def _create_plugin_class(
  plugin_name: str,
  functions: list[tuple[str, Any]],
  session: "ProviderSession",
) -> Any:
  """Create a dynamic plugin class with the given functions."""

  class MetorialPlugin:
    def __init__(self):
      self._session = session
      for name, fn in functions:
        setattr(self, name, fn)

  MetorialPlugin.__name__ = f"{plugin_name}Plugin"
  return MetorialPlugin()
