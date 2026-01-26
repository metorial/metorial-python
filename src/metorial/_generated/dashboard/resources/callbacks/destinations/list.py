from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CallbacksDestinationsListOutputItemsWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class CallbacksDestinationsListOutputItems:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    CallbacksDestinationsListOutputItemsWebhookDestination
  ] = None


@dataclass
class CallbacksDestinationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CallbacksDestinationsListOutput:
  items: List[CallbacksDestinationsListOutputItems]
  pagination: CallbacksDestinationsListOutputPagination


class mapCallbacksDestinationsListOutputItemsWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CallbacksDestinationsListOutputItemsWebhookDestination:
    return CallbacksDestinationsListOutputItemsWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      CallbacksDestinationsListOutputItemsWebhookDestination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksDestinationsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListOutputItems:
    return CallbacksDestinationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapCallbacksDestinationsListOutputItemsWebhookDestination.from_dict(
        data.get("webhook_destination")
      )
      if data.get("webhook_destination")
      else None,
      callbacks=data.get("callbacks"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksDestinationsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksDestinationsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListOutputPagination:
    return CallbacksDestinationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksDestinationsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksDestinationsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListOutput:
    return CallbacksDestinationsListOutput(
      items=[
        mapCallbacksDestinationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapCallbacksDestinationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksDestinationsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CallbacksDestinationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None


class mapCallbacksDestinationsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListQuery:
    return CallbacksDestinationsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      callback_id=data.get("callback_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksDestinationsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
