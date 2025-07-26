import json
from typing import Any, Dict, Iterable, List


def build_mistral_tools(tool_mgr):
    """Build Mistral-compatible tool definitions from Metorial tools."""
    tools = []
    for t in tool_mgr.get_tools():
        tools.append({
            "type": "function",
            "function": {
                "name": t.name,
                "description": t.description or "",
                "parameters": t.get_parameters_as("json-schema"),
                "strict": True,
            },
        })
    return tools


def _attr_or_key(obj, attr, key, default=None):
    """Helper to get attribute or key from object."""
    if hasattr(obj, attr):
        return getattr(obj, attr)
    if isinstance(obj, dict):
        return obj.get(key, default)
    return default


async def call_mistral_tools(tool_mgr, tool_calls: List[Any]) -> List[Dict[str, Any]]:
    """
    Call Metorial tools from Mistral tool calls.
    Returns a list of tool messages.
    """
    messages = []

    for tc in tool_calls:
        tool_call_id = _attr_or_key(tc, "id", "id")
        function_obj = _attr_or_key(tc, "function", "function", {})
        function_name = _attr_or_key(function_obj, "name", "name")
        function_args = _attr_or_key(function_obj, "arguments", "arguments", "{}")

        try:
            # Handle arguments parsing
            if isinstance(function_args, str):
                args = json.loads(function_args) if function_args.strip() else {}
            else:
                args = function_args
        except Exception as e:
            messages.append({
                "tool_call_id": tool_call_id,
                "role": "tool",
                "content": f"[ERROR] Invalid JSON arguments: {e}",
            })
            continue

        try:
            result = await tool_mgr.call_tool(function_name, args)
            if hasattr(result, "model_dump"):
                result = result.model_dump()
            content = json.dumps(result, ensure_ascii=False, default=str)
        except Exception as e:
            content = f"[ERROR] Tool call failed: {e!r}"

        messages.append({
            "tool_call_id": tool_call_id,
            "role": "tool",
            "content": content,
        })

    return messages


class MetorialMistralSession:
    """Mistral-specific session wrapper for Metorial tools."""
    
    def __init__(self, tool_mgr):
        self._tool_mgr = tool_mgr
        self.tools = build_mistral_tools(tool_mgr)

    async def call_tools(self, tool_calls: Iterable[Any]) -> List[Dict[str, Any]]:
        """Execute tool calls and return Mistral-compatible messages."""
        return await call_mistral_tools(self._tool_mgr, tool_calls)
