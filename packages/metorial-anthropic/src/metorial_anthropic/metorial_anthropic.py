import json
from typing import Any, Dict, Iterable, List


def build_anthropic_tools(tool_mgr):
    """Build Anthropic-compatible tool definitions from Metorial tools."""
    tools = []
    for t in tool_mgr.get_tools():
        tools.append({
            "name": t.name,
            "description": t.description or "",
            "input_schema": t.get_parameters_as("json-schema"),
        })
    return tools


def _attr_or_key(obj, attr, key, default=None):
    """Helper to get attribute or key from object."""
    if hasattr(obj, attr):
        return getattr(obj, attr)
    if isinstance(obj, dict):
        return obj.get(key, default)
    return default


async def call_anthropic_tools(tool_mgr, tool_calls: List[Any]) -> Dict[str, Any]:
    """
    Call Metorial tools from Anthropic tool use blocks.
    Returns a user message with tool results.
    """
    tool_results = []

    for tc in tool_calls:
        tool_use_id = _attr_or_key(tc, "id", "id")
        tool_name = _attr_or_key(tc, "name", "name")
        tool_input = _attr_or_key(tc, "input", "input", {})

        try:
            # Handle input parsing
            if isinstance(tool_input, str):
                args = json.loads(tool_input)
            else:
                args = tool_input
        except Exception as e:
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_use_id,
                "content": f"[ERROR] Invalid JSON arguments: {e}",
            })
            continue

        try:
            result = await tool_mgr.call_tool(tool_name, args)
            if hasattr(result, "model_dump"):
                result = result.model_dump()
            content = json.dumps(result, ensure_ascii=False, default=str)
        except Exception as e:
            content = f"[ERROR] Tool call failed: {e!r}"

        tool_results.append({
            "type": "tool_result",
            "tool_use_id": tool_use_id,
            "content": content,
        })

    return {
        "role": "user",
        "content": tool_results,
    }


class MetorialAnthropicSession:
    """Anthropic-specific session wrapper for Metorial tools."""
    
    def __init__(self, tool_mgr):
        self._tool_mgr = tool_mgr
        self.tools = build_anthropic_tools(tool_mgr)

    async def call_tools(self, tool_calls: Iterable[Any]) -> Dict[str, Any]:
        """Execute tool calls and return Anthropic-compatible message."""
        return await call_anthropic_tools(self._tool_mgr, tool_calls)
