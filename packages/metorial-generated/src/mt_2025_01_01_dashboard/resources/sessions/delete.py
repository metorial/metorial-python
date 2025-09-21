from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

SessionsDeleteOutput = Dict[str, Any]


class mapSessionsDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsDeleteOutput:
    data

  @staticmethod
  def to_dict(
    value: Union[SessionsDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
