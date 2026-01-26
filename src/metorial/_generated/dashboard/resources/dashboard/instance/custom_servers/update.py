from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCustomServersUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceCustomServersUpdateOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class DashboardInstanceCustomServersUpdateOutputRepository:
  object: str
  id: str
  name: str
  owner: str
  url: str
  default_branch: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardInstanceCustomServersUpdateOutput:
  object: str
  id: str
  status: str
  type: str
  publication_status: str
  name: str
  metadata: Dict[str, Any]
  server: DashboardInstanceCustomServersUpdateOutputServer
  server_variant: DashboardInstanceCustomServersUpdateOutputServerVariant
  created_at: datetime
  updated_at: datetime
  fork: Dict[str, Any]
  description: Optional[str] = None
  current_version_id: Optional[str] = None
  deleted_at: Optional[datetime] = None
  repository: Optional[DashboardInstanceCustomServersUpdateOutputRepository] = None


class mapDashboardInstanceCustomServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersUpdateOutput:
    return DashboardInstanceCustomServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      publication_status=data.get("publication_status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      server=mapDashboardInstanceCustomServersUpdateOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_variant=mapDashboardInstanceCustomServersUpdateOutputServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      current_version_id=data.get("current_version_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      deleted_at=parse_iso_datetime(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
      fork=data.get("fork"),
      repository=mapDashboardInstanceCustomServersUpdateOutputRepository.from_dict(
        data.get("repository")
      )
      if data.get("repository")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCustomServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceCustomServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  is_forkable: Optional[bool] = None


class mapDashboardInstanceCustomServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersUpdateBody:
    return DashboardInstanceCustomServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      is_forkable=data.get("is_forkable"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCustomServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
