from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServerRunErrorsGetOutputServerRunServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorsGetOutputServerRunServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunErrorsGetOutputServerRunServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServerRunErrorsGetOutputServerRunServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServerRunErrorsGetOutputServerRunServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorsGetOutputServerRunServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunErrorsGetOutputServerRunServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[ServerRunErrorsGetOutputServerRunServerSessionMcpClient] = None
  server: Optional[ServerRunErrorsGetOutputServerRunServerSessionMcpServer] = None


@dataclass
class ServerRunErrorsGetOutputServerRunServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class ServerRunErrorsGetOutputServerRunServerSession:
  object: str
  id: str
  status: str
  mcp: ServerRunErrorsGetOutputServerRunServerSessionMcp
  usage: ServerRunErrorsGetOutputServerRunServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class ServerRunErrorsGetOutputServerRun:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: ServerRunErrorsGetOutputServerRunServer
  server_deployment: ServerRunErrorsGetOutputServerRunServerDeployment
  server_session: ServerRunErrorsGetOutputServerRunServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


@dataclass
class ServerRunErrorsGetOutput:
  object: str
  id: str
  code: str
  message: str
  metadata: Dict[str, Any]
  server_run: ServerRunErrorsGetOutputServerRun
  created_at: datetime


class mapServerRunErrorsGetOutputServerRunServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsGetOutputServerRunServer:
    return ServerRunErrorsGetOutputServerRunServer(
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
    value: Union[ServerRunErrorsGetOutputServerRunServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsGetOutputServerRunServerDeploymentServer:
    return ServerRunErrorsGetOutputServerRunServerDeploymentServer(
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
      ServerRunErrorsGetOutputServerRunServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsGetOutputServerRunServerDeployment:
    return ServerRunErrorsGetOutputServerRunServerDeployment(
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
      server=mapServerRunErrorsGetOutputServerRunServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsGetOutputServerRunServerDeployment, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerSessionMcpClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsGetOutputServerRunServerSessionMcpClient:
    return ServerRunErrorsGetOutputServerRunServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsGetOutputServerRunServerSessionMcpClient, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerSessionMcpServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsGetOutputServerRunServerSessionMcpServer:
    return ServerRunErrorsGetOutputServerRunServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsGetOutputServerRunServerSessionMcpServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerSessionMcp:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsGetOutputServerRunServerSessionMcp:
    return ServerRunErrorsGetOutputServerRunServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapServerRunErrorsGetOutputServerRunServerSessionMcpClient.from_dict(
        data.get("client")
      )
      if data.get("client")
      else None,
      server=mapServerRunErrorsGetOutputServerRunServerSessionMcpServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServerRunErrorsGetOutputServerRunServerSessionMcp, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerSessionUsage:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServerRunErrorsGetOutputServerRunServerSessionUsage:
    return ServerRunErrorsGetOutputServerRunServerSessionUsage(
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
      ServerRunErrorsGetOutputServerRunServerSessionUsage, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRunServerSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsGetOutputServerRunServerSession:
    return ServerRunErrorsGetOutputServerRunServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapServerRunErrorsGetOutputServerRunServerSessionMcp.from_dict(
        data.get("mcp")
      )
      if data.get("mcp")
      else None,
      usage=mapServerRunErrorsGetOutputServerRunServerSessionUsage.from_dict(
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
    value: Union[ServerRunErrorsGetOutputServerRunServerSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutputServerRun:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsGetOutputServerRun:
    return ServerRunErrorsGetOutputServerRun(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapServerRunErrorsGetOutputServerRunServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_deployment=mapServerRunErrorsGetOutputServerRunServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapServerRunErrorsGetOutputServerRunServerSession.from_dict(
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
    value: Union[ServerRunErrorsGetOutputServerRun, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunErrorsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunErrorsGetOutput:
    return ServerRunErrorsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      code=data.get("code"),
      message=data.get("message"),
      metadata=data.get("metadata"),
      server_run=mapServerRunErrorsGetOutputServerRun.from_dict(data.get("server_run"))
      if data.get("server_run")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunErrorsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
