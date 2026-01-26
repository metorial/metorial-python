from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: DashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider
  config: Dict[str, Any]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputCallback:
  object: str
  id: str
  type: str
  schedule: DashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant
  server: DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutputAccess:
  ip_allowlist: Dict[str, Any]


@dataclass
class DashboardInstanceServersDeploymentsUpdateOutput:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: DashboardInstanceServersDeploymentsUpdateOutputServer
  config: DashboardInstanceServersDeploymentsUpdateOutputConfig
  server_implementation: DashboardInstanceServersDeploymentsUpdateOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[
    DashboardInstanceServersDeploymentsUpdateOutputOauthConnection
  ] = None
  callback: Optional[DashboardInstanceServersDeploymentsUpdateOutputCallback] = None
  access: Optional[DashboardInstanceServersDeploymentsUpdateOutputAccess] = None


class mapDashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider:
    return DashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputOauthConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputOauthConnection:
    return DashboardInstanceServersDeploymentsUpdateOutputOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapDashboardInstanceServersDeploymentsUpdateOutputOauthConnectionProvider.from_dict(
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
      DashboardInstanceServersDeploymentsUpdateOutputOauthConnection,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule:
    return DashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputCallback:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputCallback:
    return DashboardInstanceServersDeploymentsUpdateOutputCallback(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapDashboardInstanceServersDeploymentsUpdateOutputCallbackSchedule.from_dict(
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
      DashboardInstanceServersDeploymentsUpdateOutputCallback, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputServer:
    return DashboardInstanceServersDeploymentsUpdateOutputServer(
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
      DashboardInstanceServersDeploymentsUpdateOutputServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputConfig:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputConfig:
    return DashboardInstanceServersDeploymentsUpdateOutputConfig(
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
      DashboardInstanceServersDeploymentsUpdateOutputConfig, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant:
    return (
      DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant(
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
      DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer:
    return DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer(
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
      DashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputServerImplementation:
    return DashboardInstanceServersDeploymentsUpdateOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapDashboardInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapDashboardInstanceServersDeploymentsUpdateOutputServerImplementationServer.from_dict(
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
      DashboardInstanceServersDeploymentsUpdateOutputServerImplementation,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutputAccess:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutputAccess:
    return DashboardInstanceServersDeploymentsUpdateOutputAccess(
      ip_allowlist=data.get("ip_allowlist")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsUpdateOutputAccess, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateOutput:
    return DashboardInstanceServersDeploymentsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      oauth_connection=mapDashboardInstanceServersDeploymentsUpdateOutputOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      callback=mapDashboardInstanceServersDeploymentsUpdateOutputCallback.from_dict(
        data.get("callback")
      )
      if data.get("callback")
      else None,
      result=data.get("result"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapDashboardInstanceServersDeploymentsUpdateOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      config=mapDashboardInstanceServersDeploymentsUpdateOutputConfig.from_dict(
        data.get("config")
      )
      if data.get("config")
      else None,
      server_implementation=mapDashboardInstanceServersDeploymentsUpdateOutputServerImplementation.from_dict(
        data.get("server_implementation")
      )
      if data.get("server_implementation")
      else None,
      access=mapDashboardInstanceServersDeploymentsUpdateOutputAccess.from_dict(
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
    value: Union[DashboardInstanceServersDeploymentsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist:
  ip_whitelist: List[str]
  ip_blacklist: List[str]


@dataclass
class DashboardInstanceServersDeploymentsUpdateBodyAccess:
  ip_allowlist: Optional[
    DashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist
  ] = None


@dataclass
class DashboardInstanceServersDeploymentsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  config: Optional[Dict[str, Any]] = None
  access: Optional[DashboardInstanceServersDeploymentsUpdateBodyAccess] = None


class mapDashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist:
    return DashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist(
      ip_whitelist=data.get("ip_whitelist", []),
      ip_blacklist=data.get("ip_blacklist", []),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateBodyAccess:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServersDeploymentsUpdateBodyAccess:
    return DashboardInstanceServersDeploymentsUpdateBodyAccess(
      ip_allowlist=mapDashboardInstanceServersDeploymentsUpdateBodyAccessIpAllowlist.from_dict(
        data.get("ip_allowlist")
      )
      if data.get("ip_allowlist")
      else None
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceServersDeploymentsUpdateBodyAccess, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceServersDeploymentsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsUpdateBody:
    return DashboardInstanceServersDeploymentsUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      config=data.get("config"),
      access=mapDashboardInstanceServersDeploymentsUpdateBodyAccess.from_dict(
        data.get("access")
      )
      if data.get("access")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceServersDeploymentsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
