from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersDeleteOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersDeleteOutputEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersDeleteOutputEndpointsUrls


@dataclass
class MagicMcpServersDeleteOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersDeleteOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersDeleteOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersDeleteOutputDefaultOauthSession:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class MagicMcpServersDeleteOutput:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersDeleteOutputEndpoints]
  server_deployments: List[MagicMcpServersDeleteOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  needs_default_oauth_session: bool
  description: Optional[str] = None
  default_oauth_session: Optional[MagicMcpServersDeleteOutputDefaultOauthSession] = None


class mapMagicMcpServersDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersDeleteOutput:
    return MagicMcpServersDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersDeleteOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersDeleteOutputServerDeployments.from_dict(item)
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
      default_oauth_session=mapMagicMcpServersDeleteOutputDefaultOauthSession.from_dict(
        data.get("default_oauth_session")
      )
      if data.get("default_oauth_session")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
