from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer:
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpSessionsGetOutputUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class DashboardInstanceMagicMcpSessionsGetOutput:
  object: str
  id: str
  session_id: str
  connection_status: str
  magic_mcp_server: DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer
  usage: DashboardInstanceMagicMcpSessionsGetOutputUsage
  created_at: datetime
  updated_at: datetime


class mapDashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer:
    return DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer(
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
      DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpSessionsGetOutputUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpSessionsGetOutputUsage:
    return DashboardInstanceMagicMcpSessionsGetOutputUsage(
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
    value: Union[DashboardInstanceMagicMcpSessionsGetOutputUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpSessionsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsGetOutput:
    return DashboardInstanceMagicMcpSessionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      session_id=data.get("session_id"),
      connection_status=data.get("connection_status"),
      magic_mcp_server=mapDashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer.from_dict(
        data.get("magic_mcp_server")
      )
      if data.get("magic_mcp_server")
      else None,
      usage=mapDashboardInstanceMagicMcpSessionsGetOutputUsage.from_dict(
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
    value: Union[DashboardInstanceMagicMcpSessionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
