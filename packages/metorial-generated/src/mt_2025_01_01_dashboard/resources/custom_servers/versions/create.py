from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersVersionsCreateOutputServerVersionServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersVersionsCreateOutputServerVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: Dict[str, Any]
  server: CustomServersVersionsCreateOutputServerVersionServer
  created_at: datetime


@dataclass
class CustomServersVersionsCreateOutputServerInstanceRemoteServerProviderOauth:
  config: Dict[str, Any]
  scopes: List[str]


@dataclass
class CustomServersVersionsCreateOutputServerInstanceRemoteServer:
  object: str
  id: str
  remote_url: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[
    CustomServersVersionsCreateOutputServerInstanceRemoteServerProviderOauth
  ] = None


@dataclass
class CustomServersVersionsCreateOutputServerInstanceManagedServerProviderOauth:
  config: Dict[str, Any]
  scopes: List[str]


@dataclass
class CustomServersVersionsCreateOutputServerInstanceManagedServer:
  object: str
  id: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[
    CustomServersVersionsCreateOutputServerInstanceManagedServerProviderOauth
  ] = None


@dataclass
class CustomServersVersionsCreateOutputServerInstance:
  type: str
  remote_server: Optional[
    CustomServersVersionsCreateOutputServerInstanceRemoteServer
  ] = None
  managed_server: Optional[
    CustomServersVersionsCreateOutputServerInstanceManagedServer
  ] = None


@dataclass
class CustomServersVersionsCreateOutput:
  object: str
  id: str
  status: str
  type: str
  is_current: bool
  version_index: float
  server_instance: CustomServersVersionsCreateOutputServerInstance
  custom_server_id: str
  created_at: datetime
  updated_at: datetime
  version_hash: str
  server_version: Optional[CustomServersVersionsCreateOutputServerVersion] = None
  deployment_id: Optional[str] = None


class mapCustomServersVersionsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsCreateOutput:
    return CustomServersVersionsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      is_current=data.get("is_current"),
      version_index=data.get("version_index"),
      server_version=mapCustomServersVersionsCreateOutputServerVersion.from_dict(
        data.get("server_version")
      )
      if data.get("server_version")
      else None,
      server_instance=mapCustomServersVersionsCreateOutputServerInstance.from_dict(
        data.get("server_instance")
      )
      if data.get("server_instance")
      else None,
      custom_server_id=data.get("custom_server_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      version_hash=data.get("version_hash"),
      deployment_id=data.get("deployment_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersVersionsCreateBody:
  implementation: Dict[str, Any]


class mapCustomServersVersionsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsCreateBody:
    return CustomServersVersionsCreateBody(implementation=data.get("implementation"))

  @staticmethod
  def to_dict(
    value: Union[CustomServersVersionsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
