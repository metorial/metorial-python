from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersCreateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersCreateOutputEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersCreateOutputEndpointsUrls


@dataclass
class MagicMcpServersCreateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersCreateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersCreateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersCreateOutputDefaultOauthSession:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class MagicMcpServersCreateOutput:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersCreateOutputEndpoints]
  server_deployments: List[MagicMcpServersCreateOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  needs_default_oauth_session: bool
  description: Optional[str] = None
  default_oauth_session: Optional[MagicMcpServersCreateOutputDefaultOauthSession] = None


class mapMagicMcpServersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersCreateOutput:
    return MagicMcpServersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersCreateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersCreateOutputServerDeployments.from_dict(item)
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
      default_oauth_session=mapMagicMcpServersCreateOutputDefaultOauthSession.from_dict(
        data.get("default_oauth_session")
      )
      if data.get("default_oauth_session")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class MagicMcpServersCreateBody:
  server_implementation: Optional[Dict[str, Any]] = None
  server_implementation_id: Optional[str] = None
  server_variant_id: Optional[str] = None
  server_id: Optional[str] = None


class mapMagicMcpServersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersCreateBody:
    return MagicMcpServersCreateBody(
      server_implementation=data.get("server_implementation"),
      server_implementation_id=data.get("server_implementation_id"),
      server_variant_id=data.get("server_variant_id"),
      server_id=data.get("server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
