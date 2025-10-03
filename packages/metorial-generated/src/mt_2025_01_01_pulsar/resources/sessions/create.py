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


class mapSessionsCreateOutputClientSecret:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateOutputClientSecret:
    return SessionsCreateOutputClientSecret(
      object=data.get("object"),
      type=data.get("type"),
      id=data.get("id"),
      secret=data.get("secret"),
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateOutputClientSecret, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsCreateOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateOutputServerDeploymentsServer:
    return SessionsCreateOutputServerDeploymentsServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateOutputServerDeploymentsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsCreateOutputServerDeploymentsConnectionUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsCreateOutputServerDeploymentsConnectionUrls:
    return SessionsCreateOutputServerDeploymentsConnectionUrls(
      sse=data.get("sse"),
      streamable_http=data.get("streamable_http"),
      websocket=data.get("websocket"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsCreateOutputServerDeploymentsConnectionUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsCreateOutputServerDeployments:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateOutputServerDeployments:
    return SessionsCreateOutputServerDeployments(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      oauth_session_id=data.get("oauth_session_id"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      server=mapSessionsCreateOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      connection_urls=mapSessionsCreateOutputServerDeploymentsConnectionUrls.from_dict(
        data.get("connection_urls")
      )
      if data.get("connection_urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsCreateOutputServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsCreateOutputUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsCreateOutputUsage:
    return SessionsCreateOutputUsage(
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
    value: Union[SessionsCreateOutputUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


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
