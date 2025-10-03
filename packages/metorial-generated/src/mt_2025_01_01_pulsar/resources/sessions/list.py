from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsListOutputItemsClientSecret:
  object: str
  type: str
  id: str
  secret: str
  expires_at: datetime


@dataclass
class SessionsListOutputItemsServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsListOutputItemsServerDeploymentsConnectionUrls:
  sse: str
  streamable_http: str
  websocket: str


@dataclass
class SessionsListOutputItemsServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsListOutputItemsServerDeploymentsServer
  connection_urls: SessionsListOutputItemsServerDeploymentsConnectionUrls
  name: Optional[str] = None
  oauth_session_id: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsListOutputItemsUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsListOutputItems:
  object: str
  id: str
  status: str
  connection_status: str
  client_secret: SessionsListOutputItemsClientSecret
  server_deployments: List[SessionsListOutputItemsServerDeployments]
  usage: SessionsListOutputItemsUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class SessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SessionsListOutput:
  items: List[SessionsListOutputItems]
  pagination: SessionsListOutputPagination


class mapSessionsListOutputItemsClientSecret:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsClientSecret:
    return SessionsListOutputItemsClientSecret(
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
    value: Union[SessionsListOutputItemsClientSecret, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutputItemsServerDeploymentsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsServerDeploymentsServer:
    return SessionsListOutputItemsServerDeploymentsServer(
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
    value: Union[SessionsListOutputItemsServerDeploymentsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutputItemsServerDeploymentsConnectionUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsListOutputItemsServerDeploymentsConnectionUrls:
    return SessionsListOutputItemsServerDeploymentsConnectionUrls(
      sse=data.get("sse"),
      streamable_http=data.get("streamable_http"),
      websocket=data.get("websocket"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsListOutputItemsServerDeploymentsConnectionUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutputItemsServerDeployments:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsServerDeployments:
    return SessionsListOutputItemsServerDeployments(
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
      server=mapSessionsListOutputItemsServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      connection_urls=mapSessionsListOutputItemsServerDeploymentsConnectionUrls.from_dict(
        data.get("connection_urls")
      )
      if data.get("connection_urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListOutputItemsServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutputItemsUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsUsage:
    return SessionsListOutputItemsUsage(
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
    value: Union[SessionsListOutputItemsUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputItems:
    return SessionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      client_secret=mapSessionsListOutputItemsClientSecret.from_dict(
        data.get("client_secret")
      )
      if data.get("client_secret")
      else None,
      server_deployments=[
        mapSessionsListOutputItemsServerDeployments.from_dict(item)
        for item in data.get("server_deployments", [])
        if item
      ],
      usage=mapSessionsListOutputItemsUsage.from_dict(data.get("usage"))
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
    value: Union[SessionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputPagination:
    return SessionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutput:
    return SessionsListOutput(
      items=[
        mapSessionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapSessionsListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_id: Optional[Union[str, List[str]]] = None
  server_variant_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  server_deployment_id: Optional[Union[str, List[str]]] = None


class mapSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListQuery:
    return SessionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      server_implementation_id=data.get("server_implementation_id"),
      server_deployment_id=data.get("server_deployment_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
