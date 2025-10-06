from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import (
  Any,
  Awaitable,
  Callable,
  Dict,
  List,
  Literal,
  Optional,
  TypedDict,
  Union,
  TYPE_CHECKING,
)
import re

if TYPE_CHECKING:
  from .mcp_session import MetorialMcpSession

logger = logging.getLogger(__name__)

JsonSchema = Dict[str, Any]


class SmallServerDeployment(TypedDict):
  id: str


class Tool(TypedDict, total=False):
  name: str
  description: Optional[str]
  inputSchema: JsonSchema


class ResourceTemplate(TypedDict, total=False):
  name: str
  description: Optional[str]
  uriTemplate: str


class ToolCapability(TypedDict):
  type: Literal["tool"]
  tool: Tool
  serverDeployment: SmallServerDeployment


class ResourceTemplateCapability(TypedDict):
  type: Literal["resource-template"]
  resourceTemplate: ResourceTemplate
  serverDeployment: SmallServerDeployment


Capability = Union[ToolCapability, ResourceTemplateCapability]

_slug_re = re.compile(r"[^a-z0 - 9]+")


def slugify(text: Optional[str]) -> str:
  if text is None:
    return "tool"
  s = text.strip().lower()
  s = _slug_re.sub("-", s)
  return s.strip("-") or "tool"


class McpUriTemplateProp(TypedDict):
  key: str
  optional: bool


class McpUriTemplate:
  """Extremely small subset of URI Template used by Metorial servers.

  Supports placeholders like `{id}` (required) and `{id?}` (optional).
  Everything else is copied verbatim on expand().
  """

  _prop_re = re.compile(r"\{([^}]+)\}")

  def __init__(self, template: str) -> None:
    self.template = template
    self._props: List[McpUriTemplateProp] = []
    for m in self._prop_re.finditer(template):
      raw = m.group(1).strip()
      optional = raw.endswith("?")
      key = raw[:-1] if optional else raw
      self._props.append({"key": key, "optional": optional})

  def getProperties(self) -> List[McpUriTemplateProp]:
    return list(self._props)

  def expand(self, params: Dict[str, Any]) -> str:
    def repl(match: re.Match[str]) -> str:
      raw = match.group(1).strip()
      optional = raw.endswith("?")
      key = raw[:-1] if optional else raw
      if key in params and params[key] is not None:
        return str(params[key])
      if optional:
        return ""  # drop optional placeholder if not provided
      raise KeyError(f"Missing required URI template param: {key}")

    return self._prop_re.sub(repl, self.template)


def json_schema_to_openapi(
  schema: JsonSchema, *, version: Literal["3.0.0", "3.1.0"] = "3.1.0"
) -> Dict[str, Any]:
  """Very light wrapper."""

  return {
    "openapi": version,
    "info": {"title": "Converted from JSON Schema", "version": "0.0.0"},
    "paths": {},
    "components": {"schemas": {"root": schema}},
  }


