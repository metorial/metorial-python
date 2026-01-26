from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpSessionsListOutputItemsUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class DashboardInstanceMagicMcpSessionsListOutputItems:
  object: str
  id: str
  session_id: str
  connection_status: str
  magic_mcp_server: DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer
  usage: DashboardInstanceMagicMcpSessionsListOutputItemsUsage
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardInstanceMagicMcpSessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceMagicMcpSessionsListOutput:
  items: List[DashboardInstanceMagicMcpSessionsListOutputItems]
  pagination: DashboardInstanceMagicMcpSessionsListOutputPagination


class mapDashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
    return DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer(
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpSessionsListOutputItemsUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpSessionsListOutputItemsUsage:
    return DashboardInstanceMagicMcpSessionsListOutputItemsUsage(
      total_productive_message_count=data.get("total_productive_message_count"),
      total_productive_client_message_count=data.get(
        "total_productive_client_message_count"
      ),
      total_productive_server_message_count=data.get(
        "total_productive_server_message_count"
      ),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpSessionsListOutputItemsUsage, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpSessionsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpSessionsListOutputItems:
    return DashboardInstanceMagicMcpSessionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      session_id=data.get("session_id"),
      connection_status=data.get("connection_status"),
      magic_mcp_server=mapDashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer.from_dict(
        data.get("magic_mcp_server")
      )
      if data.get("magic_mcp_server")
      else None,
      usage=mapDashboardInstanceMagicMcpSessionsListOutputItemsUsage.from_dict(
        data.get("usage")
      )
      if data.get("usage")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpSessionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


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
      items=[
        mapDashboardInstanceMagicMcpSessionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
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
