from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider
  config: Dict[str, Any]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputCallback:
  object: str
  id: str
  type: str
  schedule: ManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant
  server: ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutputAccess:
  ip_allowlist: Dict[str, Any]


@dataclass
class ManagementInstanceServersDeploymentsUpdateOutput:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: ManagementInstanceServersDeploymentsUpdateOutputServer
  config: ManagementInstanceServersDeploymentsUpdateOutputConfig
  server_implementation: ManagementInstanceServersDeploymentsUpdateOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[
    ManagementInstanceServersDeploymentsUpdateOutputOauthConnection
  ] = None
  callback: Optional[ManagementInstanceServersDeploymentsUpdateOutputCallback] = None
  access: Optional[ManagementInstanceServersDeploymentsUpdateOutputAccess] = None


class mapManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider:
    return ManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputOauthConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputOauthConnection:
    return ManagementInstanceServersDeploymentsUpdateOutputOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapManagementInstanceServersDeploymentsUpdateOutputOauthConnectionProvider.from_dict(
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
      ManagementInstanceServersDeploymentsUpdateOutputOauthConnection,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule:
    return ManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputCallback:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputCallback:
    return ManagementInstanceServersDeploymentsUpdateOutputCallback(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapManagementInstanceServersDeploymentsUpdateOutputCallbackSchedule.from_dict(
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
      ManagementInstanceServersDeploymentsUpdateOutputCallback, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputServer:
    return ManagementInstanceServersDeploymentsUpdateOutputServer(
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
      ManagementInstanceServersDeploymentsUpdateOutputServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputConfig:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputConfig:
    return ManagementInstanceServersDeploymentsUpdateOutputConfig(
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
      ManagementInstanceServersDeploymentsUpdateOutputConfig, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant:
    return (
      ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant(
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
      ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer:
    return ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer(
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
      ManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputServerImplementation:
    return ManagementInstanceServersDeploymentsUpdateOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapManagementInstanceServersDeploymentsUpdateOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapManagementInstanceServersDeploymentsUpdateOutputServerImplementationServer.from_dict(
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
      ManagementInstanceServersDeploymentsUpdateOutputServerImplementation,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutputAccess:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutputAccess:
    return ManagementInstanceServersDeploymentsUpdateOutputAccess(
      ip_allowlist=data.get("ip_allowlist")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsUpdateOutputAccess, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateOutput:
    return ManagementInstanceServersDeploymentsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      oauth_connection=mapManagementInstanceServersDeploymentsUpdateOutputOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      callback=mapManagementInstanceServersDeploymentsUpdateOutputCallback.from_dict(
        data.get("callback")
      )
      if data.get("callback")
      else None,
      result=data.get("result"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapManagementInstanceServersDeploymentsUpdateOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      config=mapManagementInstanceServersDeploymentsUpdateOutputConfig.from_dict(
        data.get("config")
      )
      if data.get("config")
      else None,
      server_implementation=mapManagementInstanceServersDeploymentsUpdateOutputServerImplementation.from_dict(
        data.get("server_implementation")
      )
      if data.get("server_implementation")
      else None,
      access=mapManagementInstanceServersDeploymentsUpdateOutputAccess.from_dict(
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
    value: Union[ManagementInstanceServersDeploymentsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist:
  ip_whitelist: List[str]
  ip_blacklist: List[str]


@dataclass
class ManagementInstanceServersDeploymentsUpdateBodyAccess:
  ip_allowlist: Optional[
    ManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist
  ] = None


@dataclass
class ManagementInstanceServersDeploymentsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  config: Optional[Dict[str, Any]] = None
  access: Optional[ManagementInstanceServersDeploymentsUpdateBodyAccess] = None


class mapManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist:
    return ManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist(
      ip_whitelist=data.get("ip_whitelist", []),
      ip_blacklist=data.get("ip_blacklist", []),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateBodyAccess:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsUpdateBodyAccess:
    return ManagementInstanceServersDeploymentsUpdateBodyAccess(
      ip_allowlist=mapManagementInstanceServersDeploymentsUpdateBodyAccessIpAllowlist.from_dict(
        data.get("ip_allowlist")
      )
      if data.get("ip_allowlist")
      else None
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsUpdateBodyAccess, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsUpdateBody:
    return ManagementInstanceServersDeploymentsUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      config=data.get("config"),
      access=mapManagementInstanceServersDeploymentsUpdateBodyAccess.from_dict(
        data.get("access")
      )
      if data.get("access")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceServersDeploymentsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
