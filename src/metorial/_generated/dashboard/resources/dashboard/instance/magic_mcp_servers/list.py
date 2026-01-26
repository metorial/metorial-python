from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceMagicMcpServersListOutput:
  items: List[Dict[str, Any]]
  pagination: DashboardInstanceMagicMcpServersListOutputPagination


class mapDashboardInstanceMagicMcpServersListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersListOutputPagination:
    return DashboardInstanceMagicMcpServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutput:
    return DashboardInstanceMagicMcpServersListOutput(
      items=data.get("items", []),
      pagination=mapDashboardInstanceMagicMcpServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceMagicMcpServersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_id: Optional[Union[str, List[str]]] = None
  server_variant_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  session_id: Optional[Union[str, List[str]]] = None
  search: Optional[str] = None


class mapDashboardInstanceMagicMcpServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListQuery:
    return DashboardInstanceMagicMcpServersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      server_implementation_id=data.get("server_implementation_id"),
      session_id=data.get("session_id"),
      search=data.get("search"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
