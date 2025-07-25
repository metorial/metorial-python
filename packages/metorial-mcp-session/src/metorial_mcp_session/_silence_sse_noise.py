# metorial_py/_silence_sse_noise.py  (import this very early)

from anyio import BrokenResourceError, EndOfStream
from anyio.streams.memory import MemoryObjectSendStream

# Keep originals so we can still call them
_orig_send = MemoryObjectSendStream.send
_orig_send_nowait = MemoryObjectSendStream.send_nowait

async def _safe_send(self, item):
    try:
        return await _orig_send(self, item)
    except (BrokenResourceError, EndOfStream):
        # Writer is gone during shutdown; ignore
        return

def _safe_send_nowait(self, item):
    try:
        return _orig_send_nowait(self, item)
    except (BrokenResourceError, EndOfStream):
        return

# Patch once
MemoryObjectSendStream.send = _safe_send
MemoryObjectSendStream.send_nowait = _safe_send_nowait
