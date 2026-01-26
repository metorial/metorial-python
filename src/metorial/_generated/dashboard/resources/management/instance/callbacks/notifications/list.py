from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest:
  object: str
  id: str
  url: str
  request_method: str
  request_body: str
  request_headers: Dict[str, str]
  response_status: float
  response_body: str
  response_headers: Dict[str, str]
  duration: float
  created_at: datetime
  request_error: Optional[str] = None


@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  webhook_request: Optional[
    ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest
  ] = None


@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItems:
  object: str
  id: str
  type: str
  status: str
  attempts: List[ManagementInstanceCallbacksNotificationsListOutputItemsAttempts]
  created_at: datetime
  url: Optional[str] = None


@dataclass
class ManagementInstanceCallbacksNotificationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceCallbacksNotificationsListOutput:
  items: List[ManagementInstanceCallbacksNotificationsListOutputItems]
  pagination: ManagementInstanceCallbacksNotificationsListOutputPagination


class mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest:
    return (
      ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest(
        object=data.get("object"),
        id=data.get("id"),
        url=data.get("url"),
        request_method=data.get("request_method"),
        request_body=data.get("request_body"),
        request_headers=data.get("request_headers"),
        response_status=data.get("response_status"),
        response_body=data.get("response_body"),
        response_headers=data.get("response_headers"),
        request_error=data.get("request_error"),
        duration=data.get("duration"),
        created_at=parse_iso_datetime(data.get("created_at"))
        if data.get("created_at")
        else None,
      )
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksNotificationsListOutputItemsAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsListOutputItemsAttempts:
    return ManagementInstanceCallbacksNotificationsListOutputItemsAttempts(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      index=data.get("index"),
      webhook_request=mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest.from_dict(
        data.get("webhook_request")
      )
      if data.get("webhook_request")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksNotificationsListOutputItemsAttempts,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksNotificationsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsListOutputItems:
    return ManagementInstanceCallbacksNotificationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      url=data.get("url"),
      attempts=[
        mapManagementInstanceCallbacksNotificationsListOutputItemsAttempts.from_dict(
          item
        )
        for item in data.get("attempts", [])
        if item
      ],
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksNotificationsListOutputItems, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksNotificationsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsListOutputPagination:
    return ManagementInstanceCallbacksNotificationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksNotificationsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksNotificationsListOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsListOutput:
    return ManagementInstanceCallbacksNotificationsListOutput(
      items=[
        mapManagementInstanceCallbacksNotificationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementInstanceCallbacksNotificationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksNotificationsListOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCallbacksNotificationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None
  event_id: Optional[Union[str, List[str]]] = None
  destination_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceCallbacksNotificationsListQuery:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsListQuery:
    return ManagementInstanceCallbacksNotificationsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      callback_id=data.get("callback_id"),
      event_id=data.get("event_id"),
      destination_id=data.get("destination_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksNotificationsListQuery, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
