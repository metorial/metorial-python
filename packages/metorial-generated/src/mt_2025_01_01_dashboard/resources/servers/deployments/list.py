from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersDeploymentsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsListOutputItemsConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class ServersDeploymentsListOutputItemsServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersDeploymentsListOutputItemsServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsListOutputItemsServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersDeploymentsListOutputItemsServerImplementationServerVariant
  server: ServersDeploymentsListOutputItemsServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ServersDeploymentsListOutputItems:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  secret_id: str
  server: ServersDeploymentsListOutputItemsServer
  config: ServersDeploymentsListOutputItemsConfig
  server_implementation: ServersDeploymentsListOutputItemsServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersDeploymentsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersDeploymentsListOutput:
  items: List[ServersDeploymentsListOutputItems]
  pagination: ServersDeploymentsListOutputPagination


class mapServersDeploymentsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputItemsServer:
    return ServersDeploymentsListOutputItemsServer(
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
    value: Union[ServersDeploymentsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsConfig:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputItemsConfig:
    return ServersDeploymentsListOutputItemsConfig(
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
    value: Union[ServersDeploymentsListOutputItemsConfig, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsListOutputItemsServerImplementationServerVariant:
    return ServersDeploymentsListOutputItemsServerImplementationServerVariant(
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
      ServersDeploymentsListOutputItemsServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsListOutputItemsServerImplementationServer:
    return ServersDeploymentsListOutputItemsServerImplementationServer(
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
      ServersDeploymentsListOutputItemsServerImplementationServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsListOutputItemsServerImplementation:
    return ServersDeploymentsListOutputItemsServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersDeploymentsListOutputItemsServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersDeploymentsListOutputItemsServerImplementationServer.from_dict(
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
      ServersDeploymentsListOutputItemsServerImplementation, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputItems:
    return ServersDeploymentsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapServersDeploymentsListOutputItemsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      config=mapServersDeploymentsListOutputItemsConfig.from_dict(data.get("config"))
      if data.get("config")
      else None,
      server_implementation=mapServersDeploymentsListOutputItemsServerImplementation.from_dict(
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
    value: Union[ServersDeploymentsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputPagination:
    return ServersDeploymentsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutput:
    return ServersDeploymentsListOutput(
      items=[
        mapServersDeploymentsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServersDeploymentsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


ServersDeploymentsListQuery = Any


class mapServersDeploymentsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListQuery:
    data

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
