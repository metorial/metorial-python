from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[
    ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient
  ] = None
  server: Optional[
    ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer
  ] = None


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp
  usage: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer
  server_deployment: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment
  server_session: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class ServerRunErrorGroupsListOutputItemsDefaultError:
  object: str
  id: str
  code: str
  message: str
  metadata: Dict[str, Any]
  server_run: ServerRunErrorGroupsListOutputItemsDefaultErrorServerRun
  created_at: datetime


@dataclass
class ServerRunErrorGroupsListOutputItems:
  object: str
  id: str
  code: str
  message: str
  fingerprint: str
  count: float
  created_at: datetime
  first_seen_at: datetime
  last_seen_at: datetime
  default_error: Optional[ServerRunErrorGroupsListOutputItemsDefaultError] = None


@dataclass
class ServerRunErrorGroupsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServerRunErrorGroupsListOutput:
  items: List[ServerRunErrorGroupsListOutputItems]
  pagination: ServerRunErrorGroupsListOutputPagination


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
    return ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer(
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
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
    return (
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer(
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
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
    return ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment(
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
      server=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
    return (
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient(
        object=data.get("object"),
        name=data.get("name"),
        version=data.get("version"),
        capabilities=data.get("capabilities"),
      )
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
    return (
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer(
        object=data.get("object"),
        name=data.get("name"),
        version=data.get("version"),
        capabilities=data.get("capabilities"),
      )
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
    return ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
    return ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage(
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
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
    return ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage.from_dict(
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
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
    return ServerRunErrorGroupsListOutputItemsDefaultErrorServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_deployment=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession.from_dict(
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
    value: Union[
      ServerRunErrorGroupsListOutputItemsDefaultErrorServerRun, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItemsDefaultError:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsListOutputItemsDefaultError:
    return ServerRunErrorGroupsListOutputItemsDefaultError(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      metadata=data.get("metadata"),
      server_run=mapServerRunErrorGroupsListOutputItemsDefaultErrorServerRun.from_dict(
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
    value: Union[ServerRunErrorGroupsListOutputItemsDefaultError, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsListOutputItems:
    return ServerRunErrorGroupsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      fingerprint=data.get("fingerprint"),
      count=data.get("count"),
      default_error=mapServerRunErrorGroupsListOutputItemsDefaultError.from_dict(
        data.get("default_error")
      )
      if data.get("default_error")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      first_seen_at=datetime.fromisoformat(data.get("first_seen_at"))
      if data.get("first_seen_at")
      else None,
      last_seen_at=datetime.fromisoformat(data.get("last_seen_at"))
      if data.get("last_seen_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorGroupsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsListOutputPagination:
    return ServerRunErrorGroupsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorGroupsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsListOutput:
    return ServerRunErrorGroupsListOutput(
      items=[
        mapServerRunErrorGroupsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServerRunErrorGroupsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorGroupsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServerRunErrorGroupsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  server_id: Optional[Union[str, List[str]]] = None


class mapServerRunErrorGroupsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsListQuery:
    return ServerRunErrorGroupsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      server_id=data.get("server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorGroupsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
