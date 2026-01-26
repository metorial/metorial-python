from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCustomServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceCustomServersListOutput:
  items: List[Dict[str, Any]]
  pagination: ManagementInstanceCustomServersListOutputPagination


class mapManagementInstanceCustomServersListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCustomServersListOutputPagination:
    return ManagementInstanceCustomServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCustomServersListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCustomServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersListOutput:
    return ManagementInstanceCustomServersListOutput(
      items=data.get("items", []),
      pagination=mapManagementInstanceCustomServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCustomServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCustomServersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  type: Optional[Union[List[str], str]] = None


class mapManagementInstanceCustomServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersListQuery:
    return ManagementInstanceCustomServersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      type=data.get("type"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCustomServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
