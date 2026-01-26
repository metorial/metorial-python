from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CallbacksListOutputItemsSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class CallbacksListOutputItems:
  object: str
  id: str
  type: str
  schedule: CallbacksListOutputItemsSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class CallbacksListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CallbacksListOutput:
  items: List[CallbacksListOutputItems]
  pagination: CallbacksListOutputPagination


class mapCallbacksListOutputItemsSchedule:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItemsSchedule:
    return CallbacksListOutputItemsSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksListOutputItemsSchedule, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItems:
    return CallbacksListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapCallbacksListOutputItemsSchedule.from_dict(data.get("schedule"))
      if data.get("schedule")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksListOutputPagination:
    return CallbacksListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksListOutput:
    return CallbacksListOutput(
      items=[
        mapCallbacksListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapCallbacksListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CallbacksListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapCallbacksListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksListQuery:
    return CallbacksListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
