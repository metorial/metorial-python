from __future__ import annotations

from typing import Any


class SandboxAccessError(Exception):
  def __init__(
    self,
    code: str,
    message: str | None = None,
    *,
    retryable: bool = False,
    path: str | None = None,
  ) -> None:
    super().__init__(message or code.replace("_", " "))
    self.code = code
    self.retryable = retryable
    self.path = path


class SandboxCommandError(SandboxAccessError):
  pass


def closed_error() -> SandboxAccessError:
  return SandboxAccessError("closed", "The sandbox connection was closed.")


def server_error(
  raw: Any, error_class: type[SandboxAccessError] = SandboxAccessError
) -> SandboxAccessError:
  data = raw if isinstance(raw, dict) else {}
  code = data.get("code")
  message = data.get("message")
  path = data.get("path")

  return error_class(
    code if isinstance(code, str) else "unknown",
    message if isinstance(message, str) else None,
    retryable=data.get("retryable") is True,
    path=path if isinstance(path, str) else None,
  )


_CLOSE_REASONS = {
  "machine_paused": "The machine paused, so this connection was closed.",
  "machine_restarting": "The machine is restarting.",
  "machine_terminated": "The machine was terminated.",
  "idle_timeout": "This connection was closed after being idle.",
}


def describe_socket_close(code: int | None, reason: str) -> SandboxAccessError:
  if code == 4401:
    return SandboxAccessError(
      "unauthorized", "Access to the machine was rejected.", retryable=True
    )
  if code == 4404:
    return SandboxAccessError("not_found", "This machine could not be found.")
  if code == 4410:
    return SandboxAccessError(
      "machine_terminated", _CLOSE_REASONS["machine_terminated"]
    )
  if code == 4429:
    return SandboxAccessError(
      "rate_limited", "Too many connections to the machine.", retryable=True
    )
  if code == 4503:
    if reason == "machine_failed":
      return SandboxAccessError("machine_failed", "The machine has failed.")
    return SandboxAccessError(
      "machine_unavailable", "The machine is not available.", retryable=True
    )
  if code == 1012:
    kind = (
      reason
      if reason in ("machine_terminated", "machine_restarting")
      else "machine_paused"
    )
    return SandboxAccessError(
      kind, _CLOSE_REASONS[kind], retryable=kind != "machine_terminated"
    )
  if code == 1000 and reason == "idle_timeout":
    return SandboxAccessError(
      "idle_timeout", _CLOSE_REASONS["idle_timeout"], retryable=True
    )

  return SandboxAccessError(
    "disconnected", "The connection to the machine was lost.", retryable=True
  )
