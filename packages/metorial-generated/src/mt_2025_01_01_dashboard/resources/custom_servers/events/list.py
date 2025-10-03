from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersEventsListOutputItems:
  object: str
  id: str
  type: str
  message: str
  payload: Dict[str, Any]
  custom_server_id: str
  created_at: datetime
  custom_server_version_id: Optional[str] = None


@dataclass
class CustomServersEventsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CustomServersEventsListOutput:
  items: List[CustomServersEventsListOutputItems]
  pagination: CustomServersEventsListOutputPagination


class mapCustomServersEventsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersEventsListOutputItems:
    return CustomServersEventsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      message=data.get("message"),
      payload=data.get("payload"),
      custom_server_id=data.get("custom_server_id"),
      custom_server_version_id=data.get("custom_server_version_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersEventsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersEventsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersEventsListOutputPagination:
    return CustomServersEventsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersEventsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersEventsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersEventsListOutput:
    return CustomServersEventsListOutput(
      items=[
        mapCustomServersEventsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapCustomServersEventsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersEventsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersEventsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  version_id: Optional[Union[str, List[str]]] = None


class mapCustomServersEventsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersEventsListQuery:
    return CustomServersEventsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      version_id=data.get("version_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersEventsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
