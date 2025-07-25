from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Dict, List, Literal, Optional, TypedDict, Union
import re

# ---------------------------------------------------------------------------
# Types 
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Helpers: slugify + URI template parser
# ---------------------------------------------------------------------------

_slug_re = re.compile(r"[^a-z0-9]+")

def slugify(text: str) -> str:
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


# ---------------------------------------------------------------------------
# JSON Schema -> OpenAPI stub
# ---------------------------------------------------------------------------

def json_schema_to_openapi(schema: JsonSchema, *, version: Literal["3.0.0", "3.1.0"] = "3.1.0") -> Dict[str, Any]:
    """Very light wrapper.

    If you need real conversion, install a lib or port your TS converter.
    For now we just embed the schema under `schema` (valid in OpenAPI 3 as a
    parameter or requestBody schema). Adjust to your use case.
    """
    return {
        "openapi": version,
        "info": {"title": "Converted from JSON Schema", "version": "0.0.0"},
        "paths": {},
        "components": {"schemas": {"root": schema}},
    }


# ---------------------------------------------------------------------------
# MetorialMcpTool class
# ---------------------------------------------------------------------------

@dataclass
class MetorialMcpTool:
    session: "MetorialMcpSession"
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

    # ---- behavior ----
    async def call(self, args: Any) -> Any:
        return await self._action(args)

    def get_parameters_as(
        self,
        as_: Literal["json-schema", "openapi-3.0.0", "openapi-3.1.0"] = "json-schema",
    ) -> Any:
        if as_ == "json-schema":
            return self._parameters
        if as_ in ("openapi-3.0.0", "openapi-3.1.0"):
            return json_schema_to_openapi(self._parameters, version="3.0.0" if as_ == "openapi-3.0.0" else "3.1.0")
        raise ValueError(f"Unknown parameters format: {as_}")

    # ---- factories ----
    @staticmethod
    def from_tool(session: "MetorialMcpSession", capability: Capability) -> "MetorialMcpTool":
        if capability["type"] != "tool":
            raise TypeError(f"Expected capability type 'tool', got {capability['type']}")

        tool = capability["tool"]
        dep = capability["serverDeployment"]

        async def _action(params: Any) -> Any:
            client = await session.get_client({"deploymentId": dep["id"]})
            return await client.call_tool({"name": tool["name"], "arguments": params})

        return MetorialMcpTool(
            session=session,
            _id=slugify(tool["name"]),
            _name=tool["name"],
            _description=tool.get("description"),
            _parameters=tool["inputSchema"],
            _action=_action,
        )

    @staticmethod
    def from_resource_template(session: "MetorialMcpSession", capability: Capability) -> "MetorialMcpTool":
        if capability["type"] != "resource-template":
            raise TypeError(
                f"Expected capability type 'resource-template', got {capability['type']}"
            )

        rt = capability["resourceTemplate"]
        dep = capability["serverDeployment"]
        uri = McpUriTemplate(rt["uriTemplate"])

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
            client = await session.get_client({"deploymentId": dep["id"]})
            final_uri = uri.expand(params)
            return await client.read_resource({"uri": final_uri})

        return MetorialMcpTool(
            session=session,
            _id=slugify(rt["name"]),
            _name=rt["name"],
            _description=rt.get("description"),
            _parameters=parameters,
            _action=_action,
        )

    @staticmethod
    def from_capability(session: "MetorialMcpSession", capability: Capability) -> "MetorialMcpTool":
        if capability["type"] == "tool":
            return MetorialMcpTool.from_tool(session, capability)
        if capability["type"] == "resource-template":
            return MetorialMcpTool.from_resource_template(session, capability)
        raise TypeError(f"Unknown capability type: {capability}")
