from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination:
  url: str
  signing_secret: str


@dataclass
class DashboardInstanceCallbacksDestinationsListOutputItems:
  object: str
  id: str
  type: str
  name: str
  description: str
  callbacks: Dict[str, Any]
  created_at: datetime
  webhook_destination: Optional[
    DashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination
  ] = None


@dataclass
class DashboardInstanceCallbacksDestinationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardInstanceCallbacksDestinationsListOutput:
  items: List[DashboardInstanceCallbacksDestinationsListOutputItems]
  pagination: DashboardInstanceCallbacksDestinationsListOutputPagination


class mapDashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination:
    return DashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination(
      url=data.get("url"), signing_secret=data.get("signing_secret")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksDestinationsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsListOutputItems:
    return DashboardInstanceCallbacksDestinationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      webhook_destination=mapDashboardInstanceCallbacksDestinationsListOutputItemsWebhookDestination.from_dict(
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
      DashboardInstanceCallbacksDestinationsListOutputItems, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksDestinationsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsListOutputPagination:
    return DashboardInstanceCallbacksDestinationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksDestinationsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksDestinationsListOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsListOutput:
    return DashboardInstanceCallbacksDestinationsListOutput(
      items=[
        mapDashboardInstanceCallbacksDestinationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapDashboardInstanceCallbacksDestinationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCallbacksDestinationsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceCallbacksDestinationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  callback_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCallbacksDestinationsListQuery:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksDestinationsListQuery:
    return DashboardInstanceCallbacksDestinationsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      callback_id=data.get("callback_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCallbacksDestinationsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
