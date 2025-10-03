from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersListingGetOutputProfileBadges:
  type: str
  name: str


@dataclass
class CustomServersListingGetOutputProfile:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[CustomServersListingGetOutputProfileBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersListingGetOutputCategories:
  object: str
  id: str
  name: str
  slug: str
  description: str
  created_at: datetime
  updated_at: datetime


@dataclass
class CustomServersListingGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class CustomServersListingGetOutputVendor:
  id: str
  identifier: str
  name: str
  image_url: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  attributes: Optional[Any] = None


@dataclass
class CustomServersListingGetOutputRepository:
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
class CustomServersListingGetOutputInstallation:
  id: str
  instance_id: str
  created_at: datetime


@dataclass
class CustomServersListingGetOutput:
  object: str
  id: str
  status: str
  slug: str
  image_url: str
  name: str
  description: str
  readme: str
  categories: List[CustomServersListingGetOutputCategories]
  skills: List[str]
  is_official: bool
  is_community: bool
  is_hostable: bool
  is_metorial: bool
  is_verified: bool
  server: CustomServersListingGetOutputServer
  created_at: datetime
  updated_at: datetime
  profile: Optional[CustomServersListingGetOutputProfile] = None
  vendor: Optional[CustomServersListingGetOutputVendor] = None
  repository: Optional[CustomServersListingGetOutputRepository] = None
  installation: Optional[CustomServersListingGetOutputInstallation] = None
  readme_html: Optional[str] = None


class mapCustomServersListingGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersListingGetOutput:
    return CustomServersListingGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      image_url=data.get("image_url"),
      profile=mapCustomServersListingGetOutputProfile.from_dict(data.get("profile"))
      if data.get("profile")
      else None,
      name=data.get("name"),
      description=data.get("description"),
      readme=data.get("readme"),
      categories=[
        mapCustomServersListingGetOutputCategories.from_dict(item)
        for item in data.get("categories", [])
        if item
      ],
      skills=data.get("skills", []),
      is_official=data.get("is_official"),
      is_community=data.get("is_community"),
      is_hostable=data.get("is_hostable"),
      is_metorial=data.get("is_metorial"),
      is_verified=data.get("is_verified"),
      server=mapCustomServersListingGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      vendor=mapCustomServersListingGetOutputVendor.from_dict(data.get("vendor"))
      if data.get("vendor")
      else None,
      repository=mapCustomServersListingGetOutputRepository.from_dict(
        data.get("repository")
      )
      if data.get("repository")
      else None,
      installation=mapCustomServersListingGetOutputInstallation.from_dict(
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
    value: Union[CustomServersListingGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
