import json
from typing import Any, Dict, Iterable, List


def build_google_tools(tool_mgr):
    """Build Google Gemini-compatible tool definitions from Metorial tools."""
    function_declarations = []
    for t in tool_mgr.get_tools():
        function_declarations.append({
            "name": t.name,
            "description": t.description or "",
            "parameters": t.get_parameters_as("openapi-3.0.0"),  # Google uses OpenAPI format
        })
    
    return [{
        "function_declarations": function_declarations
    }]


def _attr_or_key(obj, attr, key, default=None):
    """Helper to get attribute or key from object."""
    if hasattr(obj, attr):
        return getattr(obj, attr)
    if isinstance(obj, dict):
        return obj.get(key, default)
    return default


async def call_google_tools(tool_mgr, function_calls: List[Any]) -> Dict[str, Any]:
    """
    Call Metorial tools from Google function calls.
    Returns a user content with function responses.
    """
    parts = []

    for fc in function_calls:
        call_id = _attr_or_key(fc, "id", "id")
        call_name = _attr_or_key(fc, "name", "name")
        call_args = _attr_or_key(fc, "args", "args", {})

        try:
            # Handle args parsing  
            if isinstance(call_args, str):
                args = json.loads(call_args)
            else:
                args = call_args
        except Exception as e:
            parts.append({
                "function_response": {
                    "id": call_id,
                    "name": call_name,
                    "response": {
                        "error": f"[ERROR] Invalid JSON arguments: {e}"
                    }
                }
            })
            continue

        try:
            result = await tool_mgr.call_tool(call_name, args)
            if hasattr(result, "model_dump"):
                result = result.model_dump()
        except Exception as e:
            result = {"error": f"[ERROR] Tool call failed: {e!r}"}

        parts.append({
            "function_response": {
                "id": call_id,
                "name": call_name,
                "response": result
            }
        })

    return {
        "role": "user",
        "parts": parts,
    }


class MetorialGoogleSession:
    """Google Gemini-specific session wrapper for Metorial tools."""
    
    def __init__(self, tool_mgr):
        self._tool_mgr = tool_mgr
        self.tools = build_google_tools(tool_mgr)

    async def call_tools(self, function_calls: Iterable[Any]) -> Dict[str, Any]:
        """Execute function calls and return Google-compatible content."""
        return await call_google_tools(self._tool_mgr, function_calls)
