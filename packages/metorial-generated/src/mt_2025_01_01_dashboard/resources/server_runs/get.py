from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServerRunsGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunsGetOutputServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerRunsGetOutputServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServerRunsGetOutputServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServerRunsGetOutputServerSessionMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunsGetOutputServerSessionMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class ServerRunsGetOutputServerSessionMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[ServerRunsGetOutputServerSessionMcpClient] = None
  server: Optional[ServerRunsGetOutputServerSessionMcpServer] = None


@dataclass
class ServerRunsGetOutputServerSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class ServerRunsGetOutputServerSession:
  object: str
  id: str
  status: str
  mcp: ServerRunsGetOutputServerSessionMcp
  usage: ServerRunsGetOutputServerSessionUsage
  session_id: str
  created_at: datetime


@dataclass
class ServerRunsGetOutput:
  object: str
  id: str
  type: str
  status: str
  server_version_id: str
  server: ServerRunsGetOutputServer
  server_deployment: ServerRunsGetOutputServerDeployment
  server_session: ServerRunsGetOutputServerSession
  created_at: datetime
  updated_at: datetime
  started_at: Optional[datetime] = None
  stopped_at: Optional[datetime] = None


class mapServerRunsGetOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServer:
    return ServerRunsGetOutputServer(
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
    value: Union[ServerRunsGetOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerDeploymentServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerDeploymentServer:
    return ServerRunsGetOutputServerDeploymentServer(
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
    value: Union[ServerRunsGetOutputServerDeploymentServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerDeployment:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerDeployment:
    return ServerRunsGetOutputServerDeployment(
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
      server=mapServerRunsGetOutputServerDeploymentServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsGetOutputServerDeployment, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerSessionMcpClient:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerSessionMcpClient:
    return ServerRunsGetOutputServerSessionMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsGetOutputServerSessionMcpClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerSessionMcpServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerSessionMcpServer:
    return ServerRunsGetOutputServerSessionMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsGetOutputServerSessionMcpServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerSessionMcp:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerSessionMcp:
    return ServerRunsGetOutputServerSessionMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapServerRunsGetOutputServerSessionMcpClient.from_dict(data.get("client"))
      if data.get("client")
      else None,
      server=mapServerRunsGetOutputServerSessionMcpServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsGetOutputServerSessionMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerSessionUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerSessionUsage:
    return ServerRunsGetOutputServerSessionUsage(
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
    value: Union[ServerRunsGetOutputServerSessionUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutputServerSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutputServerSession:
    return ServerRunsGetOutputServerSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapServerRunsGetOutputServerSessionMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapServerRunsGetOutputServerSessionUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      session_id=data.get("session_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerRunsGetOutputServerSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerRunsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerRunsGetOutput:
    return ServerRunsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      server_version_id=data.get("server_version_id"),
      server=mapServerRunsGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_deployment=mapServerRunsGetOutputServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      server_session=mapServerRunsGetOutputServerSession.from_dict(
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
    value: Union[ServerRunsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
