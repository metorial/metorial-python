"""
Shared thread pool executor for synchronous operations.

This module provides a lazily-initialized, shared ThreadPoolExecutor
to avoid creating a new executor for each sync operation.
"""

from __future__ import annotations

import atexit
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
  from collections.abc import Callable

T = TypeVar("T")

# Module-level shared executor (lazily initialized)
_executor: ThreadPoolExecutor | None = None
_executor_max_workers: int = 4
_executor_lock = threading.Lock()


def get_executor(max_workers: int | None = None) -> ThreadPoolExecutor:
  """Get the shared thread pool executor, creating it if needed.

  The executor is lazily initialized on first use and reused
  for all subsequent calls. Thread-safe via double-checked locking.

  Args:
      max_workers: Maximum number of worker threads. Only used
                  on first call when creating the executor.
                  Default is 4.

  Returns:
      The shared ThreadPoolExecutor instance
  """
  global _executor
  if _executor is None:
    with _executor_lock:
      if _executor is None:  # Double-check inside lock
        workers = max_workers if max_workers is not None else _executor_max_workers
        _executor = ThreadPoolExecutor(max_workers=workers)
        # Register cleanup at exit
        atexit.register(_shutdown_executor)
  return _executor


def run_sync(func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
  """Run a synchronous function in the shared thread pool.

  This is useful for running blocking operations without
  blocking the main thread.

  Args:
      func: The function to run
      *args: Positional arguments to pass to the function
      **kwargs: Keyword arguments to pass to the function

  Returns:
      The result of the function call
  """
  executor = get_executor()
  if kwargs:
    # ThreadPoolExecutor.submit doesn't support kwargs directly
    # so we need to wrap the call
    def wrapped() -> T:
      return func(*args, **kwargs)

    future = executor.submit(wrapped)
  else:
    future = executor.submit(func, *args)
  return future.result()


def _shutdown_executor() -> None:
  """Shutdown the shared executor gracefully."""
  global _executor
  if _executor is not None:
    _executor.shutdown(wait=False)
    _executor = None


def shutdown_executor(wait: bool = True) -> None:
  """Explicitly shutdown the shared executor.

  This can be called to clean up resources before exit.

  Args:
      wait: If True, wait for pending tasks to complete.
            If False, cancel pending tasks.
  """
  global _executor
  if _executor is not None:
    _executor.shutdown(wait=wait)
    _executor = None


__all__ = ["get_executor", "run_sync", "shutdown_executor"]
