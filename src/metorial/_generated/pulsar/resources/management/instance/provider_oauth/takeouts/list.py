from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceProviderOauthTakeoutsListOutputItems:
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
class ManagementInstanceProviderOauthTakeoutsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceProviderOauthTakeoutsListOutput:
  items: List[ManagementInstanceProviderOauthTakeoutsListOutputItems]
  pagination: ManagementInstanceProviderOauthTakeoutsListOutputPagination


class mapManagementInstanceProviderOauthTakeoutsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthTakeoutsListOutputItems:
    return ManagementInstanceProviderOauthTakeoutsListOutputItems(
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
    value: Union[
      ManagementInstanceProviderOauthTakeoutsListOutputItems, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceProviderOauthTakeoutsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthTakeoutsListOutputPagination:
    return ManagementInstanceProviderOauthTakeoutsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceProviderOauthTakeoutsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceProviderOauthTakeoutsListOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthTakeoutsListOutput:
    return ManagementInstanceProviderOauthTakeoutsListOutput(
      items=[
        mapManagementInstanceProviderOauthTakeoutsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementInstanceProviderOauthTakeoutsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceProviderOauthTakeoutsListOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceProviderOauthTakeoutsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapManagementInstanceProviderOauthTakeoutsListQuery:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthTakeoutsListQuery:
    return ManagementInstanceProviderOauthTakeoutsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceProviderOauthTakeoutsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
