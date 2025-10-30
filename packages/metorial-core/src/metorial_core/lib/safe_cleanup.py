"""
Safe AsyncIO cleanup utilities for eliminating SSE shutdown warnings
without global monkey-patching or hiding real errors.
"""

import asyncio
import logging
import re
import signal
import warnings
from contextlib import contextmanager
from typing import Callable, Optional


# Precise warning patterns for known cleanup artifacts
GEN_THROW = re.compile(r"generator didn't stop after athrow")
CANCEL_SCOPE = re.compile(r"Attempted to exit cancel scope")
ASYNC_GEN_CLOSE = re.compile(r"an error occurred during closing of asynchronous generator")


def install_warning_filters():
    """Install precise warning filters for known SSE cleanup noise"""
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message=GEN_THROW.pattern
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message=CANCEL_SCOPE.pattern
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message=ASYNC_GEN_CLOSE.pattern
    )


class SseNoiseFilter(logging.Filter):
    """Precise logging filter to drop only SSE cleanup noise"""
    
    NOISE = (
        "sse_client",
        "aconnect_sse", 
        "generator didn't stop after athrow",
        "Attempted to exit cancel scope",
        "an error occurred during closing of asynchronous generator",
    )
    
    def filter(self, record: logging.LogRecord) -> bool:
        """Return False to drop records containing SSE cleanup noise"""
        msg = record.getMessage()
        return not any(phrase in msg for phrase in self.NOISE)


def attach_noise_filters():
    """Attach noise filters to specific loggers (not global level blasting)"""
    for name in ("mcp.client.sse", "httpx_sse", "anyio", "httpcore", "asyncio"):
        lg = logging.getLogger(name)
        lg.addFilter(SseNoiseFilter())


@contextmanager
def quiet_asyncio_shutdown():
    """
    Scoped suppression of known asyncio cleanup noise during teardown window only.
    No global monkey-patching - restores original handler afterward.
    """
    loop = None
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    def handler(loop_, context):
        """Custom handler that suppresses only known SSE cleanup artifacts"""
        exc = context.get("exception")
        msg = (str(exc) if exc else context.get("message", "")) or ""
        
        # Suppress only known cleanup artifacts
        if any(s in msg for s in SseNoiseFilter.NOISE):
            return  # Silently ignore
            
        # For other exceptions, use default behavior
        loop_.default_exception_handler(context)

    old_handler = None
    if loop:
        old_handler = loop.get_exception_handler()
        loop.set_exception_handler(handler)
    
    try:
        yield
    finally:
        # Always restore original handler
        if loop:
            loop.set_exception_handler(old_handler)


def install_signal_shutdown(cancel_cb: Callable[[], None]):
    """Install graceful SIGINT/SIGTERM handling for services"""
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, cancel_cb)
        except NotImplementedError:
            # Signal handlers not supported on this platform (e.g., Windows)
            pass


async def drain_pending_tasks(timeout: float = 0.5):
    """
    Safely drain pending tasks during shutdown.
    Uses asyncio.timeout() for Python 3.11+ with fallback for older versions.
    """
    current_task = asyncio.current_task()
    pending = [t for t in asyncio.all_tasks() if t is not current_task and not t.done()]
    
    if not pending:
        return
        
    try:
        # Python 3.11+ has asyncio.timeout
        try:
            async with asyncio.timeout(timeout):
                await asyncio.gather(*pending, return_exceptions=True)
        except AttributeError:
            # Fallback for Python 3.10
            await asyncio.wait_for(
                asyncio.gather(*pending, return_exceptions=True), 
                timeout=timeout
            )
    except (asyncio.TimeoutError, TimeoutError):
        # Cancel remaining tasks if timeout exceeded
        for task in pending:
            if not task.done():
                task.cancel()
        # Give cancellation a moment to complete
        try:
            await asyncio.wait_for(
                asyncio.gather(*pending, return_exceptions=True),
                timeout=0.1
            )
        except Exception:
            pass  # Final cleanup should never raise
