from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCustomServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceCustomServersListOutput:
  items: List[Dict[str, Any]]
  pagination: DashboardInstanceCustomServersListOutputPagination


class mapDashboardInstanceCustomServersListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCustomServersListOutputPagination:
    return DashboardInstanceCustomServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCustomServersListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCustomServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersListOutput:
    return DashboardInstanceCustomServersListOutput(
      items=data.get("items", []),
      pagination=mapDashboardInstanceCustomServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCustomServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceCustomServersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  type: Optional[Union[List[str], str]] = None


class mapDashboardInstanceCustomServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersListQuery:
    return DashboardInstanceCustomServersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      type=data.get("type"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCustomServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
