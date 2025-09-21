from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersVariantsGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersVariantsGetOutputCurrentVersionSchema:
  id: str
  fingerprint: str
  schema: Dict[str, Any]
  server_id: str
  server_variant_id: str
  server_version_id: str
  created_at: datetime


@dataclass
class ServersVariantsGetOutputCurrentVersionServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersVariantsGetOutputCurrentVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: ServersVariantsGetOutputCurrentVersionSchema
  server: ServersVariantsGetOutputCurrentVersionServer
  created_at: datetime


@dataclass
class ServersVariantsGetOutput:
  object: str
  id: str
  identifier: str
  server: ServersVariantsGetOutputServer
  source: Dict[str, Any]
  created_at: datetime
  current_version: Optional[ServersVariantsGetOutputCurrentVersion] = None


class mapServersVariantsGetOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsGetOutputServer:
    return ServersVariantsGetOutputServer(
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
    value: Union[ServersVariantsGetOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsGetOutputCurrentVersionSchema:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsGetOutputCurrentVersionSchema:
    return ServersVariantsGetOutputCurrentVersionSchema(
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
    value: Union[ServersVariantsGetOutputCurrentVersionSchema, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsGetOutputCurrentVersionServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsGetOutputCurrentVersionServer:
    return ServersVariantsGetOutputCurrentVersionServer(
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
    value: Union[ServersVariantsGetOutputCurrentVersionServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsGetOutputCurrentVersion:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsGetOutputCurrentVersion:
    return ServersVariantsGetOutputCurrentVersion(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      get_launch_params=data.get("get_launch_params"),
      source=data.get("source"),
      schema=mapServersVariantsGetOutputCurrentVersionSchema.from_dict(
        data.get("schema")
      )
      if data.get("schema")
      else None,
      server=mapServersVariantsGetOutputCurrentVersionServer.from_dict(
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
    value: Union[ServersVariantsGetOutputCurrentVersion, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsGetOutput:
    return ServersVariantsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server=mapServersVariantsGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      current_version=mapServersVariantsGetOutputCurrentVersion.from_dict(
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
    value: Union[ServersVariantsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
