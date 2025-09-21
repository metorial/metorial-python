from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsEventsGetOutputServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsGetOutputServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsGetOutputServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsEventsGetOutputServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsEventsGetOutputServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsGetOutputServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsGetOutputServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[SessionsEventsGetOutputServerRunServerSessionMcpClient] = None
  server: Optional[SessionsEventsGetOutputServerRunServerSessionMcpServer] = None


@dataclass
class SessionsEventsGetOutputServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsEventsGetOutputServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: SessionsEventsGetOutputServerRunServerSessionMcp
  usage: SessionsEventsGetOutputServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class SessionsEventsGetOutputServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: SessionsEventsGetOutputServerRunServer
  server_deployment: SessionsEventsGetOutputServerRunServerDeployment
  server_session: SessionsEventsGetOutputServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[
    SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient
  ] = None
  server: Optional[
    SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer
  ] = None


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp
  usage: SessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class SessionsEventsGetOutputServerRunErrorServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: SessionsEventsGetOutputServerRunErrorServerRunServer
  server_deployment: SessionsEventsGetOutputServerRunErrorServerRunServerDeployment
  server_session: SessionsEventsGetOutputServerRunErrorServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class SessionsEventsGetOutputServerRunError:
  object: str
  id: str
  code: str
  message: str
  metadata: Dict[str, Any]
  server_run: SessionsEventsGetOutputServerRunErrorServerRun
  created_at: datetime


@dataclass
class SessionsEventsGetOutputLogLines:
  type: str
  line: str


@dataclass
class SessionsEventsGetOutput:
  object: str
  id: str
  type: str
  session_id: str
  log_lines: List[SessionsEventsGetOutputLogLines]
  created_at: datetime
  server_run: Optional[SessionsEventsGetOutputServerRun] = None
  server_run_error: Optional[SessionsEventsGetOutputServerRunError] = None


class mapSessionsEventsGetOutputServerRunServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputServerRunServer:
    return SessionsEventsGetOutputServerRunServer(
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
    value: Union[SessionsEventsGetOutputServerRunServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunServerDeploymentServer:
    return SessionsEventsGetOutputServerRunServerDeploymentServer(
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
      SessionsEventsGetOutputServerRunServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunServerDeployment:
    return SessionsEventsGetOutputServerRunServerDeployment(
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
      server=mapSessionsEventsGetOutputServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsGetOutputServerRunServerDeployment, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunServerSessionMcpClient:
    return SessionsEventsGetOutputServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsGetOutputServerRunServerSessionMcpClient, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunServerSessionMcpServer:
    return SessionsEventsGetOutputServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsGetOutputServerRunServerSessionMcpServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunServerSessionMcp:
    return SessionsEventsGetOutputServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsEventsGetOutputServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapSessionsEventsGetOutputServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsGetOutputServerRunServerSessionMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunServerSessionUsage:
    return SessionsEventsGetOutputServerRunServerSessionUsage(
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
      SessionsEventsGetOutputServerRunServerSessionUsage, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunServerSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputServerRunServerSession:
    return SessionsEventsGetOutputServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsEventsGetOutputServerRunServerSessionMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapSessionsEventsGetOutputServerRunServerSessionUsage.from_dict(
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
    value: Union[SessionsEventsGetOutputServerRunServerSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRun:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputServerRun:
    return SessionsEventsGetOutputServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapSessionsEventsGetOutputServerRunServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_deployment=mapSessionsEventsGetOutputServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapSessionsEventsGetOutputServerRunServerSession.from_dict(
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
    value: Union[SessionsEventsGetOutputServerRun, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServer:
    return SessionsEventsGetOutputServerRunErrorServerRunServer(
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
      SessionsEventsGetOutputServerRunErrorServerRunServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer:
    return SessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer(
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
      SessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerDeployment:
    return SessionsEventsGetOutputServerRunErrorServerRunServerDeployment(
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
      server=mapSessionsEventsGetOutputServerRunErrorServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsGetOutputServerRunErrorServerRunServerDeployment,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient:
    return SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer:
    return SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp:
    return SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      SessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage:
    return SessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage(
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
      SessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRunServerSession:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsEventsGetOutputServerRunErrorServerRunServerSession:
    return SessionsEventsGetOutputServerRunErrorServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapSessionsEventsGetOutputServerRunErrorServerRunServerSessionUsage.from_dict(
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
      SessionsEventsGetOutputServerRunErrorServerRunServerSession, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunErrorServerRun:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputServerRunErrorServerRun:
    return SessionsEventsGetOutputServerRunErrorServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapSessionsEventsGetOutputServerRunErrorServerRunServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_deployment=mapSessionsEventsGetOutputServerRunErrorServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapSessionsEventsGetOutputServerRunErrorServerRunServerSession.from_dict(
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
    value: Union[SessionsEventsGetOutputServerRunErrorServerRun, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputServerRunError:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputServerRunError:
    return SessionsEventsGetOutputServerRunError(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      metadata=data.get("metadata"),
      server_run=mapSessionsEventsGetOutputServerRunErrorServerRun.from_dict(
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
    value: Union[SessionsEventsGetOutputServerRunError, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutputLogLines:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputLogLines:
    return SessionsEventsGetOutputLogLines(type=data.get("type"), line=data.get("line"))

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsGetOutputLogLines, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsEventsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutput:
    return SessionsEventsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      session_id=data.get("session_id"),
      server_run=mapSessionsEventsGetOutputServerRun.from_dict(data.get("server_run"))
      if data.get("server_run")
      else None,
      server_run_error=mapSessionsEventsGetOutputServerRunError.from_dict(
        data.get("server_run_error")
      )
      if data.get("server_run_error")
      else None,
      log_lines=[
        mapSessionsEventsGetOutputLogLines.from_dict(item)
        for item in data.get("log_lines", [])
        if item
      ],
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsEventsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
