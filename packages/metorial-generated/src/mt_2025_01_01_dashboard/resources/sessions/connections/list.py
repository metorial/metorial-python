from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsConnectionsListOutputItemsMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsConnectionsListOutputItemsMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsConnectionsListOutputItemsMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[SessionsConnectionsListOutputItemsMcpClient] = None
  server: Optional[SessionsConnectionsListOutputItemsMcpServer] = None


@dataclass
class SessionsConnectionsListOutputItemsUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsConnectionsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsConnectionsListOutputItemsSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsConnectionsListOutputItemsSession:
  object: str
  id: str
  status: str
  connection_status: str
  usage: SessionsConnectionsListOutputItemsSessionUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class SessionsConnectionsListOutputItemsServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsConnectionsListOutputItemsServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsConnectionsListOutputItemsServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsConnectionsListOutputItems:
  object: str
  id: str
  status: str
  mcp: SessionsConnectionsListOutputItemsMcp
  usage: SessionsConnectionsListOutputItemsUsage
  server: SessionsConnectionsListOutputItemsServer
  session: SessionsConnectionsListOutputItemsSession
  server_deployment: SessionsConnectionsListOutputItemsServerDeployment
  created_at: datetime
  started_at: datetime
  ended_at: Optional[datetime] = None


@dataclass
class SessionsConnectionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SessionsConnectionsListOutput:
  items: List[SessionsConnectionsListOutputItems]
  pagination: SessionsConnectionsListOutputPagination


class mapSessionsConnectionsListOutputItemsMcpClient:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsMcpClient:
    return SessionsConnectionsListOutputItemsMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListOutputItemsMcpClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsMcpServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsMcpServer:
    return SessionsConnectionsListOutputItemsMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListOutputItemsMcpServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsMcp:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsMcp:
    return SessionsConnectionsListOutputItemsMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsConnectionsListOutputItemsMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapSessionsConnectionsListOutputItemsMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListOutputItemsMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsUsage:
    return SessionsConnectionsListOutputItemsUsage(
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
    value: Union[SessionsConnectionsListOutputItemsUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsServer:
    return SessionsConnectionsListOutputItemsServer(
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
    value: Union[SessionsConnectionsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsSessionUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsSessionUsage:
    return SessionsConnectionsListOutputItemsSessionUsage(
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
    value: Union[SessionsConnectionsListOutputItemsSessionUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsSession:
    return SessionsConnectionsListOutputItemsSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      usage=mapSessionsConnectionsListOutputItemsSessionUsage.from_dict(
        data.get("usage")
      )
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
    value: Union[SessionsConnectionsListOutputItemsSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsConnectionsListOutputItemsServerDeploymentServer:
    return SessionsConnectionsListOutputItemsServerDeploymentServer(
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
    value: Union[
      SessionsConnectionsListOutputItemsServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItemsServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsConnectionsListOutputItemsServerDeployment:
    return SessionsConnectionsListOutputItemsServerDeployment(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      server=mapSessionsConnectionsListOutputItemsServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsConnectionsListOutputItemsServerDeployment, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItems:
    return SessionsConnectionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsConnectionsListOutputItemsMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapSessionsConnectionsListOutputItemsUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      server=mapSessionsConnectionsListOutputItemsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      session=mapSessionsConnectionsListOutputItemsSession.from_dict(
        data.get("session")
      )
      if data.get("session")
      else None,
      server_deployment=mapSessionsConnectionsListOutputItemsServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      started_at=datetime.fromisoformat(data.get("started_at"))
      if data.get("started_at")
      else None,
      ended_at=datetime.fromisoformat(data.get("ended_at"))
      if data.get("ended_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputPagination:
    return SessionsConnectionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutput:
    return SessionsConnectionsListOutput(
      items=[
        mapSessionsConnectionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapSessionsConnectionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsConnectionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapSessionsConnectionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListQuery:
    return SessionsConnectionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
