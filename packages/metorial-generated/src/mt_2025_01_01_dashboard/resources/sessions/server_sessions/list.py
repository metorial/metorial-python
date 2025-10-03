from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsServerSessionsListOutputItemsMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsServerSessionsListOutputItemsMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsServerSessionsListOutputItemsMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[SessionsServerSessionsListOutputItemsMcpClient] = None
  server: Optional[SessionsServerSessionsListOutputItemsMcpServer] = None


@dataclass
class SessionsServerSessionsListOutputItemsUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsServerSessionsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsServerSessionsListOutputItemsSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsServerSessionsListOutputItemsSession:
  object: str
  id: str
  status: str
  connection_status: str
  usage: SessionsServerSessionsListOutputItemsSessionUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class SessionsServerSessionsListOutputItemsServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsServerSessionsListOutputItemsServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsServerSessionsListOutputItemsServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsServerSessionsListOutputItemsConnectionClient:
  user_agent: str
  anonymized_ip_address: str


@dataclass
class SessionsServerSessionsListOutputItemsConnection:
  object: str
  id: str
  client: SessionsServerSessionsListOutputItemsConnectionClient
  created_at: datetime
  started_at: datetime
  ended_at: Optional[datetime] = None


@dataclass
class SessionsServerSessionsListOutputItems:
  object: str
  id: str
  status: str
  mcp: SessionsServerSessionsListOutputItemsMcp
  usage: SessionsServerSessionsListOutputItemsUsage
  server: SessionsServerSessionsListOutputItemsServer
  session: SessionsServerSessionsListOutputItemsSession
  server_deployment: SessionsServerSessionsListOutputItemsServerDeployment
  created_at: datetime
  connection: Optional[SessionsServerSessionsListOutputItemsConnection] = None


@dataclass
class SessionsServerSessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SessionsServerSessionsListOutput:
  items: List[SessionsServerSessionsListOutputItems]
  pagination: SessionsServerSessionsListOutputPagination


class mapSessionsServerSessionsListOutputItemsMcpClient:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItemsMcpClient:
    return SessionsServerSessionsListOutputItemsMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListOutputItemsMcpClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsMcpServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItemsMcpServer:
    return SessionsServerSessionsListOutputItemsMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListOutputItemsMcpServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsMcp:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItemsMcp:
    return SessionsServerSessionsListOutputItemsMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsServerSessionsListOutputItemsMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapSessionsServerSessionsListOutputItemsMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListOutputItemsMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItemsUsage:
    return SessionsServerSessionsListOutputItemsUsage(
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
    value: Union[SessionsServerSessionsListOutputItemsUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItemsServer:
    return SessionsServerSessionsListOutputItemsServer(
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
    value: Union[SessionsServerSessionsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsListOutputItemsSessionUsage:
    return SessionsServerSessionsListOutputItemsSessionUsage(
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
    value: Union[
      SessionsServerSessionsListOutputItemsSessionUsage, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItemsSession:
    return SessionsServerSessionsListOutputItemsSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      usage=mapSessionsServerSessionsListOutputItemsSessionUsage.from_dict(
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
    value: Union[SessionsServerSessionsListOutputItemsSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsListOutputItemsServerDeploymentServer:
    return SessionsServerSessionsListOutputItemsServerDeploymentServer(
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
      SessionsServerSessionsListOutputItemsServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsListOutputItemsServerDeployment:
    return SessionsServerSessionsListOutputItemsServerDeployment(
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
      server=mapSessionsServerSessionsListOutputItemsServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsServerSessionsListOutputItemsServerDeployment, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsConnectionClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsListOutputItemsConnectionClient:
    return SessionsServerSessionsListOutputItemsConnectionClient(
      user_agent=data.get("user_agent"),
      anonymized_ip_address=data.get("anonymized_ip_address"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsServerSessionsListOutputItemsConnectionClient, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItemsConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsListOutputItemsConnection:
    return SessionsServerSessionsListOutputItemsConnection(
      object=data.get("object"),
      id=data.get("id"),
      client=mapSessionsServerSessionsListOutputItemsConnectionClient.from_dict(
        data.get("client")
      )
      if data.get("client")
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
    value: Union[SessionsServerSessionsListOutputItemsConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputItems:
    return SessionsServerSessionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsServerSessionsListOutputItemsMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapSessionsServerSessionsListOutputItemsUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      server=mapSessionsServerSessionsListOutputItemsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      session=mapSessionsServerSessionsListOutputItemsSession.from_dict(
        data.get("session")
      )
      if data.get("session")
      else None,
      server_deployment=mapSessionsServerSessionsListOutputItemsServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      connection=mapSessionsServerSessionsListOutputItemsConnection.from_dict(
        data.get("connection")
      )
      if data.get("connection")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutputPagination:
    return SessionsServerSessionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListOutput:
    return SessionsServerSessionsListOutput(
      items=[
        mapSessionsServerSessionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapSessionsServerSessionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsServerSessionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapSessionsServerSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsListQuery:
    return SessionsServerSessionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
