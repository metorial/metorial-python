from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest:
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
class DashboardInstanceCallbacksNotificationsListOutputItemsAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  webhook_request: Optional[
    DashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest
  ] = None


@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItems:
  object: str
  id: str
  type: str
  status: str
  attempts: List[DashboardInstanceCallbacksNotificationsListOutputItemsAttempts]
  created_at: datetime
  url: Optional[str] = None


@dataclass
class DashboardInstanceCallbacksNotificationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceCallbacksNotificationsListOutput:
  items: List[DashboardInstanceCallbacksNotificationsListOutputItems]
  pagination: DashboardInstanceCallbacksNotificationsListOutputPagination


class mapDashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest:
    return DashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest(
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

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksNotificationsListOutputItemsAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksNotificationsListOutputItemsAttempts:
    return DashboardInstanceCallbacksNotificationsListOutputItemsAttempts(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      index=data.get("index"),
      webhook_request=mapDashboardInstanceCallbacksNotificationsListOutputItemsAttemptsWebhookRequest.from_dict(
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
      DashboardInstanceCallbacksNotificationsListOutputItemsAttempts,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksNotificationsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksNotificationsListOutputItems:
    return DashboardInstanceCallbacksNotificationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      url=data.get("url"),
      attempts=[
        mapDashboardInstanceCallbacksNotificationsListOutputItemsAttempts.from_dict(
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
      DashboardInstanceCallbacksNotificationsListOutputItems, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksNotificationsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksNotificationsListOutputPagination:
    return DashboardInstanceCallbacksNotificationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksNotificationsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksNotificationsListOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksNotificationsListOutput:
    return DashboardInstanceCallbacksNotificationsListOutput(
      items=[
        mapDashboardInstanceCallbacksNotificationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapDashboardInstanceCallbacksNotificationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksNotificationsListOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceCallbacksNotificationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None
  event_id: Optional[Union[str, List[str]]] = None
  destination_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCallbacksNotificationsListQuery:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksNotificationsListQuery:
    return DashboardInstanceCallbacksNotificationsListQuery(
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
    value: Union[DashboardInstanceCallbacksNotificationsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
