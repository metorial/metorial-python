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
class DashboardInstanceMagicMcpSessionsGetOutputClientInfo:
  name: str
  version: str


@dataclass
class DashboardInstanceMagicMcpSessionsGetOutputClient:
  object: str
  info: DashboardInstanceMagicMcpSessionsGetOutputClientInfo


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
  client: Optional[DashboardInstanceMagicMcpSessionsGetOutputClient] = None


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
      client=mapDashboardInstanceMagicMcpSessionsGetOutputClient.from_dict(
        data.get("client")
      )
      if data.get("client")
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
