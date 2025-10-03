from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersVariantsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersVariantsListOutputItemsCurrentVersionServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersVariantsListOutputItemsCurrentVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  get_launch_params: str
  source: Dict[str, Any]
  schema: Dict[str, Any]
  server: ServersVariantsListOutputItemsCurrentVersionServer
  created_at: datetime


@dataclass
class ServersVariantsListOutputItems:
  object: str
  id: str
  status: str
  identifier: str
  server: ServersVariantsListOutputItemsServer
  source: Dict[str, Any]
  created_at: datetime
  current_version: Optional[ServersVariantsListOutputItemsCurrentVersion] = None


@dataclass
class ServersVariantsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersVariantsListOutput:
  items: List[ServersVariantsListOutputItems]
  pagination: ServersVariantsListOutputPagination


class mapServersVariantsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsListOutputItemsServer:
    return ServersVariantsListOutputItemsServer(
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
    value: Union[ServersVariantsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsListOutputItemsCurrentVersionServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersVariantsListOutputItemsCurrentVersionServer:
    return ServersVariantsListOutputItemsCurrentVersionServer(
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
    value: Union[
      ServersVariantsListOutputItemsCurrentVersionServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsListOutputItemsCurrentVersion:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsListOutputItemsCurrentVersion:
    return ServersVariantsListOutputItemsCurrentVersion(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      get_launch_params=data.get("get_launch_params"),
      source=data.get("source"),
      schema=data.get("schema"),
      server=mapServersVariantsListOutputItemsCurrentVersionServer.from_dict(
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
    value: Union[ServersVariantsListOutputItemsCurrentVersion, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsListOutputItems:
    return ServersVariantsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      identifier=data.get("identifier"),
      server=mapServersVariantsListOutputItemsServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      current_version=mapServersVariantsListOutputItemsCurrentVersion.from_dict(
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
    value: Union[ServersVariantsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsListOutputPagination:
    return ServersVariantsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersVariantsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersVariantsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsListOutput:
    return ServersVariantsListOutput(
      items=[
        mapServersVariantsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServersVariantsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersVariantsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersVariantsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapServersVariantsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersVariantsListQuery:
    return ServersVariantsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersVariantsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
