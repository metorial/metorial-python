"""
Tests for safe AsyncIO cleanup functionality.
Fast, deterministic tests to ensure proper resource cleanup without warnings.
"""

import asyncio
import logging
import warnings

import pytest

from metorial._safe_cleanup import (
  attach_noise_filters,
  drain_pending_tasks,
  install_warning_filters,
  quiet_asyncio_shutdown,
)


class TestWarningFilters:
  """Test warning filter installation"""

  def test_install_warning_filters(self):
    """Test that warning filters are installed correctly"""
    with warnings.catch_warnings(record=True) as caught_warnings:
      warnings.simplefilter("always")  # Capture all warnings

      install_warning_filters()

      # Try to trigger the specific warnings that should be filtered
      # These would normally generate RuntimeWarnings
      warnings.warn("generator didn't stop after athrow", RuntimeWarning, stacklevel=2)
      warnings.warn("Attempted to exit cancel scope", RuntimeWarning, stacklevel=2)
      warnings.warn(
        "an error occurred during closing of asynchronous generator",
        RuntimeWarning,
        stacklevel=2,
      )

      # Check that SSE-related warnings were filtered
      sse_warnings = [
        w
        for w in caught_warnings
        if any(
          phrase in str(w.message)
          for phrase in [
            "generator didn't stop",
            "cancel scope",
            "closing of asynchronous generator",
          ]
        )
      ]

      assert len(sse_warnings) == 0, f"SSE warnings should be filtered: {sse_warnings}"


class TestQuietAsyncioShutdown:
  """Test the scoped exception handler context manager"""

  @pytest.mark.asyncio
  async def test_quiet_shutdown_context(self):
    """Test that quiet_asyncio_shutdown provides scoped suppression"""

    # Track handler changes
    loop = asyncio.get_running_loop()
    original_handler = loop.get_exception_handler()

    handler_during_context = None

    with quiet_asyncio_shutdown():
      handler_during_context = loop.get_exception_handler()

    handler_after_context = loop.get_exception_handler()

    # Handler should change during context
    assert handler_during_context != original_handler

    # Handler should be restored after context
    assert handler_after_context == original_handler

  @pytest.mark.asyncio
  async def test_suppresses_known_noise(self):
    """Test that known SSE cleanup noise is suppressed"""

    exception_caught = False

    def test_handler(loop, context):
      nonlocal exception_caught
      exception_caught = True

    loop = asyncio.get_running_loop()
    loop.set_exception_handler(test_handler)

    try:
      with quiet_asyncio_shutdown():
        # Simulate the types of exceptions that should be suppressed
        context = {
          "exception": RuntimeError("generator didn't stop after athrow"),
          "message": "Test SSE cleanup error",
        }
        loop.call_exception_handler(context)

      # Exception should have been suppressed
      assert not exception_caught, "SSE cleanup exception should be suppressed"

    finally:
      loop.set_exception_handler(None)

  @pytest.mark.asyncio
  async def test_preserves_real_exceptions(self):
    """Test that real exceptions still surface properly"""

    caught_contexts = []

    def test_handler(loop, context):
      caught_contexts.append(context)

    loop = asyncio.get_running_loop()
    original_handler = loop.get_exception_handler()
    loop.set_exception_handler(test_handler)

    try:
      with quiet_asyncio_shutdown():
        # Simulate a real exception that should NOT be suppressed
        context = {
          "exception": ValueError("Real application error"),
          "message": "Important user error",
        }
        loop.call_exception_handler(context)

      # Real exception should still be processed (by default handler within our handler)
      # The context should have been passed to our test handler
      assert len(caught_contexts) > 0, "Real exceptions should still be handled"
      assert caught_contexts[0]["message"] == "Important user error"

    finally:
      loop.set_exception_handler(original_handler)


class TestDrainPendingTasks:
  """Test the task draining utility"""

  @pytest.mark.asyncio
  async def test_drain_empty_tasks(self):
    """Test draining when no tasks are pending"""
    # Should complete immediately without error
    await drain_pending_tasks(timeout=0.1)

  @pytest.mark.asyncio
  async def test_drain_completed_tasks(self):
    """Test draining when tasks complete normally"""

    async def quick_task():
      await asyncio.sleep(0.01)
      return "completed"

    # Start task
    task = asyncio.create_task(quick_task())

    # Wait for it to complete
    await task

    # Draining should work even with completed tasks
    await drain_pending_tasks(timeout=0.1)

  @pytest.mark.asyncio
  async def test_drain_cancels_hanging_tasks(self):
    """Test that hanging tasks are cancelled on timeout"""

    async def hanging_task():
      try:
        await asyncio.sleep(10)  # Long-running task
        return "should_not_reach"
      except asyncio.CancelledError:
        return "cancelled"

    # Start hanging task
    task = asyncio.create_task(hanging_task())

    # Drain with short timeout should cancel the task
    await drain_pending_tasks(timeout=0.1)

    # Task should be cancelled
    assert task.cancelled() or task.done()


@pytest.mark.asyncio
async def test_no_shutdown_warnings(recwarn, caplog):
  """Integration test: ensure no shutdown warnings are captured"""

  caplog.set_level(logging.DEBUG)

  # Install filters
  install_warning_filters()
  attach_noise_filters()

  # Simulate a complete shutdown sequence with SSE cleanup
  with quiet_asyncio_shutdown():
    try:
      # Simulate some async work
      await asyncio.sleep(0.01)
    finally:
      await drain_pending_tasks(timeout=0.1)

  # Check that no SSE-related warnings were captured
  sse_warnings = [
    w
    for w in recwarn
    if any(
      phrase in str(w.message)
      for phrase in [
        "generator didn't stop",
        "cancel scope",
        "closing of asynchronous generator",
      ]
    )
  ]

  assert len(sse_warnings) == 0, f"Should have no SSE warnings: {sse_warnings}"

  # Check that no SSE-related log messages were captured
  sse_logs = [
    r
    for r in caplog.records
    if any(
      phrase in r.message
      for phrase in ["closing of asynchronous generator", "sse_client", "aconnect_sse"]
    )
  ]

  assert len(sse_logs) == 0, f"Should have no SSE log noise: {sse_logs}"
