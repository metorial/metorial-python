from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCustomServersCreateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceCustomServersCreateOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ManagementInstanceCustomServersCreateOutputRepository:
  object: str
  id: str
  name: str
  owner: str
  url: str
  default_branch: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementInstanceCustomServersCreateOutput:
  object: str
  id: str
  status: str
  type: str
  publication_status: str
  name: str
  metadata: Dict[str, Any]
  server: ManagementInstanceCustomServersCreateOutputServer
  server_variant: ManagementInstanceCustomServersCreateOutputServerVariant
  created_at: datetime
  updated_at: datetime
  fork: Dict[str, Any]
  description: Optional[str] = None
  current_version_id: Optional[str] = None
  deleted_at: Optional[datetime] = None
  repository: Optional[ManagementInstanceCustomServersCreateOutputRepository] = None


class mapManagementInstanceCustomServersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersCreateOutput:
    return ManagementInstanceCustomServersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      publication_status=data.get("publication_status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      server=mapManagementInstanceCustomServersCreateOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_variant=mapManagementInstanceCustomServersCreateOutputServerVariant.from_dict(
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
      repository=mapManagementInstanceCustomServersCreateOutputRepository.from_dict(
        data.get("repository")
      )
      if data.get("repository")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCustomServersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCustomServersCreateBody:
  name: str
  implementation: Dict[str, Any]
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceCustomServersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersCreateBody:
    return ManagementInstanceCustomServersCreateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      implementation=data.get("implementation"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCustomServersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
