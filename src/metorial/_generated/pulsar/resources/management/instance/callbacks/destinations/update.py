from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class ManagementInstanceCallbacksDestinationsUpdateOutput:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    ManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination
  ] = None


class mapManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination:
    return ManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceCallbacksDestinationsUpdateOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksDestinationsUpdateOutput:
    return ManagementInstanceCallbacksDestinationsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapManagementInstanceCallbacksDestinationsUpdateOutputWebhookDestination.from_dict(
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
      ManagementInstanceCallbacksDestinationsUpdateOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceCallbacksDestinationsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None


class mapManagementInstanceCallbacksDestinationsUpdateBody:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCallbacksDestinationsUpdateBody:
    return ManagementInstanceCallbacksDestinationsUpdateBody(
      name=data.get("name"), description=data.get("description")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCallbacksDestinationsUpdateBody, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
