"""Regression tests for the Autogen integration.

These focus on C-10a: a hostile or compromised MCP server must not be able to
execute arbitrary Python when ``create_autogen_tools`` builds tool wrappers from
server-supplied tool metadata (name, description, JSON-schema property names).

The ``autogen`` integration module has no runtime dependency on the rest of the
``metorial`` package (its only ``metorial`` import is guarded by
``TYPE_CHECKING``), so it is loaded standalone here. This keeps the tests
independent of unrelated top-level import concerns and of whether ``autogen`` is
installed.
"""

from __future__ import annotations

import importlib.util
import inspect
import json
import keyword
from pathlib import Path
from typing import Any

import pytest

_MODULE_PATH = (
  Path(__file__).resolve().parents[1]
  / "src"
  / "metorial"
  / "integrations"
  / "autogen.py"
)


def _load_autogen_module():
  """Import ``metorial/integrations/autogen.py`` in isolation."""
  spec = importlib.util.spec_from_file_location(
    "metorial_autogen_under_test", _MODULE_PATH
  )
  assert spec is not None and spec.loader is not None
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module


@pytest.fixture
def autogen_mod():
  """A freshly loaded module so ``FunctionTool`` overrides never leak."""
  return _load_autogen_module()


class RecordingFunctionTool:
  """Stand-in for ``autogen_core.tools.FunctionTool`` that records its inputs."""

  def __init__(self, func, description=None, name=None):
    self.func = func
    self.description = description
    self.name = name


class StubTool:
  """Minimal stand-in for ``MetorialMcpTool``."""

  def __init__(self, name: str, description: str | None, schema: Any):
    self.name = name
    self.description = description
    self._schema = schema

  def get_parameters_as(self, fmt: str) -> Any:
    assert fmt == "json-schema"
    return self._schema


class StubToolManager:
  def __init__(self, tools: list[StubTool]):
    self._tools = tools
    self.calls: list[tuple[str, dict]] = []

  def get_tools(self) -> list[StubTool]:
    return self._tools

  async def execute_tool(self, name: str, args: dict) -> dict:
    self.calls.append((name, dict(args)))
    return {"tool": name, "args": args}


class StubSession:
  def __init__(self, tool_manager: StubToolManager | None):
    self.tool_manager = tool_manager


def _build(autogen_mod, tools, fake=RecordingFunctionTool):
  autogen_mod.FunctionTool = fake
  manager = StubToolManager(tools)
  session = StubSession(manager)
  built = autogen_mod.create_autogen_tools(session)
  return manager, built


def test_malicious_description_is_not_executed(autogen_mod):
  """A description that closes the docstring and adds code must not run."""
  import builtins

  sentinel = "_metorial_autogen_rce_sentinel"
  if hasattr(builtins, sentinel):
    delattr(builtins, sentinel)

  payload = (
    "Innocent looking tool.'''\n"
    "import builtins\n"
    f"setattr(builtins, {sentinel!r}, True)\n"
    "'''"
  )
  tool = StubTool("safe_tool", payload, {"type": "object", "properties": {}})

  try:
    _, built = _build(autogen_mod, [tool])
    assert not hasattr(builtins, sentinel), "server description was executed"
    assert len(built) == 1
    # The description is carried as data only, never parsed.
    assert built[0].description == payload
    assert built[0].func.__doc__ == payload
  finally:
    if hasattr(builtins, sentinel):
      delattr(builtins, sentinel)


def test_tool_names_are_sanitized_or_skipped(autogen_mod):
  """Injection characters in a name are neutralized; unusable names skipped."""
  tools = [
    # Injection payload collapses to a plain identifier and is kept, harmless.
    StubTool("evil'''\nimport os\n#", "d", {"properties": {}}),
    StubTool("good-tool", "d", {"properties": {}}),  # -> good_tool
    StubTool("1bad", "d", {"properties": {}}),  # leading digit -> skipped
    StubTool("class", "d", {"properties": {}}),  # keyword -> skipped
    StubTool("", "d", {"properties": {}}),  # empty -> skipped
  ]

  _, built = _build(autogen_mod, tools)
  names = {t.name for t in built}

  assert "good_tool" in names
  assert "1bad" not in names
  assert "class" not in names
  assert "" not in names
  assert len(built) == 2
  # Every exposed name is a real, safe Python identifier.
  for name in names:
    assert name.isidentifier()
    assert not keyword.iskeyword(name)


def test_invalid_property_names_skip_tool(autogen_mod):
  """Non-identifier / keyword / reserved property names skip the whole tool."""
  tools = [
    StubTool("bad0", "d", {"properties": {"a): pass\n#": {"type": "string"}}}),
    StubTool("bad1", "d", {"properties": {"class": {"type": "string"}}}),
    StubTool("bad2", "d", {"properties": {"cancellation_token": {"type": "string"}}}),
    StubTool("bad3", "d", {"properties": {"123": {"type": "string"}}}),
    StubTool("good_tool", "d", {"properties": {"q": {"type": "string"}}}),
  ]

  _, built = _build(autogen_mod, tools)
  assert {t.name for t in built} == {"good_tool"}


