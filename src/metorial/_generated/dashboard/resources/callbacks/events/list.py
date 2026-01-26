from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CallbacksEventsListOutputItemsProcessingAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  error_code: Optional[str] = None
  error_message: Optional[str] = None


@dataclass
class CallbacksEventsListOutputItems:
  object: str
  id: str
  status: str
  payload_incoming: str
  processing_attempts: List[CallbacksEventsListOutputItemsProcessingAttempts]
  created_at: datetime
  type: Optional[str] = None
  payload_outgoing: Optional[str] = None


@dataclass
class CallbacksEventsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CallbacksEventsListOutput:
  items: List[CallbacksEventsListOutputItems]
  pagination: CallbacksEventsListOutputPagination


class mapCallbacksEventsListOutputItemsProcessingAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CallbacksEventsListOutputItemsProcessingAttempts:
    return CallbacksEventsListOutputItemsProcessingAttempts(
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
    value: Union[CallbacksEventsListOutputItemsProcessingAttempts, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksEventsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutputItems:
    return CallbacksEventsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      payload_incoming=data.get("payload_incoming"),
      payload_outgoing=data.get("payload_outgoing"),
      processing_attempts=[
        mapCallbacksEventsListOutputItemsProcessingAttempts.from_dict(item)
        for item in data.get("processing_attempts", [])
        if item
      ],
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksEventsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksEventsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutputPagination:
    return CallbacksEventsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksEventsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksEventsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutput:
    return CallbacksEventsListOutput(
      items=[
        mapCallbacksEventsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapCallbacksEventsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksEventsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CallbacksEventsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None


class mapCallbacksEventsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksEventsListQuery:
    return CallbacksEventsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      callback_id=data.get("callback_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksEventsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
