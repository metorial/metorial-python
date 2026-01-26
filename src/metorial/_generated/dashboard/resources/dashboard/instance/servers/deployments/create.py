from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider
  config: Dict[str, Any]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputCallbackSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputCallback:
  object: str
  id: str
  type: str
  schedule: DashboardInstanceServersDeploymentsCreateOutputCallbackSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant
  server: DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsCreateOutputAccess:
  ip_allowlist: Dict[str, Any]


@dataclass
class DashboardInstanceServersDeploymentsCreateOutput:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: DashboardInstanceServersDeploymentsCreateOutputServer
  config: DashboardInstanceServersDeploymentsCreateOutputConfig
  server_implementation: DashboardInstanceServersDeploymentsCreateOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[
    DashboardInstanceServersDeploymentsCreateOutputOauthConnection
  ] = None
  callback: Optional[DashboardInstanceServersDeploymentsCreateOutputCallback] = None
  access: Optional[DashboardInstanceServersDeploymentsCreateOutputAccess] = None


class mapDashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
    return DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputOauthConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputOauthConnection:
    return DashboardInstanceServersDeploymentsCreateOutputOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapDashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider.from_dict(
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
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputOauthConnection,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputCallbackSchedule:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputCallbackSchedule:
    return DashboardInstanceServersDeploymentsCreateOutputCallbackSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputCallbackSchedule,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputCallback:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputCallback:
    return DashboardInstanceServersDeploymentsCreateOutputCallback(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapDashboardInstanceServersDeploymentsCreateOutputCallbackSchedule.from_dict(
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
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputCallback, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputServer:
    return DashboardInstanceServersDeploymentsCreateOutputServer(
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
      DashboardInstanceServersDeploymentsCreateOutputServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputConfig:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputConfig:
    return DashboardInstanceServersDeploymentsCreateOutputConfig(
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
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputConfig, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
    return (
      DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant(
        object=data.get("object"),
        id=data.get("id"),
        identifier=data.get("identifier"),
        server_id=data.get("server_id"),
        source=data.get("source"),
        created_at=parse_iso_datetime(data.get("created_at"))
        if data.get("created_at")
        else None,
      )
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer:
    return DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer(
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
      DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputServerImplementation:
    return DashboardInstanceServersDeploymentsCreateOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServer.from_dict(
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
      DashboardInstanceServersDeploymentsCreateOutputServerImplementation,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutputAccess:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutputAccess:
    return DashboardInstanceServersDeploymentsCreateOutputAccess(
      ip_allowlist=data.get("ip_allowlist")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsCreateOutputAccess, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsCreateOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsCreateOutput:
    return DashboardInstanceServersDeploymentsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      oauth_connection=mapDashboardInstanceServersDeploymentsCreateOutputOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      callback=mapDashboardInstanceServersDeploymentsCreateOutputCallback.from_dict(
        data.get("callback")
      )
      if data.get("callback")
      else None,
      result=data.get("result"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapDashboardInstanceServersDeploymentsCreateOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      config=mapDashboardInstanceServersDeploymentsCreateOutputConfig.from_dict(
        data.get("config")
      )
      if data.get("config")
      else None,
      server_implementation=mapDashboardInstanceServersDeploymentsCreateOutputServerImplementation.from_dict(
        data.get("server_implementation")
      )
      if data.get("server_implementation")
      else None,
      access=mapDashboardInstanceServersDeploymentsCreateOutputAccess.from_dict(
        data.get("access")
      )
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
    value: Union[DashboardInstanceServersDeploymentsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceServersDeploymentsCreateBody:
  server_implementation: Optional[Dict[str, Any]] = None
  server_implementation_id: Optional[str] = None
  server_variant_id: Optional[str] = None
  server_id: Optional[str] = None


class mapDashboardInstanceServersDeploymentsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateBody:
    return DashboardInstanceServersDeploymentsCreateBody(
      server_implementation=data.get("server_implementation"),
      server_implementation_id=data.get("server_implementation_id"),
      server_variant_id=data.get("server_variant_id"),
      server_id=data.get("server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceServersDeploymentsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
