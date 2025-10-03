from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsAuthenticationsListOutputItemsError:
  code: str
  message: Optional[str] = None


@dataclass
class ProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
  id: str
  type: str
  metadata: Dict[str, Any]
  created_at: datetime


@dataclass
class ProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
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
class ProviderOauthConnectionsAuthenticationsListOutputItems:
  object: str
  id: str
  status: str
  events: List[ProviderOauthConnectionsAuthenticationsListOutputItemsEvents]
  connection_id: str
  created_at: datetime
  error: Optional[ProviderOauthConnectionsAuthenticationsListOutputItemsError] = None
  profile: Optional[
    ProviderOauthConnectionsAuthenticationsListOutputItemsProfile
  ] = None


@dataclass
class ProviderOauthConnectionsAuthenticationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ProviderOauthConnectionsAuthenticationsListOutput:
  items: List[ProviderOauthConnectionsAuthenticationsListOutputItems]
  pagination: ProviderOauthConnectionsAuthenticationsListOutputPagination


class mapProviderOauthConnectionsAuthenticationsListOutputItemsError:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListOutputItemsError:
    return ProviderOauthConnectionsAuthenticationsListOutputItemsError(
      code=data.get("code"), message=data.get("message")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsListOutputItemsError, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
    return ProviderOauthConnectionsAuthenticationsListOutputItemsEvents(
      id=data.get("id"),
      type=data.get("type"),
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsListOutputItemsEvents, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
    return ProviderOauthConnectionsAuthenticationsListOutputItemsProfile(
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
    value: Union[
      ProviderOauthConnectionsAuthenticationsListOutputItemsProfile,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListOutputItems:
    return ProviderOauthConnectionsAuthenticationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      error=mapProviderOauthConnectionsAuthenticationsListOutputItemsError.from_dict(
        data.get("error")
      )
      if data.get("error")
      else None,
      events=[
        mapProviderOauthConnectionsAuthenticationsListOutputItemsEvents.from_dict(item)
        for item in data.get("events", [])
        if item
      ],
      connection_id=data.get("connection_id"),
      profile=mapProviderOauthConnectionsAuthenticationsListOutputItemsProfile.from_dict(
        data.get("profile")
      )
      if data.get("profile")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsListOutputItems, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListOutputPagination:
    return ProviderOauthConnectionsAuthenticationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsListOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListOutput:
    return ProviderOauthConnectionsAuthenticationsListOutput(
      items=[
        mapProviderOauthConnectionsAuthenticationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapProviderOauthConnectionsAuthenticationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsListOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionsAuthenticationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapProviderOauthConnectionsAuthenticationsListQuery:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsListQuery:
    return ProviderOauthConnectionsAuthenticationsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsAuthenticationsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
