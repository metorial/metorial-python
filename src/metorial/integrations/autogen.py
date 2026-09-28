"""Autogen integration for Metorial."""

from __future__ import annotations

import inspect
import json
import keyword
import logging
import re
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession

try:
  from autogen_core.tools import FunctionTool
except ImportError:
  FunctionTool = None

logger = logging.getLogger(__name__)

# A valid Python identifier of at most 64 characters. Server-supplied tool and
# parameter names are checked against this before they are ever used to build a
# function signature.
_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")

# Parameter names that autogen's FunctionTool injects itself; a tool may not
# declare them as parameters.
_RESERVED_PARAMS = frozenset({"cancellation_token"})


def _build_tool_fn(
  tool_manager: Any,
  tool_name: str,
  func_name: str,
  description: str,
  params: list[inspect.Parameter],
) -> Callable[..., Any]:
  """
  Build an async callable that autogen's FunctionTool can introspect.

  The function is created as a real closure and given an explicit
  ``inspect.Signature`` instead of being compiled from a source string. All
  server-controlled values (``tool_name``, ``description``, parameter names)
  are treated as data only and are never parsed or executed.
  """

  async def _invoke(**kwargs: Any) -> str:
    args = {k: v for k, v in kwargs.items() if v is not None}
    try:
      result = await tool_manager.execute_tool(tool_name, args)
      if hasattr(result, "model_dump"):
        result = result.model_dump()
      return json.dumps(result, ensure_ascii=False, default=str)
    except Exception as e:
      return json.dumps({"error": str(e)}, ensure_ascii=False)

  _invoke.__signature__ = inspect.Signature(params, return_annotation=str)
  # autogen's FunctionTool resolves parameter types via typing.get_type_hints,
  # which reads __annotations__ rather than __signature__, so keep the two in
  # sync. Real type objects (not strings) are used so no evaluation is needed.
  annotations: dict[str, Any] = {p.name: p.annotation for p in params}
  annotations["return"] = str
  _invoke.__annotations__ = annotations
  _invoke.__name__ = func_name
  _invoke.__qualname__ = func_name
  _invoke.__doc__ = description
  return _invoke


def create_autogen_tools(session: ProviderSession) -> list[Any]:
  """
  Convert Metorial session tools to Autogen FunctionTool objects.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of Autogen FunctionTool objects

  Example:
      ```python
      from autogen_agentchat.agents import AssistantAgent
      from autogen_ext.models.anthropic import AnthropicChatCompletionClient
      from metorial import Metorial
      from metorial.integrations.autogen import create_autogen_tools

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="anthropic",
          providers=[{"session_template_id": "deployment-id"}],
      ) as session:
          tools = create_autogen_tools(session)

          model_client = AnthropicChatCompletionClient(model="claude-sonnet-4-20250514")
          assistant = AssistantAgent(
              name="assistant",
              model_client=model_client,
              tools=tools,
          )
      ```
  """
  if FunctionTool is None:
    raise ImportError(
      "autogen-core is required for Autogen integration. "
      "Install it with: pip install autogen-agentchat autogen-ext"
    )

  tools = []
  tool_manager = session.tool_manager

  if tool_manager is None:
    return tools

  # JSON-schema type -> Python annotation used only to describe the signature.
  type_map = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "array": list,
    "object": dict,
  }

  seen_names: set[str] = set()

  for tool in tool_manager.get_tools():
    tool_name = tool.name
    tool_description = tool.description or f"Tool: {tool_name}"

    # Derive a safe Python identifier for the exposed function name. The
    # original tool_name is what we hand back to execute_tool; it is only ever
    # data. Hyphens (common in MCP tool names like "list-issues") and other
    # non-identifier characters are collapsed to underscores.
    func_name = re.sub(r"[^A-Za-z0-9_]", "_", tool_name)
    if not _IDENT_RE.match(func_name) or keyword.iskeyword(func_name):
      logger.warning(
        "Skipping tool with unusable name %r (sanitized to %r)",
        tool_name,
        func_name,
      )
      continue
    if func_name in seen_names:
      logger.warning(
        "Skipping tool %r: duplicate sanitized function name %r",
        tool_name,
        func_name,
      )
      continue

    schema = tool.get_parameters_as("json-schema") or {}
    properties = schema.get("properties")
    if not isinstance(properties, dict):
      properties = {}
    raw_required = schema.get("required")
    required_params = (
      {r for r in raw_required if isinstance(r, str)}
      if isinstance(raw_required, list)
      else set()
    )

    # Validate every parameter name before it becomes part of a signature. A
    # non-identifier, keyword or reserved name means we skip the whole tool
    # rather than risk an exception (or, historically, code injection).
    invalid_prop = next(
      (
        name
        for name in properties
        if not isinstance(name, str)
        or not _IDENT_RE.match(name)
        or keyword.iskeyword(name)
        or name in _RESERVED_PARAMS
      ),
      None,
    )
    if invalid_prop is not None:
      logger.warning(
        "Skipping tool %r: invalid parameter name %r", tool_name, invalid_prop
      )
      continue

    # Sort: required params first, optional params after.
    required_props = [(n, s) for n, s in properties.items() if n in required_params]
    optional_props = [(n, s) for n, s in properties.items() if n not in required_params]

    params = []
    for prop_name, prop_schema in required_props + optional_props:
      if not isinstance(prop_schema, dict):
        prop_schema = {}
      # JSON Schema "type" may be a string or a list (e.g. ["string", "null"]
      # for a nullable field). Normalize to a single hashable key before the
      # lookup so a list type never raises TypeError and aborts the build.
      json_type = prop_schema.get("type")
      if isinstance(json_type, list):
        json_type = next(
          (t for t in json_type if isinstance(t, str) and t != "null"), None
        )
      if not isinstance(json_type, str):
        json_type = None
      py_type = type_map.get(json_type, str)
      if prop_name in required_params:
        params.append(
          inspect.Parameter(
            prop_name,
            inspect.Parameter.KEYWORD_ONLY,
            annotation=py_type,
          )
        )
      else:
        params.append(
          inspect.Parameter(
            prop_name,
            inspect.Parameter.KEYWORD_ONLY,
            annotation=py_type | None,
            default=None,
          )
        )

    fn = _build_tool_fn(tool_manager, tool_name, func_name, tool_description, params)

    autogen_tool = FunctionTool(fn, description=tool_description, name=func_name)
    tools.append(autogen_tool)
    seen_names.add(func_name)

  return tools


def get_autogen_tool_executor(session: ProviderSession) -> dict[str, Callable]:
  """
  Get a function map for legacy Autogen tool execution.

  .. deprecated::
      Use create_autogen_tools() with the new Autogen API instead.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      Dictionary mapping tool names to executor functions
  """
  import asyncio

  metorial_tools = session.get_tools()
  function_map: dict[str, Callable] = {}

  for tool in metorial_tools:
    # Handle OpenAI-style format (type: function, function: {name, ...})
    if "function" in tool:
      tool_name = tool["function"].get("name", "")
    else:
      tool_name = tool.get("name", "")

    def make_executor(name: str) -> Callable:
      def executor(**kwargs: Any) -> str:
        async def call():
          result = await session.call_tool(name, kwargs)
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

    function_map[tool_name] = make_executor(tool_name)

  return function_map
