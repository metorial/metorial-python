from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CallbacksDestinationsCreateOutputWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class CallbacksDestinationsCreateOutput:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    CallbacksDestinationsCreateOutputWebhookDestination
  ] = None


class mapCallbacksDestinationsCreateOutputWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CallbacksDestinationsCreateOutputWebhookDestination:
    return CallbacksDestinationsCreateOutputWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      CallbacksDestinationsCreateOutputWebhookDestination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksDestinationsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsCreateOutput:
    return CallbacksDestinationsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapCallbacksDestinationsCreateOutputWebhookDestination.from_dict(
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
    value: Union[CallbacksDestinationsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CallbacksDestinationsCreateBody:
  name: str
  url: str
  callbacks: Dict[str, Any]
  description: Optional[str] = None


class mapCallbacksDestinationsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsCreateBody:
    return CallbacksDestinationsCreateBody(
      name=data.get("name"),
      description=data.get("description"),
      url=data.get("url"),
      callbacks=data.get("callbacks"),
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksDestinationsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
