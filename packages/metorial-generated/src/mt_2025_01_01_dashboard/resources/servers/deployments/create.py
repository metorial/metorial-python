from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersDeploymentsCreateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsCreateOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class ServersDeploymentsCreateOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersDeploymentsCreateOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsCreateOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersDeploymentsCreateOutputServerImplementationServerVariant
  server: ServersDeploymentsCreateOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ServersDeploymentsCreateOutput:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  secret_id: str
  server: ServersDeploymentsCreateOutputServer
  config: ServersDeploymentsCreateOutputConfig
  server_implementation: ServersDeploymentsCreateOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapServersDeploymentsCreateOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsCreateOutputServer:
    return ServersDeploymentsCreateOutputServer(
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
    value: Union[ServersDeploymentsCreateOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsCreateOutputConfig:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsCreateOutputConfig:
    return ServersDeploymentsCreateOutputConfig(
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
    value: Union[ServersDeploymentsCreateOutputConfig, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsCreateOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsCreateOutputServerImplementationServerVariant:
    return ServersDeploymentsCreateOutputServerImplementationServerVariant(
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
      ServersDeploymentsCreateOutputServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsCreateOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsCreateOutputServerImplementationServer:
    return ServersDeploymentsCreateOutputServerImplementationServer(
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
      ServersDeploymentsCreateOutputServerImplementationServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsCreateOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsCreateOutputServerImplementation:
    return ServersDeploymentsCreateOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersDeploymentsCreateOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersDeploymentsCreateOutputServerImplementationServer.from_dict(
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
      ServersDeploymentsCreateOutputServerImplementation, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsCreateOutput:
    return ServersDeploymentsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapServersDeploymentsCreateOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      config=mapServersDeploymentsCreateOutputConfig.from_dict(data.get("config"))
      if data.get("config")
      else None,
      server_implementation=mapServersDeploymentsCreateOutputServerImplementation.from_dict(
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
    value: Union[ServersDeploymentsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


ServersDeploymentsCreateBody = Any


class mapServersDeploymentsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsCreateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
