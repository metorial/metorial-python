from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsEventsListOutputItems:
  object: str
  id: str
  status: str
  type: str
  metadata: Dict[str, Any]
  connection_id: str
  created_at: datetime


@dataclass
class ProviderOauthConnectionsEventsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ProviderOauthConnectionsEventsListOutput:
  items: List[ProviderOauthConnectionsEventsListOutputItems]
  pagination: ProviderOauthConnectionsEventsListOutputPagination


class mapProviderOauthConnectionsEventsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsEventsListOutputItems:
    return ProviderOauthConnectionsEventsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      metadata=data.get("metadata"),
      connection_id=data.get("connection_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsEventsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsEventsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsEventsListOutputPagination:
    return ProviderOauthConnectionsEventsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsEventsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsEventsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsEventsListOutput:
    return ProviderOauthConnectionsEventsListOutput(
      items=[
        mapProviderOauthConnectionsEventsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapProviderOauthConnectionsEventsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsEventsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionsEventsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapProviderOauthConnectionsEventsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsEventsListQuery:
    return ProviderOauthConnectionsEventsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsEventsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
