from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersListingsCollectionsListOutputItems:
  object: str
  id: str
  name: str
  slug: str
  description: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ServersListingsCollectionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersListingsCollectionsListOutput:
  items: List[ServersListingsCollectionsListOutputItems]
  pagination: ServersListingsCollectionsListOutputPagination


class mapServersListingsCollectionsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsCollectionsListOutputItems:
    return ServersListingsCollectionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsCollectionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersListingsCollectionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsCollectionsListOutputPagination:
    return ServersListingsCollectionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsCollectionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersListingsCollectionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsCollectionsListOutput:
    return ServersListingsCollectionsListOutput(
      items=[
        mapServersListingsCollectionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapServersListingsCollectionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsCollectionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersListingsCollectionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapServersListingsCollectionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsCollectionsListQuery:
    return ServersListingsCollectionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsCollectionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