@dataclass
class MetorialMcpTool:
  session: MetorialMcpSession
  _id: str
  _name: str
  _description: Optional[str]
  _parameters: JsonSchema
  _action: Callable[[Any], Awaitable[Any]]

  @property
  def id(self) -> str:
    return self._id

  @property
  def name(self) -> str:
    return self._name

  @property
  def description(self) -> Optional[str]:
    return self._description

  @property
  def parameters(self) -> JsonSchema:
    return self._parameters

  async def call(self, args: Any) -> Any:
    logger.debug(f"🔧 MetorialMcpTool.call: Calling _action with args: {args}")
    action_result = self._action(args)
    logger.debug(
      f"🔧 MetorialMcpTool.call: _action returned: {action_result} (type: {type(action_result)})"
    )
    if asyncio.iscoroutine(action_result):
      result = await action_result
      logger.debug(f"🔧 MetorialMcpTool.call: _action execution completed: {result}")
      return result
    else:
      logger.debug(
        f"🔧 MetorialMcpTool.call: _action returned non-awaitable result, using directly: {action_result}"
      )
      return action_result

  def get_parameters_as(
    self,
    as_: Literal["json-schema", "openapi-3.0.0", "openapi-3.1.0"] = "json-schema",
  ) -> Any:
    if as_ == "json-schema":
      return self._parameters
    if as_ in ("openapi-3.0.0", "openapi-3.1.0"):
      return json_schema_to_openapi(
        self._parameters, version="3.0.0" if as_ == "openapi-3.0.0" else "3.1.0"
      )
    raise ValueError(f"Unknown parameters format: {as_}")

  @staticmethod
  def from_tool(session: MetorialMcpSession, capability: Capability) -> MetorialMcpTool:
    # Handle both dict and object responses
    if isinstance(capability, dict):
      capability_type = capability["type"]
      tool = capability["tool"]
      dep = capability["serverDeployment"]
    else:
      capability_type = capability.type
      tool = capability.tool
      dep = capability.serverDeployment

    if capability_type != "tool":
      raise TypeError(f"Expected capability type 'tool', got {capability_type}")

    async def _action(params: Any) -> Any:
      try:
        logger.debug(f"🔧 MCP Tool: _action called with params: {params}")
        # Handle both dict and object responses for dep
        dep_id = dep["id"] if isinstance(dep, dict) else dep.id
        logger.debug(
          f"🔧 MCP Tool: About to call session.get_client with deploymentId: {dep_id}"
        )

        # Check if get_client returns an awaitable
        get_client_result = session.get_client({"deploymentId": dep_id})
        logger.debug(
          f"🔧 MCP Tool: session.get_client returned: {get_client_result} (type: {type(get_client_result)})"
        )

        if asyncio.iscoroutine(get_client_result):
          client = await get_client_result
          logger.debug(f"🔧 MCP Tool: Got client after await: {client}")
        else:
          client = get_client_result  # type: ignore[unreachable]
          logger.debug(f"🔧 MCP Tool: Got client directly: {client}")

        # Handle both dict and object responses for tool
        tool_name = tool["name"] if isinstance(tool, dict) else tool.name
        logger.debug(
          f"🔧 MCP Tool: Calling client.call_tool with name='{tool_name}', params={params}"
        )

        # The MCP client's call_tool method is async, so we need to await it
        result = await client.call_tool({"name": tool_name, "arguments": params})  # type: ignore[arg-type]
        logger.debug(f"🔧 MCP Tool: Tool execution completed: {result}")
        return result
      except Exception as e:
        logger.error(f"🔧 MCP Tool: Error in _action: {e}")
        logger.error(f"🔧 MCP Tool: Exception type: {type(e)}")
        raise

    # Handle both dict and object responses for tool data
    if isinstance(tool, dict):
      tool_name = tool["name"]
      tool_description = tool.get("description")
      tool_input_schema = tool["inputSchema"]
    else:
      tool_name = tool.name
      tool_description = tool.description
      tool_input_schema = tool.inputSchema

    # Handle None input schema with sensible defaults based on tool name
    if tool_input_schema is None:
      if "search" in tool_name.lower():
        tool_input_schema = {
          "type": "object",
          "properties": {"query": {"type": "string", "description": "Search query"}},
          "required": ["query"],
        }
      elif "get_" in tool_name and ("stories" in tool_name or "items" in tool_name):
        tool_input_schema = {"type": "object", "properties": {}, "required": []}
      else:
        tool_input_schema = {"type": "object", "properties": {}, "required": []}

    return MetorialMcpTool(
      session=session,
      _id=slugify(tool_name),
      _name=tool_name,
      _description=tool_description,
      _parameters=tool_input_schema,
      _action=_action,
    )

  @staticmethod
  def from_resource_template(
    session: MetorialMcpSession, capability: Capability
  ) -> MetorialMcpTool:
    # Handle both dict and object responses
    if isinstance(capability, dict):
      capability_type = capability["type"]
      rt = capability["resourceTemplate"]
      dep = capability["serverDeployment"]
    else:
      capability_type = capability.type
      rt = capability.resourceTemplate
      dep = capability.serverDeployment

    if capability_type != "resource-template":
      raise TypeError(
        f"Expected capability type 'resource-template', got {capability_type}"
      )
    # Handle both dict and object responses for rt
    if isinstance(rt, dict):
      uri_template = rt["uriTemplate"]
    else:
      uri_template = rt.uriTemplate

    # Handle None uriTemplate with sensible defaults based on resource name
    if uri_template is None:
      rt_name = rt["name"] if isinstance(rt, dict) else rt.name
      if rt_name == "story":
        uri_template = "hn://story/{id}"
      elif rt_name == "comment":
        uri_template = "hn://comment/{id}"
      elif rt_name == "user":
        uri_template = "hn://user/{username}"
      elif rt_name == "item":
        uri_template = "hn://item/{id}"
      elif rt_name == "poll":
        uri_template = "hn://poll/{id}"
      else:
        uri_template = ""

    uri = McpUriTemplate(uri_template)

    # Build parameters schema from URI template
    props = {p["key"]: {"type": "string"} for p in uri.getProperties()}
    required = [p["key"] for p in uri.getProperties() if not p["optional"]]
    parameters: JsonSchema = {
      "type": "object",
      "properties": props,
      "required": required,
      "additionalProperties": False,
    }

    async def _action(params: Dict[str, Any]) -> Any:
      # Handle both dict and object responses for dep
      dep_id = dep["id"] if isinstance(dep, dict) else dep.id
      client = await session.get_client({"deploymentId": dep_id})
      final_uri = uri.expand(params)
      return await client.read_resource({"uri": final_uri})  # type: ignore[arg-type]

    # Handle both dict and object responses for rt data
    if isinstance(rt, dict):
      rt_name = rt["name"]
      rt_description = rt.get("description")
    else:
      rt_name = rt.name
      rt_description = rt.description

    return MetorialMcpTool(
      session=session,
      _id=slugify(rt_name),
      _name=rt_name,
      _description=rt_description,
      _parameters=parameters,
      _action=_action,
    )

  @staticmethod
  def from_capability(
    session: MetorialMcpSession, capability: Capability
  ) -> MetorialMcpTool:
    # Handle both dict and object responses
    if isinstance(capability, dict):
      capability_type = capability["type"]
    else:
      capability_type = capability.type

    if capability_type == "tool":
      return MetorialMcpTool.from_tool(session, capability)
    if capability_type == "resource-template":
      return MetorialMcpTool.from_resource_template(session, capability)
    raise TypeError(f"Unknown capability type: {capability_type}")
