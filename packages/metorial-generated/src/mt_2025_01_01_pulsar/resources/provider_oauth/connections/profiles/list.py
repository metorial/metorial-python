from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsProfilesListOutputItems:
  object: str
  id: str
  status: str
  sub: str
  connection_id: str
  created_at: datetime
  last_used_at: datetime
  updated_at: datetime
  name: Optional[str] = None
  email: Optional[str] = None


@dataclass
class ProviderOauthConnectionsProfilesListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ProviderOauthConnectionsProfilesListOutput:
  items: List[ProviderOauthConnectionsProfilesListOutputItems]
  pagination: ProviderOauthConnectionsProfilesListOutputPagination


class mapProviderOauthConnectionsProfilesListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsProfilesListOutputItems:
    return ProviderOauthConnectionsProfilesListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      sub=data.get("sub"),
      name=data.get("name"),
      email=data.get("email"),
      connection_id=data.get("connection_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      last_used_at=datetime.fromisoformat(data.get("last_used_at"))
      if data.get("last_used_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsProfilesListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsProfilesListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsProfilesListOutputPagination:
    return ProviderOauthConnectionsProfilesListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsProfilesListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsProfilesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsProfilesListOutput:
    return ProviderOauthConnectionsProfilesListOutput(
      items=[
        mapProviderOauthConnectionsProfilesListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapProviderOauthConnectionsProfilesListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsProfilesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionsProfilesListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapProviderOauthConnectionsProfilesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsProfilesListQuery:
    return ProviderOauthConnectionsProfilesListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsProfilesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
