from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

CustomServersVersionsCreateOutput = Any


class mapCustomServersVersionsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsCreateOutput:
    data

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersVersionsCreateBody:
  implementation: Dict[str, Any]


class mapCustomServersVersionsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsCreateBody:
    return CustomServersVersionsCreateBody(implementation=data.get("implementation"))

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
