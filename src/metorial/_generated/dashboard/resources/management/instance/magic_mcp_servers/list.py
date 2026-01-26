from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceMagicMcpServersListOutput:
  items: List[Dict[str, Any]]
  pagination: ManagementInstanceMagicMcpServersListOutputPagination


class mapManagementInstanceMagicMcpServersListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputPagination:
    return ManagementInstanceMagicMcpServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersListOutput:
    return ManagementInstanceMagicMcpServersListOutput(
      items=data.get("items", []),
      pagination=mapManagementInstanceMagicMcpServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceMagicMcpServersListQuery:
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


class mapManagementInstanceMagicMcpServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersListQuery:
    return ManagementInstanceMagicMcpServersListQuery(
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
    value: Union[ManagementInstanceMagicMcpServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
