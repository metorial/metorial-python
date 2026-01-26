from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CallbacksDestinationsUpdateOutputWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class CallbacksDestinationsUpdateOutput:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    CallbacksDestinationsUpdateOutputWebhookDestination
  ] = None


class mapCallbacksDestinationsUpdateOutputWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CallbacksDestinationsUpdateOutputWebhookDestination:
    return CallbacksDestinationsUpdateOutputWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      CallbacksDestinationsUpdateOutputWebhookDestination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksDestinationsUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsUpdateOutput:
    return CallbacksDestinationsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapCallbacksDestinationsUpdateOutputWebhookDestination.from_dict(
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
    value: Union[CallbacksDestinationsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CallbacksDestinationsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None


class mapCallbacksDestinationsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsUpdateBody:
    return CallbacksDestinationsUpdateBody(
      name=data.get("name"), description=data.get("description")
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksDestinationsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
