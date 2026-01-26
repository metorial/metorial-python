from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpServersGetOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class DashboardInstanceMagicMcpServersGetOutputEndpoints:
  id: str
  alias: str
  urls: DashboardInstanceMagicMcpServersGetOutputEndpointsUrls


@dataclass
class DashboardInstanceMagicMcpServersGetOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersGetOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: DashboardInstanceMagicMcpServersGetOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersGetOutputDefaultOauthSession:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardInstanceMagicMcpServersGetOutput:
  object: str
  id: str
  status: str
  endpoints: List[DashboardInstanceMagicMcpServersGetOutputEndpoints]
  server_deployments: List[DashboardInstanceMagicMcpServersGetOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  needs_default_oauth_session: bool
  description: Optional[str] = None
  default_oauth_session: Optional[
    DashboardInstanceMagicMcpServersGetOutputDefaultOauthSession
  ] = None


class mapDashboardInstanceMagicMcpServersGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersGetOutput:
    return DashboardInstanceMagicMcpServersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapDashboardInstanceMagicMcpServersGetOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapDashboardInstanceMagicMcpServersGetOutputServerDeployments.from_dict(item)
        for item in data.get("server_deployments", [])
        if item
      ],
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      needs_default_oauth_session=data.get("needs_default_oauth_session"),
      default_oauth_session=mapDashboardInstanceMagicMcpServersGetOutputDefaultOauthSession.from_dict(
        data.get("default_oauth_session")
      )
      if data.get("default_oauth_session")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
