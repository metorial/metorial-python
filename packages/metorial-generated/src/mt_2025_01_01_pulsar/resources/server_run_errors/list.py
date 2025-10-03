from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServerRunErrorsListOutputItemsServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServerRunErrorsListOutputItemsServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[ServerRunErrorsListOutputItemsServerRunServerSessionMcpClient] = None
  server: Optional[ServerRunErrorsListOutputItemsServerRunServerSessionMcpServer] = None


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class ServerRunErrorsListOutputItemsServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: ServerRunErrorsListOutputItemsServerRunServerSessionMcp
  usage: ServerRunErrorsListOutputItemsServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class ServerRunErrorsListOutputItemsServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: ServerRunErrorsListOutputItemsServerRunServer
  server_deployment: ServerRunErrorsListOutputItemsServerRunServerDeployment
  server_session: ServerRunErrorsListOutputItemsServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class ServerRunErrorsListOutputItems:
  object: str
  id: str
  code: str
  message: str
  metadata: Dict[str, Any]
  server_run: ServerRunErrorsListOutputItemsServerRun
  created_at: datetime


@dataclass
class ServerRunErrorsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServerRunErrorsListOutput:
  items: List[ServerRunErrorsListOutputItems]
  pagination: ServerRunErrorsListOutputPagination


class mapServerRunErrorsListOutputItemsServerRunServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsListOutputItemsServerRunServer:
    return ServerRunErrorsListOutputItemsServerRunServer(
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
    value: Union[ServerRunErrorsListOutputItemsServerRunServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
    return ServerRunErrorsListOutputItemsServerRunServerDeploymentServer(
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
      ServerRunErrorsListOutputItemsServerRunServerDeploymentServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerDeployment:
    return ServerRunErrorsListOutputItemsServerRunServerDeployment(
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
      server=mapServerRunErrorsListOutputItemsServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsListOutputItemsServerRunServerDeployment, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
    return ServerRunErrorsListOutputItemsServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsListOutputItemsServerRunServerSessionMcpClient,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
    return ServerRunErrorsListOutputItemsServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsListOutputItemsServerRunServerSessionMcpServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerSessionMcp:
    return ServerRunErrorsListOutputItemsServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapServerRunErrorsListOutputItemsServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapServerRunErrorsListOutputItemsServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsListOutputItemsServerRunServerSessionMcp, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerSessionUsage:
    return ServerRunErrorsListOutputItemsServerRunServerSessionUsage(
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
      ServerRunErrorsListOutputItemsServerRunServerSessionUsage, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRunServerSession:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsListOutputItemsServerRunServerSession:
    return ServerRunErrorsListOutputItemsServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapServerRunErrorsListOutputItemsServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapServerRunErrorsListOutputItemsServerRunServerSessionUsage.from_dict(
        data.get("usage")
      )
      if data.get("usage")
      else None,
      session_id=data.get("session_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsListOutputItemsServerRunServerSession, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItemsServerRun:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsListOutputItemsServerRun:
    return ServerRunErrorsListOutputItemsServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapServerRunErrorsListOutputItemsServerRunServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_deployment=mapServerRunErrorsListOutputItemsServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapServerRunErrorsListOutputItemsServerRunServerSession.from_dict(
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
    value: Union[ServerRunErrorsListOutputItemsServerRun, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsListOutputItems:
    return ServerRunErrorsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      metadata=data.get("metadata"),
      server_run=mapServerRunErrorsListOutputItemsServerRun.from_dict(
        data.get("server_run")
      )
      if data.get("server_run")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsListOutputPagination:
    return ServerRunErrorsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsListOutput:
    return ServerRunErrorsListOutput(
      items=[
        mapServerRunErrorsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServerRunErrorsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServerRunErrorsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  server_session_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  server_deployment_id: Optional[Union[str, List[str]]] = None
  server_run_id: Optional[Union[str, List[str]]] = None
  server_run_error_group_id: Optional[Union[str, List[str]]] = None


class mapServerRunErrorsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsListQuery:
    return ServerRunErrorsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      server_session_id=data.get("server_session_id"),
      server_implementation_id=data.get("server_implementation_id"),
      server_deployment_id=data.get("server_deployment_id"),
      server_run_id=data.get("server_run_id"),
      server_run_error_group_id=data.get("server_run_error_group_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
