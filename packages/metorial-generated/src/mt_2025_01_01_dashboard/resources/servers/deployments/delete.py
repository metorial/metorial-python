from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersDeploymentsDeleteOutputOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ServersDeploymentsDeleteOutputOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ServersDeploymentsDeleteOutputOauthConnectionProvider
  config: Dict[str, Any]
  scopes: List[str]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ServersDeploymentsDeleteOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsDeleteOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class ServersDeploymentsDeleteOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersDeploymentsDeleteOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsDeleteOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersDeploymentsDeleteOutputServerImplementationServerVariant
  server: ServersDeploymentsDeleteOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ServersDeploymentsDeleteOutput:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: ServersDeploymentsDeleteOutputServer
  config: ServersDeploymentsDeleteOutputConfig
  server_implementation: ServersDeploymentsDeleteOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[ServersDeploymentsDeleteOutputOauthConnection] = None


class mapServersDeploymentsDeleteOutputOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsDeleteOutputOauthConnectionProvider:
    return ServersDeploymentsDeleteOutputOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersDeploymentsDeleteOutputOauthConnectionProvider, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutputOauthConnection:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsDeleteOutputOauthConnection:
    return ServersDeploymentsDeleteOutputOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapServersDeploymentsDeleteOutputOauthConnectionProvider.from_dict(
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
    value: Union[ServersDeploymentsDeleteOutputOauthConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsDeleteOutputServer:
    return ServersDeploymentsDeleteOutputServer(
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
    value: Union[ServersDeploymentsDeleteOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutputConfig:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsDeleteOutputConfig:
    return ServersDeploymentsDeleteOutputConfig(
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
    value: Union[ServersDeploymentsDeleteOutputConfig, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsDeleteOutputServerImplementationServerVariant:
    return ServersDeploymentsDeleteOutputServerImplementationServerVariant(
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
      ServersDeploymentsDeleteOutputServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsDeleteOutputServerImplementationServer:
    return ServersDeploymentsDeleteOutputServerImplementationServer(
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
      ServersDeploymentsDeleteOutputServerImplementationServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsDeleteOutputServerImplementation:
    return ServersDeploymentsDeleteOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersDeploymentsDeleteOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersDeploymentsDeleteOutputServerImplementationServer.from_dict(
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
    value: Union[
      ServersDeploymentsDeleteOutputServerImplementation, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsDeleteOutput:
    return ServersDeploymentsDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      oauth_connection=mapServersDeploymentsDeleteOutputOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      result=data.get("result"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapServersDeploymentsDeleteOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      config=mapServersDeploymentsDeleteOutputConfig.from_dict(data.get("config"))
      if data.get("config")
      else None,
      server_implementation=mapServersDeploymentsDeleteOutputServerImplementation.from_dict(
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
    value: Union[ServersDeploymentsDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
