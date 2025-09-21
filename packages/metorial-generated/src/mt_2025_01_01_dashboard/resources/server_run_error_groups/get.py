from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[
    ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient
  ] = None
  server: Optional[
    ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer
  ] = None


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp
  usage: ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class ServerRunErrorGroupsGetOutputDefaultErrorServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: ServerRunErrorGroupsGetOutputDefaultErrorServerRunServer
  server_deployment: ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment
  server_session: ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class ServerRunErrorGroupsGetOutputDefaultError:
  object: str
  id: str
  code: str
  message: str
  metadata: Dict[str, Any]
  server_run: ServerRunErrorGroupsGetOutputDefaultErrorServerRun
  created_at: datetime


@dataclass
class ServerRunErrorGroupsGetOutput:
  object: str
  id: str
  code: str
  message: str
  fingerprint: str
  count: float
  created_at: datetime
  first_seen_at: datetime
  last_seen_at: datetime
  default_error: Optional[ServerRunErrorGroupsGetOutputDefaultError] = None


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServer(
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
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer(
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
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment(
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
      server=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage(
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
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage.from_dict(
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
      ServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultErrorServerRun:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorGroupsGetOutputDefaultErrorServerRun:
    return ServerRunErrorGroupsGetOutputDefaultErrorServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_deployment=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession.from_dict(
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
      ServerRunErrorGroupsGetOutputDefaultErrorServerRun, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutputDefaultError:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsGetOutputDefaultError:
    return ServerRunErrorGroupsGetOutputDefaultError(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      metadata=data.get("metadata"),
      server_run=mapServerRunErrorGroupsGetOutputDefaultErrorServerRun.from_dict(
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
    value: Union[ServerRunErrorGroupsGetOutputDefaultError, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorGroupsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsGetOutput:
    return ServerRunErrorGroupsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      fingerprint=data.get("fingerprint"),
      count=data.get("count"),
      default_error=mapServerRunErrorGroupsGetOutputDefaultError.from_dict(
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
    value: Union[ServerRunErrorGroupsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
