"""
Metorial Chat Metrics
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class ChatMetrics:
  """Chat completion metrics"""

  start_time: float
  end_time: Optional[float] = None
  iterations: int = 0
  tool_calls: int = 0
  tokens_used: Optional[int] = None
  error: Optional[str] = None

  @property
  def duration(self) -> Optional[float]:
    return self.end_time - self.start_time if self.end_time else None
