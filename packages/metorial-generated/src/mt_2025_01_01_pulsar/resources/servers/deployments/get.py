from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersDeploymentsGetOutputOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ServersDeploymentsGetOutputOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ServersDeploymentsGetOutputOauthConnectionProvider
  config: Dict[str, Any]
  scopes: List[str]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ServersDeploymentsGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsGetOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class ServersDeploymentsGetOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersDeploymentsGetOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsGetOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersDeploymentsGetOutputServerImplementationServerVariant
  server: ServersDeploymentsGetOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ServersDeploymentsGetOutput:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: ServersDeploymentsGetOutputServer
  config: ServersDeploymentsGetOutputConfig
  server_implementation: ServersDeploymentsGetOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[ServersDeploymentsGetOutputOauthConnection] = None


class mapServersDeploymentsGetOutputOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsGetOutputOauthConnectionProvider:
    return ServersDeploymentsGetOutputOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersDeploymentsGetOutputOauthConnectionProvider, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutputOauthConnection:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsGetOutputOauthConnection:
    return ServersDeploymentsGetOutputOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapServersDeploymentsGetOutputOauthConnectionProvider.from_dict(
        data.get("provider")
      )
      if data.get("provider")
      else None,
      config=data.get("config"),
      scopes=data.get("scopes", []),
      client_id=data.get("client_id"),
      instance_id=data.get("instance_id"),
      template_id=data.get("template_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsGetOutputOauthConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsGetOutputServer:
    return ServersDeploymentsGetOutputServer(
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
    value: Union[ServersDeploymentsGetOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutputConfig:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsGetOutputConfig:
    return ServersDeploymentsGetOutputConfig(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      secret_id=data.get("secret_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsGetOutputConfig, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsGetOutputServerImplementationServerVariant:
    return ServersDeploymentsGetOutputServerImplementationServerVariant(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      source=data.get("source"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersDeploymentsGetOutputServerImplementationServerVariant, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsGetOutputServerImplementationServer:
    return ServersDeploymentsGetOutputServerImplementationServer(
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
      ServersDeploymentsGetOutputServerImplementationServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsGetOutputServerImplementation:
    return ServersDeploymentsGetOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersDeploymentsGetOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersDeploymentsGetOutputServerImplementationServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsGetOutputServerImplementation, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsGetOutput:
    return ServersDeploymentsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      oauth_connection=mapServersDeploymentsGetOutputOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      result=data.get("result"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapServersDeploymentsGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      config=mapServersDeploymentsGetOutputConfig.from_dict(data.get("config"))
      if data.get("config")
      else None,
      server_implementation=mapServersDeploymentsGetOutputServerImplementation.from_dict(
        data.get("server_implementation")
      )
      if data.get("server_implementation")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
