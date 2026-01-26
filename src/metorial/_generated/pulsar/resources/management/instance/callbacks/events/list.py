from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  error_code: Optional[str] = None
  error_message: Optional[str] = None


@dataclass
class ManagementInstanceCallbacksEventsListOutputItems:
  object: str
  id: str
  status: str
  payload_incoming: str
  processing_attempts: List[
    ManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts
  ]
  created_at: datetime
  type: Optional[str] = None
  payload_outgoing: Optional[str] = None


@dataclass
class ManagementInstanceCallbacksEventsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceCallbacksEventsListOutput:
  items: List[ManagementInstanceCallbacksEventsListOutputItems]
  pagination: ManagementInstanceCallbacksEventsListOutputPagination


class mapManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts:
    return ManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts(
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
      ManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksEventsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksEventsListOutputItems:
    return ManagementInstanceCallbacksEventsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      payload_incoming=data.get("payload_incoming"),
      payload_outgoing=data.get("payload_outgoing"),
      processing_attempts=[
        mapManagementInstanceCallbacksEventsListOutputItemsProcessingAttempts.from_dict(
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
    value: Union[ManagementInstanceCallbacksEventsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksEventsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksEventsListOutputPagination:
    return ManagementInstanceCallbacksEventsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksEventsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksEventsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksEventsListOutput:
    return ManagementInstanceCallbacksEventsListOutput(
      items=[
        mapManagementInstanceCallbacksEventsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementInstanceCallbacksEventsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCallbacksEventsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCallbacksEventsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceCallbacksEventsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksEventsListQuery:
    return ManagementInstanceCallbacksEventsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      callback_id=data.get("callback_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceCallbacksEventsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
