"""Turning tool results into the plain JSON handed to LLM providers."""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel


def normalize_tool_result(result: Any) -> Any:
  """Convert an MCP result model into plain JSON-compatible data.

  Pydantic models are dumped by alias so the keys match the MCP wire format
  (``structuredContent``, ``isError``, ``_meta``) regardless of whether the
  installed MCP SDK names its attributes in camelCase (1.x) or snake_case (2.x).
  """
  if isinstance(result, BaseModel):
    return result.model_dump(by_alias=True, mode="json", exclude_none=True)
  if hasattr(result, "model_dump"):
    return result.model_dump()
  return result


def serialize_tool_result(result: Any) -> str:
  return json.dumps(normalize_tool_result(result), ensure_ascii=False, default=str)
