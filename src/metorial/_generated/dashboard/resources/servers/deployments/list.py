from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ServersDeploymentsListOutputItemsOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ServersDeploymentsListOutputItemsOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ServersDeploymentsListOutputItemsOauthConnectionProvider
  config: Dict[str, Any]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ServersDeploymentsListOutputItemsCallbackSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class ServersDeploymentsListOutputItemsCallback:
  object: str
  id: str
  type: str
  schedule: ServersDeploymentsListOutputItemsCallbackSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


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
class ServersDeploymentsListOutputItemsAccess:
  ip_allowlist: Dict[str, Any]


@dataclass
class ServersDeploymentsListOutputItems:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: ServersDeploymentsListOutputItemsServer
  config: ServersDeploymentsListOutputItemsConfig
  server_implementation: ServersDeploymentsListOutputItemsServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[ServersDeploymentsListOutputItemsOauthConnection] = None
  callback: Optional[ServersDeploymentsListOutputItemsCallback] = None
  access: Optional[ServersDeploymentsListOutputItemsAccess] = None


@dataclass
class ServersDeploymentsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersDeploymentsListOutput:
  items: List[ServersDeploymentsListOutputItems]
  pagination: ServersDeploymentsListOutputPagination


class mapServersDeploymentsListOutputItemsOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsListOutputItemsOauthConnectionProvider:
    return ServersDeploymentsListOutputItemsOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersDeploymentsListOutputItemsOauthConnectionProvider, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsOauthConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsListOutputItemsOauthConnection:
    return ServersDeploymentsListOutputItemsOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapServersDeploymentsListOutputItemsOauthConnectionProvider.from_dict(
        data.get("provider")
      )
      if data.get("provider")
      else None,
      config=data.get("config"),
      client_id=data.get("client_id"),
      instance_id=data.get("instance_id"),
      template_id=data.get("template_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsListOutputItemsOauthConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsCallbackSchedule:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersDeploymentsListOutputItemsCallbackSchedule:
    return ServersDeploymentsListOutputItemsCallbackSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersDeploymentsListOutputItemsCallbackSchedule, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsCallback:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputItemsCallback:
    return ServersDeploymentsListOutputItemsCallback(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapServersDeploymentsListOutputItemsCallbackSchedule.from_dict(
        data.get("schedule")
      )
      if data.get("schedule")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsListOutputItemsCallback, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersDeploymentsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputItemsServer:
    return ServersDeploymentsListOutputItemsServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
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
      created_at=parse_iso_datetime(data.get("created_at"))
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
      created_at=parse_iso_datetime(data.get("created_at"))
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
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
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
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
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


class mapServersDeploymentsListOutputItemsAccess:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListOutputItemsAccess:
    return ServersDeploymentsListOutputItemsAccess(
      ip_allowlist=data.get("ip_allowlist")
    )

  @staticmethod
  def to_dict(
    value: Union[ServersDeploymentsListOutputItemsAccess, Dict[str, Any], None]
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
      oauth_connection=mapServersDeploymentsListOutputItemsOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      callback=mapServersDeploymentsListOutputItemsCallback.from_dict(
        data.get("callback")
      )
      if data.get("callback")
      else None,
      result=data.get("result"),
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
      access=mapServersDeploymentsListOutputItemsAccess.from_dict(data.get("access"))
      if data.get("access")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
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


@dataclass
class ServersDeploymentsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_id: Optional[Union[str, List[str]]] = None
  server_variant_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  session_id: Optional[Union[str, List[str]]] = None
  search: Optional[str] = None


class mapServersDeploymentsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersDeploymentsListQuery:
    return ServersDeploymentsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      server_implementation_id=data.get("server_implementation_id"),
      session_id=data.get("session_id"),
      search=data.get("search"),
    )

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
