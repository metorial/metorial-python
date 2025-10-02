from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersVersionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CustomServersVersionsListOutput:
  items: List[Any]
  pagination: CustomServersVersionsListOutputPagination


class mapCustomServersVersionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsListOutputPagination:
    return CustomServersVersionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersVersionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsListOutput:
    return CustomServersVersionsListOutput(
      items=data.get("items", []),
      pagination=mapCustomServersVersionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


CustomServersVersionsListQuery = Any


class mapCustomServersVersionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsListQuery:
    data

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
