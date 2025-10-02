"""
Metorial Streaming Types
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum


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
  content: Optional[str] = None
  tool_calls: Optional[List[Dict]] = None
  error: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
