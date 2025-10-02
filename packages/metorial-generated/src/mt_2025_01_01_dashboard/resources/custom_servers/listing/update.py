from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

CustomServersListingUpdateOutput = Any


class mapCustomServersListingUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListingUpdateOutput:
    data

  @staticmethod
  def to_dict(
    value: Union[CustomServersListingUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


CustomServersListingUpdateBody = Dict[str, Any]


class mapCustomServersListingUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListingUpdateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[CustomServersListingUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
