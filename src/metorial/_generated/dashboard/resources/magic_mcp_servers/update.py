from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersUpdateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersUpdateOutputEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersUpdateOutputEndpointsUrls


@dataclass
class MagicMcpServersUpdateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersUpdateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersUpdateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersUpdateOutputDefaultOauthSession:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class MagicMcpServersUpdateOutput:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersUpdateOutputEndpoints]
  server_deployments: List[MagicMcpServersUpdateOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  needs_default_oauth_session: bool
  description: Optional[str] = None
  default_oauth_session: Optional[MagicMcpServersUpdateOutputDefaultOauthSession] = None


class mapMagicMcpServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutput:
    return MagicMcpServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersUpdateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersUpdateOutputServerDeployments.from_dict(item)
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
      default_oauth_session=mapMagicMcpServersUpdateOutputDefaultOauthSession.from_dict(
        data.get("default_oauth_session")
      )
      if data.get("default_oauth_session")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class MagicMcpServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  aliases: Optional[List[str]] = None
  default_oauth_session_id: Optional[str] = None


class mapMagicMcpServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateBody:
    return MagicMcpServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      aliases=data.get("aliases", []),
      default_oauth_session_id=data.get("default_oauth_session_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
