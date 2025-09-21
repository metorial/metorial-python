from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

SessionsCreateOutput = Dict[str, Any]


class mapSessionsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateOutput:
    data

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


SessionsCreateBody = Dict[str, Any]


class mapSessionsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
