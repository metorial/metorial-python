from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputEndpoints:
  id: str
  alias: str
  urls: DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputDefaultOauthSession:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutput:
  object: str
  id: str
  status: str
  endpoints: List[DashboardInstanceMagicMcpServersUpdateOutputEndpoints]
  server_deployments: List[
    DashboardInstanceMagicMcpServersUpdateOutputServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  needs_default_oauth_session: bool
  description: Optional[str] = None
  default_oauth_session: Optional[
    DashboardInstanceMagicMcpServersUpdateOutputDefaultOauthSession
  ] = None


class mapDashboardInstanceMagicMcpServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersUpdateOutput:
    return DashboardInstanceMagicMcpServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapDashboardInstanceMagicMcpServersUpdateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapDashboardInstanceMagicMcpServersUpdateOutputServerDeployments.from_dict(item)
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
      default_oauth_session=mapDashboardInstanceMagicMcpServersUpdateOutputDefaultOauthSession.from_dict(
        data.get("default_oauth_session")
      )
      if data.get("default_oauth_session")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceMagicMcpServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  aliases: Optional[List[str]] = None
  default_oauth_session_id: Optional[str] = None


class mapDashboardInstanceMagicMcpServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersUpdateBody:
    return DashboardInstanceMagicMcpServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      aliases=data.get("aliases", []),
      default_oauth_session_id=data.get("default_oauth_session_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
