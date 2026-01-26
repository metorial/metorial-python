from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ProviderOauthTakeoutsListOutputItems:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  note: Optional[str] = None
  access_token: Optional[str] = None
  id_token: Optional[str] = None
  scope: Optional[str] = None
  expires_at: Optional[datetime] = None


@dataclass
class ProviderOauthTakeoutsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ProviderOauthTakeoutsListOutput:
  items: List[ProviderOauthTakeoutsListOutputItems]
  pagination: ProviderOauthTakeoutsListOutputPagination


class mapProviderOauthTakeoutsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthTakeoutsListOutputItems:
    return ProviderOauthTakeoutsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      note=data.get("note"),
      metadata=data.get("metadata"),
      access_token=data.get("access_token"),
      id_token=data.get("id_token"),
      scope=data.get("scope"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      expires_at=parse_iso_datetime(data.get("expires_at"))
      if data.get("expires_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthTakeoutsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthTakeoutsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthTakeoutsListOutputPagination:
    return ProviderOauthTakeoutsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthTakeoutsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthTakeoutsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthTakeoutsListOutput:
    return ProviderOauthTakeoutsListOutput(
      items=[
        mapProviderOauthTakeoutsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapProviderOauthTakeoutsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthTakeoutsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthTakeoutsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapProviderOauthTakeoutsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthTakeoutsListQuery:
    return ProviderOauthTakeoutsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthTakeoutsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
