from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersImplementationsListOutputItemsServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersImplementationsListOutputItemsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersImplementationsListOutputItems:
  object: str
  id: str
  status: str
  is_default: bool
  is_ephemeral: bool
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersImplementationsListOutputItemsServerVariant
  server: ServersImplementationsListOutputItemsServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


@dataclass
class ServersImplementationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersImplementationsListOutput:
  items: List[ServersImplementationsListOutputItems]
  pagination: ServersImplementationsListOutputPagination


class mapServersImplementationsListOutputItemsServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersImplementationsListOutputItemsServerVariant:
    return ServersImplementationsListOutputItemsServerVariant(
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
    value: Union[
      ServersImplementationsListOutputItemsServerVariant, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsListOutputItemsServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsListOutputItemsServer:
    return ServersImplementationsListOutputItemsServer(
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
    value: Union[ServersImplementationsListOutputItemsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsListOutputItems:
    return ServersImplementationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      is_default=data.get("is_default"),
      is_ephemeral=data.get("is_ephemeral"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersImplementationsListOutputItemsServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersImplementationsListOutputItemsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsListOutputPagination:
    return ServersImplementationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsListOutput:
    return ServersImplementationsListOutput(
      items=[
        mapServersImplementationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServersImplementationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersImplementationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_id: Optional[Union[str, List[str]]] = None
  server_variant_id: Optional[Union[str, List[str]]] = None


class mapServersImplementationsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsListQuery:
    return ServersImplementationsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
