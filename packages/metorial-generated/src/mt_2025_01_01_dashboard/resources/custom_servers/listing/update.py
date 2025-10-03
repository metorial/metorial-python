from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersListingUpdateOutputProfileBadges:
  type: str
  name: str


@dataclass
class CustomServersListingUpdateOutputProfile:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[CustomServersListingUpdateOutputProfileBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersListingUpdateOutputCategories:
  object: str
  id: str
  name: str
  slug: str
  description: str
  created_at: datetime
  updated_at: datetime


@dataclass
class CustomServersListingUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersListingUpdateOutputVendor:
  id: str
  identifier: str
  name: str
  image_url: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  attributes: Optional[Any] = None


@dataclass
class CustomServersListingUpdateOutputRepository:
  id: str
  identifier: str
  slug: str
  name: str
  provider_url: str
  website_url: str
  provider: str
  star_count: float
  fork_count: float
  watcher_count: float
  open_issues_count: float
  subscription_count: float
  default_branch: str
  license_name: str
  license_url: str
  license_spdx_id: str
  topics: List[str]
  created_at: datetime
  updated_at: datetime
  language: Optional[str] = None
  description: Optional[str] = None
  pushed_at: Optional[datetime] = None


@dataclass
class CustomServersListingUpdateOutputInstallation:
  id: str
  instance_id: str
  created_at: datetime


@dataclass
class CustomServersListingUpdateOutput:
  object: str
  id: str
  status: str
  slug: str
  image_url: str
  name: str
  description: str
  readme: str
  categories: List[CustomServersListingUpdateOutputCategories]
  skills: List[str]
  is_official: bool
  is_community: bool
  is_hostable: bool
  is_metorial: bool
  is_verified: bool
  server: CustomServersListingUpdateOutputServer
  created_at: datetime
  updated_at: datetime
  profile: Optional[CustomServersListingUpdateOutputProfile] = None
  vendor: Optional[CustomServersListingUpdateOutputVendor] = None
  repository: Optional[CustomServersListingUpdateOutputRepository] = None
  installation: Optional[CustomServersListingUpdateOutputInstallation] = None
  readme_html: Optional[str] = None


class mapCustomServersListingUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListingUpdateOutput:
    return CustomServersListingUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      image_url=data.get("image_url"),
      profile=mapCustomServersListingUpdateOutputProfile.from_dict(data.get("profile"))
      if data.get("profile")
      else None,
      name=data.get("name"),
      description=data.get("description"),
      readme=data.get("readme"),
      categories=[
        mapCustomServersListingUpdateOutputCategories.from_dict(item)
        for item in data.get("categories", [])
        if item
      ],
      skills=data.get("skills", []),
      is_official=data.get("is_official"),
      is_community=data.get("is_community"),
      is_hostable=data.get("is_hostable"),
      is_metorial=data.get("is_metorial"),
      is_verified=data.get("is_verified"),
      server=mapCustomServersListingUpdateOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      vendor=mapCustomServersListingUpdateOutputVendor.from_dict(data.get("vendor"))
      if data.get("vendor")
      else None,
      repository=mapCustomServersListingUpdateOutputRepository.from_dict(
        data.get("repository")
      )
      if data.get("repository")
      else None,
      installation=mapCustomServersListingUpdateOutputInstallation.from_dict(
        data.get("installation")
      )
      if data.get("installation")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      readme_html=data.get("readme_html"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersListingUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


CustomServersListingUpdateBody = Dict[str, Any]


class mapCustomServersListingUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListingUpdateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[CustomServersListingUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
