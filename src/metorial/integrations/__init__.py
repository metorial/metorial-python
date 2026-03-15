"""
Metorial integrations for popular Python agent frameworks.

Available integrations:
- langchain: LangChain tool integration
- langgraph: LangGraph tool integration
- openai_agents: OpenAI Agents SDK integration
- pydantic_ai: PydanticAI tool integration
- llamaindex: LlamaIndex tool integration
- autogen: Microsoft Autogen integration
- haystack: deepset Haystack integration
"""

from __future__ import annotations

import re
from typing import Any


def _sanitize_tool_name(name: str) -> str:
  """Sanitize tool name to be a valid Python identifier (replace hyphens, etc.)."""
  return re.sub(r"[^a-zA-Z0-9_]", "_", name)


def _sanitize_schema(schema: dict[str, Any]) -> dict[str, Any]:
  """Remove unsupported JSON schema fields that some providers reject (e.g. 'format': 'uri')."""
  if not isinstance(schema, dict):
    return schema
  cleaned: dict[str, Any] = {}
  for k, v in schema.items():
    if k == "format":
      # Skip 'format' field - OpenAI rejects non-standard formats like 'uri'
      continue
    if isinstance(v, dict):
      cleaned[k] = _sanitize_schema(v)
    elif isinstance(v, list):
      cleaned[k] = [_sanitize_schema(i) if isinstance(i, dict) else i for i in v]
    else:
      cleaned[k] = v
  return cleaned


__all__ = [
  "langchain",
  "langgraph",
  "openai_agents",
  "pydantic_ai",
  "llamaindex",
  "autogen",
  "haystack",
]
