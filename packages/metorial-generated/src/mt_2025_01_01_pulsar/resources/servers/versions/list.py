from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersVersionsListOutputItemsSchema:
  id: str
  fingerprint: str
  schema: Dict[str, Any]
  server_id: str
  server_variant_id: str
  server_version_id: str
  created_at: datetime


@dataclass
class ServersVersionsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersVersionsListOutputItems:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: ServersVersionsListOutputItemsSchema
  server: ServersVersionsListOutputItemsServer
  created_at: datetime


@dataclass
class ServersVersionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersVersionsListOutput:
  items: List[ServersVersionsListOutputItems]
  pagination: ServersVersionsListOutputPagination


class mapServersVersionsListOutputItemsSchema:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVersionsListOutputItemsSchema:
    return ServersVersionsListOutputItemsSchema(
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
    value: Union[ServersVersionsListOutputItemsSchema, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVersionsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVersionsListOutputItemsServer:
    return ServersVersionsListOutputItemsServer(
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
    value: Union[ServersVersionsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVersionsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVersionsListOutputItems:
    return ServersVersionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      get_launch_params=data.get("get_launch_params"),
      source=data.get("source"),
      schema=mapServersVersionsListOutputItemsSchema.from_dict(data.get("schema"))
      if data.get("schema")
      else None,
      server=mapServersVersionsListOutputItemsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersVersionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVersionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVersionsListOutputPagination:
    return ServersVersionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersVersionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVersionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVersionsListOutput:
    return ServersVersionsListOutput(
      items=[
        mapServersVersionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServersVersionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersVersionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


ServersVersionsListQuery = Any


class mapServersVersionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVersionsListQuery:
    data

  @staticmethod
  def to_dict(
    value: Union[ServersVersionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
