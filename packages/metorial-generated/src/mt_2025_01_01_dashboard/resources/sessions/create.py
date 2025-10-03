from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsCreateOutputClientSecret:
  object: str
  type: str
  id: str
  secret: str
  expires_at: datetime


@dataclass
class SessionsCreateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsCreateOutputServerDeploymentsConnectionUrls:
  sse: str
  streamable_http: str
  websocket: str


@dataclass
class SessionsCreateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsCreateOutputServerDeploymentsServer
  connection_urls: SessionsCreateOutputServerDeploymentsConnectionUrls
  name: Optional[str] = None
  oauth_session_id: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsCreateOutputUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsCreateOutputClientInfo:
  name: str
  version: str


@dataclass
class SessionsCreateOutputClient:
  object: str
  info: SessionsCreateOutputClientInfo


@dataclass
class SessionsCreateOutput:
  object: str
  id: str
  status: str
  connection_status: str
  client_secret: SessionsCreateOutputClientSecret
  server_deployments: List[SessionsCreateOutputServerDeployments]
  usage: SessionsCreateOutputUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  client: Optional[SessionsCreateOutputClient] = None


class mapSessionsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateOutput:
    return SessionsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      client_secret=mapSessionsCreateOutputClientSecret.from_dict(
        data.get("client_secret")
      )
      if data.get("client_secret")
      else None,
      server_deployments=[
        mapSessionsCreateOutputServerDeployments.from_dict(item)
        for item in data.get("server_deployments", [])
        if item
      ],
      usage=mapSessionsCreateOutputUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      client=mapSessionsCreateOutputClient.from_dict(data.get("client"))
      if data.get("client")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsCreateBody:
  server_deployments: List[Union[Dict[str, Any], str]]


class mapSessionsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateBody:
    return SessionsCreateBody(server_deployments=data.get("server_deployments", []))

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
