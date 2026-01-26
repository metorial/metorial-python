from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpSessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceMagicMcpSessionsListOutput:
  items: List[Dict[str, Any]]
  pagination: DashboardInstanceMagicMcpSessionsListOutputPagination


class mapDashboardInstanceMagicMcpSessionsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpSessionsListOutputPagination:
    return DashboardInstanceMagicMcpSessionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpSessionsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpSessionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListOutput:
    return DashboardInstanceMagicMcpSessionsListOutput(
      items=data.get("items", []),
      pagination=mapDashboardInstanceMagicMcpSessionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpSessionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceMagicMcpSessionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  magic_mcp_server_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceMagicMcpSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListQuery:
    return DashboardInstanceMagicMcpSessionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      magic_mcp_server_id=data.get("magic_mcp_server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpSessionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
