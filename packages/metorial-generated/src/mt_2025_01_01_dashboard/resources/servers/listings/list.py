from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersListingsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersListingsListOutput:
  items: List[Dict[str, Any]]
  pagination: ServersListingsListOutputPagination


class mapServersListingsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsListOutputPagination:
    return ServersListingsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersListingsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsListOutput:
    return ServersListingsListOutput(
      items=data.get("items", []),
      pagination=mapServersListingsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


ServersListingsListQuery = Any


class mapServersListingsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsListQuery:
    data

  @staticmethod
  def to_dict(
    value: Union[ServersListingsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
