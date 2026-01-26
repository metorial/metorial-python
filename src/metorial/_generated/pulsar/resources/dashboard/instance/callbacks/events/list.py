from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  error_code: Optional[str] = None
  error_message: Optional[str] = None


@dataclass
class DashboardInstanceCallbacksEventsListOutputItems:
  object: str
  id: str
  status: str
  payload_incoming: str
  processing_attempts: List[
    DashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts
  ]
  created_at: datetime
  type: Optional[str] = None
  payload_outgoing: Optional[str] = None


@dataclass
class DashboardInstanceCallbacksEventsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceCallbacksEventsListOutput:
  items: List[DashboardInstanceCallbacksEventsListOutputItems]
  pagination: DashboardInstanceCallbacksEventsListOutputPagination


class mapDashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts:
    return DashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      index=data.get("index"),
      error_code=data.get("error_code"),
      error_message=data.get("error_message"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksEventsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksEventsListOutputItems:
    return DashboardInstanceCallbacksEventsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      payload_incoming=data.get("payload_incoming"),
      payload_outgoing=data.get("payload_outgoing"),
      processing_attempts=[
        mapDashboardInstanceCallbacksEventsListOutputItemsProcessingAttempts.from_dict(
          item
        )
        for item in data.get("processing_attempts", [])
        if item
      ],
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCallbacksEventsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksEventsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksEventsListOutputPagination:
    return DashboardInstanceCallbacksEventsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksEventsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksEventsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsListOutput:
    return DashboardInstanceCallbacksEventsListOutput(
      items=[
        mapDashboardInstanceCallbacksEventsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapDashboardInstanceCallbacksEventsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCallbacksEventsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceCallbacksEventsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCallbacksEventsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsListQuery:
    return DashboardInstanceCallbacksEventsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      callback_id=data.get("callback_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCallbacksEventsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
