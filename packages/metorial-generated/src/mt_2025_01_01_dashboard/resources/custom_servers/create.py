from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersCreateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersCreateOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class CustomServersCreateOutput:
  object: str
  id: str
  status: str
  type: str
  publication_status: str
  name: str
  metadata: Dict[str, Any]
  server: CustomServersCreateOutputServer
  server_variant: CustomServersCreateOutputServerVariant
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  current_version_id: Optional[str] = None
  deleted_at: Optional[datetime] = None


class mapCustomServersCreateOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersCreateOutputServer:
    return CustomServersCreateOutputServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersCreateOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersCreateOutputServerVariant:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersCreateOutputServerVariant:
    return CustomServersCreateOutputServerVariant(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      source=data.get("source"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersCreateOutputServerVariant, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersCreateOutput:
    return CustomServersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      publication_status=data.get("publication_status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      server=mapCustomServersCreateOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_variant=mapCustomServersCreateOutputServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      current_version_id=data.get("current_version_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      deleted_at=datetime.fromisoformat(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersCreateBody:
  name: str
  implementation: Dict[str, Any]
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None


class mapCustomServersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersCreateBody:
    return CustomServersCreateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      implementation=data.get("implementation"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
