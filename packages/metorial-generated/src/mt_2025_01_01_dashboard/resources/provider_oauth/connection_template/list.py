from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionTemplateListOutputItemsProvider:
  name: str
  url: str
  image_url: str


@dataclass
class ProviderOauthConnectionTemplateListOutputItemsScopes:
  id: str
  identifier: str
  description: str


@dataclass
class ProviderOauthConnectionTemplateListOutputItemsVariables:
  id: str
  key: str
  type: str
  label: str
  description: Optional[str] = None


@dataclass
class ProviderOauthConnectionTemplateListOutputItemsProfileBadges:
  type: str
  name: str


@dataclass
class ProviderOauthConnectionTemplateListOutputItemsProfile:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[ProviderOauthConnectionTemplateListOutputItemsProfileBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ProviderOauthConnectionTemplateListOutputItems:
  object: str
  id: str
  status: str
  slug: str
  name: str
  provider: ProviderOauthConnectionTemplateListOutputItemsProvider
  scopes: List[ProviderOauthConnectionTemplateListOutputItemsScopes]
  variables: List[ProviderOauthConnectionTemplateListOutputItemsVariables]
  profile: ProviderOauthConnectionTemplateListOutputItemsProfile
  created_at: datetime
  updated_at: datetime


@dataclass
class ProviderOauthConnectionTemplateListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ProviderOauthConnectionTemplateListOutput:
  items: List[ProviderOauthConnectionTemplateListOutputItems]
  pagination: ProviderOauthConnectionTemplateListOutputPagination


class mapProviderOauthConnectionTemplateListOutputItemsProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateListOutputItemsProvider:
    return ProviderOauthConnectionTemplateListOutputItemsProvider(
      name=data.get("name"), url=data.get("url"), image_url=data.get("image_url")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateListOutputItemsProvider, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutputItemsScopes:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateListOutputItemsScopes:
    return ProviderOauthConnectionTemplateListOutputItemsScopes(
      id=data.get("id"),
      identifier=data.get("identifier"),
      description=data.get("description"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateListOutputItemsScopes, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutputItemsVariables:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateListOutputItemsVariables:
    return ProviderOauthConnectionTemplateListOutputItemsVariables(
      id=data.get("id"),
      key=data.get("key"),
      type=data.get("type"),
      label=data.get("label"),
      description=data.get("description"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateListOutputItemsVariables, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutputItemsProfileBadges:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateListOutputItemsProfileBadges:
    return ProviderOauthConnectionTemplateListOutputItemsProfileBadges(
      type=data.get("type"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateListOutputItemsProfileBadges, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutputItemsProfile:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateListOutputItemsProfile:
    return ProviderOauthConnectionTemplateListOutputItemsProfile(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      slug=data.get("slug"),
      image_url=data.get("image_url"),
      is_official=data.get("is_official"),
      is_metorial=data.get("is_metorial"),
      is_verified=data.get("is_verified"),
      badges=[
        mapProviderOauthConnectionTemplateListOutputItemsProfileBadges.from_dict(item)
        for item in data.get("badges", [])
        if item
      ],
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateListOutputItemsProfile, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateListOutputItems:
    return ProviderOauthConnectionTemplateListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      provider=mapProviderOauthConnectionTemplateListOutputItemsProvider.from_dict(
        data.get("provider")
      )
      if data.get("provider")
      else None,
      scopes=[
        mapProviderOauthConnectionTemplateListOutputItemsScopes.from_dict(item)
        for item in data.get("scopes", [])
        if item
      ],
      variables=[
        mapProviderOauthConnectionTemplateListOutputItemsVariables.from_dict(item)
        for item in data.get("variables", [])
        if item
      ],
      profile=mapProviderOauthConnectionTemplateListOutputItemsProfile.from_dict(
        data.get("profile")
      )
      if data.get("profile")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateListOutputPagination:
    return ProviderOauthConnectionTemplateListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateListOutput:
    return ProviderOauthConnectionTemplateListOutput(
      items=[
        mapProviderOauthConnectionTemplateListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapProviderOauthConnectionTemplateListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionTemplateListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  profile_id: Optional[Union[List[str], str]] = None


class mapProviderOauthConnectionTemplateListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateListQuery:
    return ProviderOauthConnectionTemplateListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      profile_id=data.get("profile_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
