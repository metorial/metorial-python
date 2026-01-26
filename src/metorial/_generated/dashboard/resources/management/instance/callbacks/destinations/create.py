from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class ManagementInstanceCallbacksDestinationsCreateOutput:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    ManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination
  ] = None


class mapManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination:
    return ManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksDestinationsCreateOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksDestinationsCreateOutput:
    return ManagementInstanceCallbacksDestinationsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapManagementInstanceCallbacksDestinationsCreateOutputWebhookDestination.from_dict(
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
    value: Union[
      ManagementInstanceCallbacksDestinationsCreateOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCallbacksDestinationsCreateBody:
  name: str
  url: str
  callbacks: Dict[str, Any]
  description: Optional[str] = None


class mapManagementInstanceCallbacksDestinationsCreateBody:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksDestinationsCreateBody:
    return ManagementInstanceCallbacksDestinationsCreateBody(
      name=data.get("name"),
      description=data.get("description"),
      url=data.get("url"),
      callbacks=data.get("callbacks"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksDestinationsCreateBody, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
