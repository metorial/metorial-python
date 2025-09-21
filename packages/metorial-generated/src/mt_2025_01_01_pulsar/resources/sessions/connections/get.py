from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsConnectionsGetOutputMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsConnectionsGetOutputMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsConnectionsGetOutputMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[SessionsConnectionsGetOutputMcpClient] = None
  server: Optional[SessionsConnectionsGetOutputMcpServer] = None


@dataclass
class SessionsConnectionsGetOutputUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsConnectionsGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsConnectionsGetOutputSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsConnectionsGetOutputSession:
  object: str
  id: str
  status: str
  connection_status: str
  usage: SessionsConnectionsGetOutputSessionUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class SessionsConnectionsGetOutputServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsConnectionsGetOutputServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsConnectionsGetOutputServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsConnectionsGetOutput:
  object: str
  id: str
  status: str
  mcp: SessionsConnectionsGetOutputMcp
  usage: SessionsConnectionsGetOutputUsage
  server: SessionsConnectionsGetOutputServer
  session: SessionsConnectionsGetOutputSession
  server_deployment: SessionsConnectionsGetOutputServerDeployment
  created_at: datetime
  started_at: datetime
  ended_at: Optional[datetime] = None


class mapSessionsConnectionsGetOutputMcpClient:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcpClient:
    return SessionsConnectionsGetOutputMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsGetOutputMcpClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputMcpServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcpServer:
    return SessionsConnectionsGetOutputMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsGetOutputMcpServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputMcp:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcp:
    return SessionsConnectionsGetOutputMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsConnectionsGetOutputMcpClient.from_dict(data.get("client"))
      if data.get("client")
      else None,
      server=mapSessionsConnectionsGetOutputMcpServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsGetOutputMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputUsage:
    return SessionsConnectionsGetOutputUsage(
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
    value: Union[SessionsConnectionsGetOutputUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputServer:
    return SessionsConnectionsGetOutputServer(
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
    value: Union[SessionsConnectionsGetOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputSessionUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputSessionUsage:
    return SessionsConnectionsGetOutputSessionUsage(
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
    value: Union[SessionsConnectionsGetOutputSessionUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputSession:
    return SessionsConnectionsGetOutputSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      usage=mapSessionsConnectionsGetOutputSessionUsage.from_dict(data.get("usage"))
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
    value: Union[SessionsConnectionsGetOutputSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsConnectionsGetOutputServerDeploymentServer:
    return SessionsConnectionsGetOutputServerDeploymentServer(
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
      SessionsConnectionsGetOutputServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutputServerDeployment:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputServerDeployment:
    return SessionsConnectionsGetOutputServerDeployment(
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
      server=mapSessionsConnectionsGetOutputServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsConnectionsGetOutputServerDeployment, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsConnectionsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutput:
    return SessionsConnectionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsConnectionsGetOutputMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapSessionsConnectionsGetOutputUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      server=mapSessionsConnectionsGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      session=mapSessionsConnectionsGetOutputSession.from_dict(data.get("session"))
      if data.get("session")
      else None,
      server_deployment=mapSessionsConnectionsGetOutputServerDeployment.from_dict(
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
    value: Union[SessionsConnectionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
