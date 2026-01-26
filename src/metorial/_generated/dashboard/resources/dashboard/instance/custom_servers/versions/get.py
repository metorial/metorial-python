from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCustomServersVersionsGetOutputServerVersionServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceCustomServersVersionsGetOutputServerVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: Dict[str, Any]
  server: DashboardInstanceCustomServersVersionsGetOutputServerVersionServer
  created_at: datetime


@dataclass
class DashboardInstanceCustomServersVersionsGetOutputServerInstanceRemoteServer:
  object: str
  id: str
  remote_url: str
  remote_protocol: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[Dict[str, Any]] = None


@dataclass
class DashboardInstanceCustomServersVersionsGetOutputServerInstanceManagedServer:
  object: str
  id: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[Dict[str, Any]] = None


@dataclass
class DashboardInstanceCustomServersVersionsGetOutputServerInstance:
  type: str
  remote_server: Optional[
    DashboardInstanceCustomServersVersionsGetOutputServerInstanceRemoteServer
  ] = None
  managed_server: Optional[
    DashboardInstanceCustomServersVersionsGetOutputServerInstanceManagedServer
  ] = None


@dataclass
class DashboardInstanceCustomServersVersionsGetOutputPush:
  object: str
  id: str
  branch: str
  commit_sha: str
  commit_message: str
  author_email: str
  author_name: str
  created_at: datetime


@dataclass
class DashboardInstanceCustomServersVersionsGetOutput:
  object: str
  id: str
  status: str
  type: str
  is_current: bool
  version_index: float
  server_instance: DashboardInstanceCustomServersVersionsGetOutputServerInstance
  custom_server_id: str
  created_at: datetime
  updated_at: datetime
  version_hash: str
  server_version: Optional[
    DashboardInstanceCustomServersVersionsGetOutputServerVersion
  ] = None
  deployment_id: Optional[str] = None
  push: Optional[DashboardInstanceCustomServersVersionsGetOutputPush] = None


class mapDashboardInstanceCustomServersVersionsGetOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCustomServersVersionsGetOutput:
    return DashboardInstanceCustomServersVersionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      is_current=data.get("is_current"),
      version_index=data.get("version_index"),
      server_version=mapDashboardInstanceCustomServersVersionsGetOutputServerVersion.from_dict(
        data.get("server_version")
      )
      if data.get("server_version")
      else None,
      server_instance=mapDashboardInstanceCustomServersVersionsGetOutputServerInstance.from_dict(
        data.get("server_instance")
      )
      if data.get("server_instance")
      else None,
      custom_server_id=data.get("custom_server_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      version_hash=data.get("version_hash"),
      deployment_id=data.get("deployment_id"),
      push=mapDashboardInstanceCustomServersVersionsGetOutputPush.from_dict(
        data.get("push")
      )
      if data.get("push")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCustomServersVersionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
