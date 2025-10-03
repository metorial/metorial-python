from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServerRunsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunsListOutputItemsServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunsListOutputItemsServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServerRunsListOutputItemsServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServerRunsListOutputItemsServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunsListOutputItemsServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunsListOutputItemsServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[ServerRunsListOutputItemsServerSessionMcpClient] = None
  server: Optional[ServerRunsListOutputItemsServerSessionMcpServer] = None


@dataclass
class ServerRunsListOutputItemsServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class ServerRunsListOutputItemsServerSession:
  object: str
  id: str
  status: str
  mcp: ServerRunsListOutputItemsServerSessionMcp
  usage: ServerRunsListOutputItemsServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class ServerRunsListOutputItems:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: ServerRunsListOutputItemsServer
  server_deployment: ServerRunsListOutputItemsServerDeployment
  server_session: ServerRunsListOutputItemsServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class ServerRunsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServerRunsListOutput:
  items: List[ServerRunsListOutputItems]
  pagination: ServerRunsListOutputPagination


class mapServerRunsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputItemsServer:
    return ServerRunsListOutputItemsServer(
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
    value: Union[ServerRunsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunsListOutputItemsServerDeploymentServer:
    return ServerRunsListOutputItemsServerDeploymentServer(
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
    value: Union[ServerRunsListOutputItemsServerDeploymentServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerDeployment:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputItemsServerDeployment:
    return ServerRunsListOutputItemsServerDeployment(
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
      server=mapServerRunsListOutputItemsServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputItemsServerDeployment, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunsListOutputItemsServerSessionMcpClient:
    return ServerRunsListOutputItemsServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputItemsServerSessionMcpClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunsListOutputItemsServerSessionMcpServer:
    return ServerRunsListOutputItemsServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputItemsServerSessionMcpServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerSessionMcp:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputItemsServerSessionMcp:
    return ServerRunsListOutputItemsServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapServerRunsListOutputItemsServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapServerRunsListOutputItemsServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputItemsServerSessionMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerSessionUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputItemsServerSessionUsage:
    return ServerRunsListOutputItemsServerSessionUsage(
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
    value: Union[ServerRunsListOutputItemsServerSessionUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItemsServerSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputItemsServerSession:
    return ServerRunsListOutputItemsServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapServerRunsListOutputItemsServerSessionMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapServerRunsListOutputItemsServerSessionUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      session_id=data.get("session_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputItemsServerSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputItems:
    return ServerRunsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapServerRunsListOutputItemsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_deployment=mapServerRunsListOutputItemsServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapServerRunsListOutputItemsServerSession.from_dict(
        data.get("server_session")
      )
      if data.get("server_session")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      started_at=datetime.fromisoformat(data.get("started_at"))
      if data.get("started_at")
      else None,
      stopped_at=datetime.fromisoformat(data.get("stopped_at"))
      if data.get("stopped_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutputPagination:
    return ServerRunsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListOutput:
    return ServerRunsListOutput(
      items=[
        mapServerRunsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServerRunsListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServerRunsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_session_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  server_deployment_id: Optional[Union[str, List[str]]] = None
  session_id: Optional[Union[str, List[str]]] = None


class mapServerRunsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsListQuery:
    return ServerRunsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_session_id=data.get("server_session_id"),
      server_implementation_id=data.get("server_implementation_id"),
      server_deployment_id=data.get("server_deployment_id"),
      session_id=data.get("session_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
