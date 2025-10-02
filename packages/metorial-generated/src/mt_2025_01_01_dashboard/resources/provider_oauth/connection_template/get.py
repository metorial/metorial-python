from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionTemplateGetOutputProvider:
  name: str
  url: str
  image_url: str


@dataclass
class ProviderOauthConnectionTemplateGetOutputScopes:
  id: str
  identifier: str
  description: str


@dataclass
class ProviderOauthConnectionTemplateGetOutputVariables:
  id: str
  key: str
  type: str
  label: str
  description: Optional[str] = None


@dataclass
class ProviderOauthConnectionTemplateGetOutputProfileBadges:
  type: str
  name: str


@dataclass
class ProviderOauthConnectionTemplateGetOutputProfile:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[ProviderOauthConnectionTemplateGetOutputProfileBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ProviderOauthConnectionTemplateGetOutput:
  object: str
  id: str
  status: str
  slug: str
  name: str
  provider: ProviderOauthConnectionTemplateGetOutputProvider
  scopes: List[ProviderOauthConnectionTemplateGetOutputScopes]
  variables: List[ProviderOauthConnectionTemplateGetOutputVariables]
  profile: ProviderOauthConnectionTemplateGetOutputProfile
  created_at: datetime
  updated_at: datetime


class mapProviderOauthConnectionTemplateGetOutputProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateGetOutputProvider:
    return ProviderOauthConnectionTemplateGetOutputProvider(
      name=data.get("name"), url=data.get("url"), image_url=data.get("image_url")
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateGetOutputProvider, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateGetOutputScopes:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateGetOutputScopes:
    return ProviderOauthConnectionTemplateGetOutputScopes(
      id=data.get("id"),
      identifier=data.get("identifier"),
      description=data.get("description"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateGetOutputScopes, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateGetOutputVariables:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateGetOutputVariables:
    return ProviderOauthConnectionTemplateGetOutputVariables(
      id=data.get("id"),
      key=data.get("key"),
      type=data.get("type"),
      label=data.get("label"),
      description=data.get("description"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateGetOutputVariables, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateGetOutputProfileBadges:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateGetOutputProfileBadges:
    return ProviderOauthConnectionTemplateGetOutputProfileBadges(
      type=data.get("type"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionTemplateGetOutputProfileBadges, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateGetOutputProfile:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateGetOutputProfile:
    return ProviderOauthConnectionTemplateGetOutputProfile(
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
        mapProviderOauthConnectionTemplateGetOutputProfileBadges.from_dict(item)
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
    value: Union[ProviderOauthConnectionTemplateGetOutputProfile, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionTemplateGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateGetOutput:
    return ProviderOauthConnectionTemplateGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      provider=mapProviderOauthConnectionTemplateGetOutputProvider.from_dict(
        data.get("provider")
      )
      if data.get("provider")
      else None,
      scopes=[
        mapProviderOauthConnectionTemplateGetOutputScopes.from_dict(item)
        for item in data.get("scopes", [])
        if item
      ],
      variables=[
        mapProviderOauthConnectionTemplateGetOutputVariables.from_dict(item)
        for item in data.get("variables", [])
        if item
      ],
      profile=mapProviderOauthConnectionTemplateGetOutputProfile.from_dict(
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
    value: Union[ProviderOauthConnectionTemplateGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
