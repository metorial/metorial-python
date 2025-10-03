from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersVersionsGetOutputServerVersionServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersVersionsGetOutputServerVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: Dict[str, Any]
  server: CustomServersVersionsGetOutputServerVersionServer
  created_at: datetime


@dataclass
class CustomServersVersionsGetOutputServerInstanceRemoteServerProviderOauth:
  config: Dict[str, Any]
  scopes: List[str]


@dataclass
class CustomServersVersionsGetOutputServerInstanceRemoteServer:
  object: str
  id: str
  remote_url: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[
    CustomServersVersionsGetOutputServerInstanceRemoteServerProviderOauth
  ] = None


@dataclass
class CustomServersVersionsGetOutputServerInstanceManagedServerProviderOauth:
  config: Dict[str, Any]
  scopes: List[str]


@dataclass
class CustomServersVersionsGetOutputServerInstanceManagedServer:
  object: str
  id: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[
    CustomServersVersionsGetOutputServerInstanceManagedServerProviderOauth
  ] = None


@dataclass
class CustomServersVersionsGetOutputServerInstance:
  type: str
  remote_server: Optional[
    CustomServersVersionsGetOutputServerInstanceRemoteServer
  ] = None
  managed_server: Optional[
    CustomServersVersionsGetOutputServerInstanceManagedServer
  ] = None


@dataclass
class CustomServersVersionsGetOutput:
  object: str
  id: str
  status: str
  type: str
  is_current: bool
  version_index: float
  server_instance: CustomServersVersionsGetOutputServerInstance
  custom_server_id: str
  created_at: datetime
  updated_at: datetime
  version_hash: str
  server_version: Optional[CustomServersVersionsGetOutputServerVersion] = None
  deployment_id: Optional[str] = None


class mapCustomServersVersionsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersVersionsGetOutput:
    return CustomServersVersionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      is_current=data.get("is_current"),
      version_index=data.get("version_index"),
      server_version=mapCustomServersVersionsGetOutputServerVersion.from_dict(
        data.get("server_version")
      )
      if data.get("server_version")
      else None,
      server_instance=mapCustomServersVersionsGetOutputServerInstance.from_dict(
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
    value: Union[CustomServersVersionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
