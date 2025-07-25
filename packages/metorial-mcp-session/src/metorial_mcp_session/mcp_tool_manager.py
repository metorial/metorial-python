from __future__ import annotations

from typing import Dict, List, Optional, Iterable, Any, TYPE_CHECKING

if TYPE_CHECKING:  # only for hints, avoids runtime import
    from .mcp_session import MetorialMcpSession
    
from .mcp_tool import MetorialMcpTool, Capability


class MetorialMcpToolManager:
    def __init__(self, session: MetorialMcpSession, tools: Iterable[MetorialMcpTool]) -> None:
        self._session = session
        self._tools_by_key: Dict[str, MetorialMcpTool] = {}
        for tool in tools:
            # Prefer last-wins if duplicates collide
            self._tools_by_key[tool.id] = tool
            self._tools_by_key[tool.name] = tool

    # --------- factories ---------

    @classmethod
    async def from_capabilities(
        cls,
        session: MetorialMcpSession,
        capabilities: List[Capability],
    ) -> "MetorialMcpToolManager":
        tools = [MetorialMcpTool.from_capability(session, cap) for cap in capabilities]
        return cls(session, tools)

    # --------- accessors ---------

    def get_tool(self, id_or_name: str) -> Optional[MetorialMcpTool]:
        return self._tools_by_key.get(id_or_name)

    def get_tools(self) -> List[MetorialMcpTool]:
        # unique instances (id and name point to same object)
        seen = set()
        out: List[MetorialMcpTool] = []
        for tool in self._tools_by_key.values():
            if id(tool) not in seen:
                seen.add(id(tool))
                out.append(tool)
        return out

    # --------- actions ---------

    async def call_tool(self, id_or_name: str, args: Any) -> Any:
        tool = self.get_tool(id_or_name)
        if tool is None:
            raise KeyError(f"Tool not found: {id_or_name}")
        return await tool.call(args)
