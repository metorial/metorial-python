from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsGetOutputClientSecret:
  object: str
  type: str
  id: str
  secret: str
  expires_at: datetime


@dataclass
class SessionsGetOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsGetOutputServerDeploymentsConnectionUrls:
  sse: str
  streamable_http: str
  websocket: str


@dataclass
class SessionsGetOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsGetOutputServerDeploymentsServer
  connection_urls: SessionsGetOutputServerDeploymentsConnectionUrls
  name: Optional[str] = None
  oauth_session_id: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsGetOutputUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsGetOutput:
  object: str
  id: str
  status: str
  connection_status: str
  client_secret: SessionsGetOutputClientSecret
  server_deployments: List[SessionsGetOutputServerDeployments]
  usage: SessionsGetOutputUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


class mapSessionsGetOutputClientSecret:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsGetOutputClientSecret:
    return SessionsGetOutputClientSecret(
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
    value: Union[SessionsGetOutputClientSecret, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsGetOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsGetOutputServerDeploymentsServer:
    return SessionsGetOutputServerDeploymentsServer(
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
    value: Union[SessionsGetOutputServerDeploymentsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsGetOutputServerDeploymentsConnectionUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsGetOutputServerDeploymentsConnectionUrls:
    return SessionsGetOutputServerDeploymentsConnectionUrls(
      sse=data.get("sse"),
      streamable_http=data.get("streamable_http"),
      websocket=data.get("websocket"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsGetOutputServerDeploymentsConnectionUrls, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsGetOutputServerDeployments:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsGetOutputServerDeployments:
    return SessionsGetOutputServerDeployments(
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
      server=mapSessionsGetOutputServerDeploymentsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      connection_urls=mapSessionsGetOutputServerDeploymentsConnectionUrls.from_dict(
        data.get("connection_urls")
      )
      if data.get("connection_urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsGetOutputServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsGetOutputUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsGetOutputUsage:
    return SessionsGetOutputUsage(
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
    value: Union[SessionsGetOutputUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsGetOutput:
    return SessionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      client_secret=mapSessionsGetOutputClientSecret.from_dict(
        data.get("client_secret")
      )
      if data.get("client_secret")
      else None,
      server_deployments=[
        mapSessionsGetOutputServerDeployments.from_dict(item)
        for item in data.get("server_deployments", [])
        if item
      ],
      usage=mapSessionsGetOutputUsage.from_dict(data.get("usage"))
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
    value: Union[SessionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
