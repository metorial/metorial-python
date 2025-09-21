from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersGetOutputVariantsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersGetOutputVariantsCurrentVersionSchema:
  id: str
  fingerprint: str
  schema: Dict[str, Any]
  server_id: str
  server_variant_id: str
  server_version_id: str
  created_at: datetime


@dataclass
class ServersGetOutputVariantsCurrentVersionServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersGetOutputVariantsCurrentVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: ServersGetOutputVariantsCurrentVersionSchema
  server: ServersGetOutputVariantsCurrentVersionServer
  created_at: datetime


@dataclass
class ServersGetOutputVariants:
  object: str
  id: str
  identifier: str
  server: ServersGetOutputVariantsServer
  source: Dict[str, Any]
  created_at: datetime
  current_version: Optional[ServersGetOutputVariantsCurrentVersion] = None


@dataclass
class ServersGetOutput:
  object: str
  id: str
  type: str
  name: str
  variants: List[ServersGetOutputVariants]
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  imported_server_id: Optional[str] = None


class mapServersGetOutputVariantsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersGetOutputVariantsServer:
    return ServersGetOutputVariantsServer(
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
    value: Union[ServersGetOutputVariantsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersGetOutputVariantsCurrentVersionSchema:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersGetOutputVariantsCurrentVersionSchema:
    return ServersGetOutputVariantsCurrentVersionSchema(
      id=data.get("id"),
      fingerprint=data.get("fingerprint"),
      schema=data.get("schema"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      server_version_id=data.get("server_version_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersGetOutputVariantsCurrentVersionSchema, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersGetOutputVariantsCurrentVersionServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersGetOutputVariantsCurrentVersionServer:
    return ServersGetOutputVariantsCurrentVersionServer(
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
    value: Union[ServersGetOutputVariantsCurrentVersionServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersGetOutputVariantsCurrentVersion:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersGetOutputVariantsCurrentVersion:
    return ServersGetOutputVariantsCurrentVersion(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      get_launch_params=data.get("get_launch_params"),
      source=data.get("source"),
      schema=mapServersGetOutputVariantsCurrentVersionSchema.from_dict(
        data.get("schema")
      )
      if data.get("schema")
      else None,
      server=mapServersGetOutputVariantsCurrentVersionServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersGetOutputVariantsCurrentVersion, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersGetOutputVariants:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersGetOutputVariants:
    return ServersGetOutputVariants(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server=mapServersGetOutputVariantsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      current_version=mapServersGetOutputVariantsCurrentVersion.from_dict(
        data.get("current_version")
      )
      if data.get("current_version")
      else None,
      source=data.get("source"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersGetOutputVariants, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersGetOutput:
    return ServersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      imported_server_id=data.get("imported_server_id"),
      variants=[
        mapServersGetOutputVariants.from_dict(item)
        for item in data.get("variants", [])
        if item
      ],
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
