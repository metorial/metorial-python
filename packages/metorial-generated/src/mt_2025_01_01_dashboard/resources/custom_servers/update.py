from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersUpdateOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class CustomServersUpdateOutput:
  object: str
  id: str
  status: str
  type: str
  publication_status: str
  name: str
  metadata: Dict[str, Any]
  server: CustomServersUpdateOutputServer
  server_variant: CustomServersUpdateOutputServerVariant
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  current_version_id: Optional[str] = None
  deleted_at: Optional[datetime] = None


class mapCustomServersUpdateOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersUpdateOutputServer:
    return CustomServersUpdateOutputServer(
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
    value: Union[CustomServersUpdateOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersUpdateOutputServerVariant:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersUpdateOutputServerVariant:
    return CustomServersUpdateOutputServerVariant(
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
    value: Union[CustomServersUpdateOutputServerVariant, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersUpdateOutput:
    return CustomServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      publication_status=data.get("publication_status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      server=mapCustomServersUpdateOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_variant=mapCustomServersUpdateOutputServerVariant.from_dict(
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
    value: Union[CustomServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None


class mapCustomServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersUpdateBody:
    return CustomServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
