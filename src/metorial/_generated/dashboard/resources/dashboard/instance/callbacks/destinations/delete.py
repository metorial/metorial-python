from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class DashboardInstanceCallbacksDestinationsDeleteOutput:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    DashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination
  ] = None


class mapDashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination:
    return DashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksDestinationsDeleteOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsDeleteOutput:
    return DashboardInstanceCallbacksDestinationsDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapDashboardInstanceCallbacksDestinationsDeleteOutputWebhookDestination.from_dict(
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
      DashboardInstanceCallbacksDestinationsDeleteOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
