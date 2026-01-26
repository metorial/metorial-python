"""
Metorial Streaming Types
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class StreamEventType(Enum):
  """Types of streaming events"""

  CONTENT = "content"
  TOOL_CALL = "tool_call"
  COMPLETE = "complete"
  ERROR = "error"


@dataclass
class StreamEvent:
  """Streaming event data"""

  type: StreamEventType
  content: str | None = None
  tool_calls: list[dict[str, Any]] | None = None
  error: str | None = None
  metadata: dict[str, Any] | None = None
