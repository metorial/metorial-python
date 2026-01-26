from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpSessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceMagicMcpSessionsListOutput:
  items: List[Dict[str, Any]]
  pagination: ManagementInstanceMagicMcpSessionsListOutputPagination


class mapManagementInstanceMagicMcpSessionsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpSessionsListOutputPagination:
    return ManagementInstanceMagicMcpSessionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpSessionsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpSessionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutput:
    return ManagementInstanceMagicMcpSessionsListOutput(
      items=data.get("items", []),
      pagination=mapManagementInstanceMagicMcpSessionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpSessionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceMagicMcpSessionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  magic_mcp_server_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceMagicMcpSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListQuery:
    return ManagementInstanceMagicMcpSessionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      magic_mcp_server_id=data.get("magic_mcp_server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpSessionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
