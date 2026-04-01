"""Shared helpers for framework integration modules."""

from __future__ import annotations

import asyncio
import inspect
import json
from collections.abc import Callable
from typing import Any


def json_type_to_python(json_type: str) -> type[Any]:
  """Convert a JSON schema type to a Python type."""
  type_map: dict[str, type[Any]] = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "array": list,
    "object": dict,
  }
  return type_map.get(json_type, str)


def normalize_tool_result(result: Any) -> Any:
  """Normalize SDK objects into plain Python data."""
  if hasattr(result, "model_dump"):
    return result.model_dump()
  return result


def serialize_tool_result(result: Any) -> str:
  """Serialize a tool result as JSON text."""
  return json.dumps(normalize_tool_result(result), ensure_ascii=False, default=str)


def apply_tool_signature(
  fn: Callable[..., Any],
  *,
  name: str,
  description: str,
  schema: dict[str, Any],
  return_annotation: Any,
  use_optional_union: bool = True,
) -> None:
  """Attach a tool-like signature/docstring to a callable."""
  properties = schema.get("properties", {})
  required = set(schema.get("required", []))

  annotations: dict[str, Any] = {}
  parameters: list[inspect.Parameter] = []
  for prop_name, prop_schema in properties.items():
    base_type = json_type_to_python(prop_schema.get("type", "string"))
    annotation = (
      base_type if prop_name in required or not use_optional_union else base_type | None
    )
    annotations[prop_name] = annotation
    parameters.append(
      inspect.Parameter(
        prop_name,
        inspect.Parameter.KEYWORD_ONLY,
        annotation=annotation,
        default=inspect.Parameter.empty if prop_name in required else None,
      )
    )

  annotations["return"] = return_annotation
  fn.__name__ = name
  fn.__doc__ = description
  fn.__annotations__ = annotations
  fn.__signature__ = inspect.Signature(
    parameters=parameters,
    return_annotation=return_annotation,
  )


def run_coro_on_loop(
  loop: asyncio.AbstractEventLoop,
  coro_factory: Callable[[], Any],
  *,
  timeout: float = 120.0,
) -> Any:
  """Run a coroutine on the owning session loop from sync code."""
  if loop.is_closed():
    raise RuntimeError("Metorial session loop is closed.")

  try:
    current_loop = asyncio.get_running_loop()
  except RuntimeError:
    current_loop = None

  if current_loop is loop:
    raise RuntimeError(
      "Synchronous tool execution on the active session loop is not supported. "
      "Use the framework's async execution path instead."
    )

  future = asyncio.run_coroutine_threadsafe(coro_factory(), loop)
  return future.result(timeout=timeout)
