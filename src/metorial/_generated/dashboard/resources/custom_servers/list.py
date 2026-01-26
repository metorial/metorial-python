from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CustomServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CustomServersListOutput:
  items: List[Dict[str, Any]]
  pagination: CustomServersListOutputPagination


class mapCustomServersListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListOutputPagination:
    return CustomServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListOutput:
    return CustomServersListOutput(
      items=data.get("items", []),
      pagination=mapCustomServersListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  type: Optional[Union[List[str], str]] = None


class mapCustomServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListQuery:
    return CustomServersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      type=data.get("type"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
