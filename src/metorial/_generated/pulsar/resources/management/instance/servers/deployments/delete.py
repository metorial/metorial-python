from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputOauthConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider
  config: Dict[str, Any]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputCallback:
  object: str
  id: str
  type: str
  schedule: ManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputConfig:
  object: str
  id: str
  status: str
  secret_id: str
  created_at: datetime


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputServerImplementation:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant
  server: ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutputAccess:
  ip_allowlist: Dict[str, Any]


@dataclass
class ManagementInstanceServersDeploymentsDeleteOutput:
  object: str
  id: str
  status: str
  name: str
  result: Dict[str, Any]
  metadata: Dict[str, Any]
  secret_id: str
  server: ManagementInstanceServersDeploymentsDeleteOutputServer
  config: ManagementInstanceServersDeploymentsDeleteOutputConfig
  server_implementation: ManagementInstanceServersDeploymentsDeleteOutputServerImplementation
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  oauth_connection: Optional[
    ManagementInstanceServersDeploymentsDeleteOutputOauthConnection
  ] = None
  callback: Optional[ManagementInstanceServersDeploymentsDeleteOutputCallback] = None
  access: Optional[ManagementInstanceServersDeploymentsDeleteOutputAccess] = None


class mapManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider:
    return ManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputOauthConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputOauthConnection:
    return ManagementInstanceServersDeploymentsDeleteOutputOauthConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapManagementInstanceServersDeploymentsDeleteOutputOauthConnectionProvider.from_dict(
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
      ManagementInstanceServersDeploymentsDeleteOutputOauthConnection,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule:
    return ManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputCallback:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputCallback:
    return ManagementInstanceServersDeploymentsDeleteOutputCallback(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapManagementInstanceServersDeploymentsDeleteOutputCallbackSchedule.from_dict(
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
      ManagementInstanceServersDeploymentsDeleteOutputCallback, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputServer:
    return ManagementInstanceServersDeploymentsDeleteOutputServer(
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
      ManagementInstanceServersDeploymentsDeleteOutputServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputConfig:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputConfig:
    return ManagementInstanceServersDeploymentsDeleteOutputConfig(
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
      ManagementInstanceServersDeploymentsDeleteOutputConfig, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant:
    return (
      ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant(
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
      ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer:
    return ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer(
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
      ManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputServerImplementation:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputServerImplementation:
    return ManagementInstanceServersDeploymentsDeleteOutputServerImplementation(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapManagementInstanceServersDeploymentsDeleteOutputServerImplementationServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapManagementInstanceServersDeploymentsDeleteOutputServerImplementationServer.from_dict(
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
      ManagementInstanceServersDeploymentsDeleteOutputServerImplementation,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutputAccess:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutputAccess:
    return ManagementInstanceServersDeploymentsDeleteOutputAccess(
      ip_allowlist=data.get("ip_allowlist")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceServersDeploymentsDeleteOutputAccess, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceServersDeploymentsDeleteOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceServersDeploymentsDeleteOutput:
    return ManagementInstanceServersDeploymentsDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      oauth_connection=mapManagementInstanceServersDeploymentsDeleteOutputOauthConnection.from_dict(
        data.get("oauth_connection")
      )
      if data.get("oauth_connection")
      else None,
      callback=mapManagementInstanceServersDeploymentsDeleteOutputCallback.from_dict(
        data.get("callback")
      )
      if data.get("callback")
      else None,
      result=data.get("result"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      server=mapManagementInstanceServersDeploymentsDeleteOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      config=mapManagementInstanceServersDeploymentsDeleteOutputConfig.from_dict(
        data.get("config")
      )
      if data.get("config")
      else None,
      server_implementation=mapManagementInstanceServersDeploymentsDeleteOutputServerImplementation.from_dict(
        data.get("server_implementation")
      )
      if data.get("server_implementation")
      else None,
      access=mapManagementInstanceServersDeploymentsDeleteOutputAccess.from_dict(
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
    value: Union[ManagementInstanceServersDeploymentsDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
