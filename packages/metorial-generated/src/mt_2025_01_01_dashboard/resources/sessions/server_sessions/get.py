from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsServerSessionsGetOutputMcpClient:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsServerSessionsGetOutputMcpServer:
  object: str
  name: str
  version: str
  capabilities: Dict[str, Any]


@dataclass
class SessionsServerSessionsGetOutputMcp:
  object: str
  version: str
  connection_type: str
  client: Optional[SessionsServerSessionsGetOutputMcpClient] = None
  server: Optional[SessionsServerSessionsGetOutputMcpServer] = None


@dataclass
class SessionsServerSessionsGetOutputUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsServerSessionsGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsServerSessionsGetOutputSessionUsage:
  total_productive_message_count: float
  total_productive_client_message_count: float
  total_productive_server_message_count: float


@dataclass
class SessionsServerSessionsGetOutputSession:
  object: str
  id: str
  status: str
  connection_status: str
  usage: SessionsServerSessionsGetOutputSessionUsage
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime


@dataclass
class SessionsServerSessionsGetOutputServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class SessionsServerSessionsGetOutputServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: SessionsServerSessionsGetOutputServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class SessionsServerSessionsGetOutputConnectionClient:
  user_agent: str
  anonymized_ip_address: str


@dataclass
class SessionsServerSessionsGetOutputConnection:
  object: str
  id: str
  client: SessionsServerSessionsGetOutputConnectionClient
  created_at: datetime
  started_at: datetime
  ended_at: Optional[datetime] = None


@dataclass
class SessionsServerSessionsGetOutput:
  object: str
  id: str
  status: str
  mcp: SessionsServerSessionsGetOutputMcp
  usage: SessionsServerSessionsGetOutputUsage
  server: SessionsServerSessionsGetOutputServer
  session: SessionsServerSessionsGetOutputSession
  server_deployment: SessionsServerSessionsGetOutputServerDeployment
  created_at: datetime
  connection: Optional[SessionsServerSessionsGetOutputConnection] = None


class mapSessionsServerSessionsGetOutputMcpClient:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputMcpClient:
    return SessionsServerSessionsGetOutputMcpClient(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsGetOutputMcpClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputMcpServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputMcpServer:
    return SessionsServerSessionsGetOutputMcpServer(
      object=data.get("object"),
      name=data.get("name"),
      version=data.get("version"),
      capabilities=data.get("capabilities"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsGetOutputMcpServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputMcp:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputMcp:
    return SessionsServerSessionsGetOutputMcp(
      object=data.get("object"),
      version=data.get("version"),
      connection_type=data.get("connection_type"),
      client=mapSessionsServerSessionsGetOutputMcpClient.from_dict(data.get("client"))
      if data.get("client")
      else None,
      server=mapSessionsServerSessionsGetOutputMcpServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsGetOutputMcp, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputUsage:
    return SessionsServerSessionsGetOutputUsage(
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
    value: Union[SessionsServerSessionsGetOutputUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputServer:
    return SessionsServerSessionsGetOutputServer(
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
    value: Union[SessionsServerSessionsGetOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputSessionUsage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputSessionUsage:
    return SessionsServerSessionsGetOutputSessionUsage(
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
    value: Union[SessionsServerSessionsGetOutputSessionUsage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputSession:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputSession:
    return SessionsServerSessionsGetOutputSession(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      connection_status=data.get("connection_status"),
      usage=mapSessionsServerSessionsGetOutputSessionUsage.from_dict(data.get("usage"))
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
    value: Union[SessionsServerSessionsGetOutputSession, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsGetOutputServerDeploymentServer:
    return SessionsServerSessionsGetOutputServerDeploymentServer(
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
      SessionsServerSessionsGetOutputServerDeploymentServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsGetOutputServerDeployment:
    return SessionsServerSessionsGetOutputServerDeployment(
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
      server=mapSessionsServerSessionsGetOutputServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsGetOutputServerDeployment, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputConnectionClient:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> SessionsServerSessionsGetOutputConnectionClient:
    return SessionsServerSessionsGetOutputConnectionClient(
      user_agent=data.get("user_agent"),
      anonymized_ip_address=data.get("anonymized_ip_address"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsServerSessionsGetOutputConnectionClient, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutputConnection:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutputConnection:
    return SessionsServerSessionsGetOutputConnection(
      object=data.get("object"),
      id=data.get("id"),
      client=mapSessionsServerSessionsGetOutputConnectionClient.from_dict(
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
    value: Union[SessionsServerSessionsGetOutputConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsServerSessionsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsServerSessionsGetOutput:
    return SessionsServerSessionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      mcp=mapSessionsServerSessionsGetOutputMcp.from_dict(data.get("mcp"))
      if data.get("mcp")
      else None,
      usage=mapSessionsServerSessionsGetOutputUsage.from_dict(data.get("usage"))
      if data.get("usage")
      else None,
      server=mapSessionsServerSessionsGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      session=mapSessionsServerSessionsGetOutputSession.from_dict(data.get("session"))
      if data.get("session")
      else None,
      server_deployment=mapSessionsServerSessionsGetOutputServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      connection=mapSessionsServerSessionsGetOutputConnection.from_dict(
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
    value: Union[SessionsServerSessionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