async def test_normal_tool_signature_and_execution(autogen_mod):
  """A well-formed tool yields the expected signature and executes correctly."""
  schema = {
    "type": "object",
    "properties": {
      "q": {"type": "string"},
      "limit": {"type": "integer"},
    },
    "required": ["q"],
  }
  tool = StubTool("list-issues", "List issues.", schema)

  manager, built = _build(autogen_mod, [tool])
  assert len(built) == 1
  ft = built[0]
  assert ft.name == "list_issues"

  sig = inspect.signature(ft.func)
  assert list(sig.parameters) == ["q", "limit"]

  q = sig.parameters["q"]
  assert q.kind is inspect.Parameter.KEYWORD_ONLY
  assert q.default is inspect.Parameter.empty
  assert q.annotation is str

  limit = sig.parameters["limit"]
  assert limit.kind is inspect.Parameter.KEYWORD_ONLY
  assert limit.default is None
  assert limit.annotation == (int | None)

  assert sig.return_annotation is str

  # None-valued optionals are dropped before hitting the executor.
  out = await ft.func(q="hello", limit=None)
  assert manager.calls == [("list-issues", {"q": "hello"})]
  assert json.loads(out) == {"tool": "list-issues", "args": {"q": "hello"}}

  manager.calls.clear()
  await ft.func(q="hi", limit=5)
  assert manager.calls == [("list-issues", {"q": "hi", "limit": 5})]


def test_union_list_schema_type_does_not_abort_build(autogen_mod):
  """A JSON-schema "type" list (e.g. ["string", "null"]) must not crash the loop.

  A single nullable field previously raised TypeError (unhashable list key) and
  dropped every tool; it should map to the concrete type and leave other tools
  intact.
  """
  nullable = StubTool(
    "nullable-tool",
    "Has a nullable field.",
    {
      "type": "object",
      "properties": {
        "name": {"type": ["string", "null"]},
        "count": {"type": ["integer", "null"]},
        "weird": {"type": []},  # degenerate: no concrete type -> falls back to str
      },
      "required": ["name"],
    },
  )
  plain = StubTool("plain-tool", "Plain.", {"properties": {"q": {"type": "string"}}})

  _, built = _build(autogen_mod, [nullable, plain])

  # Both tools survive; the nullable field did not abort the whole build.
  names = {t.name for t in built}
  assert names == {"nullable_tool", "plain_tool"}

  ft = next(t for t in built if t.name == "nullable_tool")
  sig = inspect.signature(ft.func)
  # "string" chosen from ["string", "null"]; required -> no default.
  assert sig.parameters["name"].annotation is str
  assert sig.parameters["name"].default is inspect.Parameter.empty
  # "integer" chosen from ["integer", "null"]; optional -> int | None, default None.
  assert sig.parameters["count"].annotation == (int | None)
  assert sig.parameters["count"].default is None
  # Empty type list -> str fallback.
  assert sig.parameters["weird"].annotation == (str | None)


def test_none_tool_manager_returns_empty(autogen_mod):
  autogen_mod.FunctionTool = RecordingFunctionTool
  assert autogen_mod.create_autogen_tools(StubSession(None)) == []


def test_missing_autogen_dependency_raises(autogen_mod):
  autogen_mod.FunctionTool = None
  with pytest.raises(ImportError):
    autogen_mod.create_autogen_tools(StubSession(StubToolManager([])))


async def test_real_functiontool_reads_signature_and_runs():
  """With autogen installed, a real FunctionTool introspects and runs the tool.

  This is the end-to-end guard against the RCE fix regressing: autogen's
  FunctionTool resolves parameter types via ``typing.get_type_hints`` (reading
  ``__annotations__``) and builds a pydantic args model, so the generated
  wrapper must expose both a matching ``__signature__`` and ``__annotations__``.
  """
  pytest.importorskip("autogen_core")
  from autogen_core import CancellationToken

  autogen_mod = _load_autogen_module()
  schema = {
    "type": "object",
    "properties": {
      "q": {"type": "string"},
      "n": {"type": "integer"},
    },
    "required": ["q"],
  }
  tool = StubTool("list-issues", "List issues.", schema)
  manager = StubToolManager([tool])
  built = autogen_mod.create_autogen_tools(StubSession(manager))

  assert len(built) == 1
  ft = built[0]

  params = ft.schema["parameters"]
  assert set(params["properties"]) == {"q", "n"}
  assert "q" in params.get("required", [])
  assert ft.description == "List issues."

  # Execute through autogen end-to-end and confirm it reaches the executor.
  args_model = ft.args_type()(q="hello", n=3)
  result = await ft.run(args_model, CancellationToken())
  assert manager.calls == [("list-issues", {"q": "hello", "n": 3})]
  assert json.loads(result) == {
    "tool": "list-issues",
    "args": {"q": "hello", "n": 3},
  }
