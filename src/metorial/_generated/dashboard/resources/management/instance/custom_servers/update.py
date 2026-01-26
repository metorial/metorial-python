from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCustomServersUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceCustomServersUpdateOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ManagementInstanceCustomServersUpdateOutputRepository:
  object: str
  id: str
  name: str
  owner: str
  url: str
  default_branch: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementInstanceCustomServersUpdateOutput:
  object: str
  id: str
  status: str
  type: str
  publication_status: str
  name: str
  metadata: Dict[str, Any]
  server: ManagementInstanceCustomServersUpdateOutputServer
  server_variant: ManagementInstanceCustomServersUpdateOutputServerVariant
  created_at: datetime
  updated_at: datetime
  fork: Dict[str, Any]
  description: Optional[str] = None
  current_version_id: Optional[str] = None
  deleted_at: Optional[datetime] = None
  repository: Optional[ManagementInstanceCustomServersUpdateOutputRepository] = None


class mapManagementInstanceCustomServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersUpdateOutput:
    return ManagementInstanceCustomServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      publication_status=data.get("publication_status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      server=mapManagementInstanceCustomServersUpdateOutputServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_variant=mapManagementInstanceCustomServersUpdateOutputServerVariant.from_dict(
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
      repository=mapManagementInstanceCustomServersUpdateOutputRepository.from_dict(
        data.get("repository")
      )
      if data.get("repository")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCustomServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCustomServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  is_forkable: Optional[bool] = None


class mapManagementInstanceCustomServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersUpdateBody:
    return ManagementInstanceCustomServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      is_forkable=data.get("is_forkable"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCustomServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
