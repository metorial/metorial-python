from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersGetOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class CustomServersGetOutput:
  object: str
  id: str
  status: str
  type: str
  publication_status: str
  name: str
  metadata: Dict[str, Any]
  server: CustomServersGetOutputServer
  server_variant: CustomServersGetOutputServerVariant
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  current_version_id: Optional[str] = None
  deleted_at: Optional[datetime] = None


class mapCustomServersGetOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersGetOutputServer:
    return CustomServersGetOutputServer(
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
    value: Union[CustomServersGetOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersGetOutputServerVariant:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersGetOutputServerVariant:
    return CustomServersGetOutputServerVariant(
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
    value: Union[CustomServersGetOutputServerVariant, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersGetOutput:
    return CustomServersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      publication_status=data.get("publication_status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      server=mapCustomServersGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      server_variant=mapCustomServersGetOutputServerVariant.from_dict(
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
    value: Union[CustomServersGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
