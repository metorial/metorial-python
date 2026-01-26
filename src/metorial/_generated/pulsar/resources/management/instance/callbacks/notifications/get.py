from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest:
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
class ManagementInstanceCallbacksNotificationsGetOutputAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  webhook_request: Optional[
    ManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest
  ] = None


@dataclass
class ManagementInstanceCallbacksNotificationsGetOutput:
  object: str
  id: str
  type: str
  status: str
  attempts: List[ManagementInstanceCallbacksNotificationsGetOutputAttempts]
  created_at: datetime
  url: Optional[str] = None


class mapManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest:
    return ManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest(
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
      ManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksNotificationsGetOutputAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsGetOutputAttempts:
    return ManagementInstanceCallbacksNotificationsGetOutputAttempts(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      index=data.get("index"),
      webhook_request=mapManagementInstanceCallbacksNotificationsGetOutputAttemptsWebhookRequest.from_dict(
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
      ManagementInstanceCallbacksNotificationsGetOutputAttempts, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksNotificationsGetOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksNotificationsGetOutput:
    return ManagementInstanceCallbacksNotificationsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      url=data.get("url"),
      attempts=[
        mapManagementInstanceCallbacksNotificationsGetOutputAttempts.from_dict(item)
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
      ManagementInstanceCallbacksNotificationsGetOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
