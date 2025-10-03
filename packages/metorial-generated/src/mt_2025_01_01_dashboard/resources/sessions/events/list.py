from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsEventsListOutputItemsServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsListOutputItemsServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsListOutputItemsServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsEventsListOutputItemsServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsEventsListOutputItemsServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsListOutputItemsServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsListOutputItemsServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[SessionsEventsListOutputItemsServerRunServerSessionMcpClient] = None
  server: Optional[SessionsEventsListOutputItemsServerRunServerSessionMcpServer] = None


@dataclass
class SessionsEventsListOutputItemsServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsEventsListOutputItemsServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: SessionsEventsListOutputItemsServerRunServerSessionMcp
  usage: SessionsEventsListOutputItemsServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class SessionsEventsListOutputItemsServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: SessionsEventsListOutputItemsServerRunServer
  server_deployment: SessionsEventsListOutputItemsServerRunServerDeployment
  server_session: SessionsEventsListOutputItemsServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[
    SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient
  ] = None
  server: Optional[
    SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer
  ] = None


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp
  usage: SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class SessionsEventsListOutputItemsServerRunErrorServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: SessionsEventsListOutputItemsServerRunErrorServerRunServer
  server_deployment: SessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment
  server_session: SessionsEventsListOutputItemsServerRunErrorServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class SessionsEventsListOutputItemsServerRunError:
  object: str
  id: str
  code: str
  message: str
  metadata: Dict[str, Any]
  server_run: SessionsEventsListOutputItemsServerRunErrorServerRun
  created_at: datetime


@dataclass
class SessionsEventsListOutputItemsLogLines:
  type: str
  line: str


@dataclass
class SessionsEventsListOutputItems:
  object: str
  id: str
  type: str
  session_id: str
  log_lines: List[SessionsEventsListOutputItemsLogLines]
  created_at: datetime
  server_run: Optional[SessionsEventsListOutputItemsServerRun] = None
  server_run_error: Optional[SessionsEventsListOutputItemsServerRunError] = None


@dataclass
class SessionsEventsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SessionsEventsListOutput:
  items: List[SessionsEventsListOutputItems]
  pagination: SessionsEventsListOutputPagination


class mapSessionsEventsListOutputItemsServerRunServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsServerRunServer:
    return SessionsEventsListOutputItemsServerRunServer(
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
    value: Union[SessionsEventsListOutputItemsServerRunServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerDeploymentServer:
    return SessionsEventsListOutputItemsServerRunServerDeploymentServer(
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
      SessionsEventsListOutputItemsServerRunServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerDeployment:
    return SessionsEventsListOutputItemsServerRunServerDeployment(
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
      server=mapSessionsEventsListOutputItemsServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunServerDeployment, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerSessionMcpClient:
    return SessionsEventsListOutputItemsServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunServerSessionMcpClient, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerSessionMcpServer:
    return SessionsEventsListOutputItemsServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunServerSessionMcpServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerSessionMcp:
    return SessionsEventsListOutputItemsServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsEventsListOutputItemsServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapSessionsEventsListOutputItemsServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunServerSessionMcp, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerSessionUsage:
    return SessionsEventsListOutputItemsServerRunServerSessionUsage(
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
      SessionsEventsListOutputItemsServerRunServerSessionUsage, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunServerSession:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunServerSession:
    return SessionsEventsListOutputItemsServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsEventsListOutputItemsServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapSessionsEventsListOutputItemsServerRunServerSessionUsage.from_dict(
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
      SessionsEventsListOutputItemsServerRunServerSession, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRun:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsServerRun:
    return SessionsEventsListOutputItemsServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapSessionsEventsListOutputItemsServerRunServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_deployment=mapSessionsEventsListOutputItemsServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapSessionsEventsListOutputItemsServerRunServerSession.from_dict(
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
    value: Union[SessionsEventsListOutputItemsServerRun, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServer:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServer(
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
      SessionsEventsListOutputItemsServerRunErrorServerRunServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer(
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
      SessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment(
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
      server=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage(
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
      SessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
    return SessionsEventsListOutputItemsServerRunErrorServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage.from_dict(
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
      SessionsEventsListOutputItemsServerRunErrorServerRunServerSession,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunErrorServerRun:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsListOutputItemsServerRunErrorServerRun:
    return SessionsEventsListOutputItemsServerRunErrorServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapSessionsEventsListOutputItemsServerRunErrorServerRunServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_deployment=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapSessionsEventsListOutputItemsServerRunErrorServerRunServerSession.from_dict(
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
      SessionsEventsListOutputItemsServerRunErrorServerRun, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsServerRunError:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsServerRunError:
    return SessionsEventsListOutputItemsServerRunError(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      metadata=data.get("metadata"),
      server_run=mapSessionsEventsListOutputItemsServerRunErrorServerRun.from_dict(
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
    value: Union[SessionsEventsListOutputItemsServerRunError, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItemsLogLines:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsLogLines:
    return SessionsEventsListOutputItemsLogLines(
      type=data.get("type"), line=data.get("line")
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsListOutputItemsLogLines, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItems:
    return SessionsEventsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      session_id=data.get("session_id"),
      server_run=mapSessionsEventsListOutputItemsServerRun.from_dict(
        data.get("server_run")
      )
      if data.get("server_run")
      else None,
      server_run_error=mapSessionsEventsListOutputItemsServerRunError.from_dict(
        data.get("server_run_error")
      )
      if data.get("server_run_error")
      else None,
      log_lines=[
        mapSessionsEventsListOutputItemsLogLines.from_dict(item)
        for item in data.get("log_lines", [])
        if item
      ],
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputPagination:
    return SessionsEventsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutput:
    return SessionsEventsListOutput(
      items=[
        mapSessionsEventsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapSessionsEventsListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsEventsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  server_run_id: Optional[Union[str, List[str]]] = None
  server_session_id: Optional[Union[str, List[str]]] = None


class mapSessionsEventsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsListQuery:
    return SessionsEventsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      server_run_id=data.get("server_run_id"),
      server_session_id=data.get("server_session_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
