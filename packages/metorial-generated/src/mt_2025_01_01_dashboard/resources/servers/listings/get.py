from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

ServersListingsGetOutput = Any


class mapServersListingsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsGetOutput:
    data

  @staticmethod
  def to_dict(
    value: Union[ServersListingsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersListingsGetQuery:
  instance_id: Optional[str] = None


class mapServersListingsGetQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsGetQuery:
    return ServersListingsGetQuery(instance_id=data.get("instance_id"))

  @staticmethod
  def to_dict(
    value: Union[ServersListingsGetQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
