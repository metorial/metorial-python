from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ServerConfigVaultsListOutputItems:
  object: str
  id: str
  name: str
  metadata: Dict[str, Any]
  secret_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServerConfigVaultsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServerConfigVaultsListOutput:
  items: List[ServerConfigVaultsListOutputItems]
  pagination: ServerConfigVaultsListOutputPagination


class mapServerConfigVaultsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerConfigVaultsListOutputItems:
    return ServerConfigVaultsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerConfigVaultsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerConfigVaultsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerConfigVaultsListOutputPagination:
    return ServerConfigVaultsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerConfigVaultsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServerConfigVaultsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerConfigVaultsListOutput:
    return ServerConfigVaultsListOutput(
      items=[
        mapServerConfigVaultsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServerConfigVaultsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServerConfigVaultsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServerConfigVaultsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapServerConfigVaultsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerConfigVaultsListQuery:
    return ServerConfigVaultsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServerConfigVaultsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
