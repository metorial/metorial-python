from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersListingsGetOutputProfileBadges:
  type: str
  name: str


@dataclass
class ServersListingsGetOutputProfile:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[ServersListingsGetOutputProfileBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersListingsGetOutputCategories:
  object: str
  id: str
  name: str
  slug: str
  description: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ServersListingsGetOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersListingsGetOutputVendor:
  id: str
  identifier: str
  name: str
  image_url: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  attributes: Optional[Any] = None


@dataclass
class ServersListingsGetOutputRepository:
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
class ServersListingsGetOutputInstallation:
  id: str
  instance_id: str
  created_at: datetime


@dataclass
class ServersListingsGetOutput:
  object: str
  id: str
  status: str
  slug: str
  image_url: str
  name: str
  description: str
  readme: str
  categories: List[ServersListingsGetOutputCategories]
  skills: List[str]
  is_official: bool
  is_community: bool
  is_hostable: bool
  is_metorial: bool
  is_verified: bool
  server: ServersListingsGetOutputServer
  created_at: datetime
  updated_at: datetime
  profile: Optional[ServersListingsGetOutputProfile] = None
  vendor: Optional[ServersListingsGetOutputVendor] = None
  repository: Optional[ServersListingsGetOutputRepository] = None
  installation: Optional[ServersListingsGetOutputInstallation] = None
  readme_html: Optional[str] = None


class mapServersListingsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsGetOutput:
    return ServersListingsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      image_url=data.get("image_url"),
      profile=mapServersListingsGetOutputProfile.from_dict(data.get("profile"))
      if data.get("profile")
      else None,
      name=data.get("name"),
      description=data.get("description"),
      readme=data.get("readme"),
      categories=[
        mapServersListingsGetOutputCategories.from_dict(item)
        for item in data.get("categories", [])
        if item
      ],
      skills=data.get("skills", []),
      is_official=data.get("is_official"),
      is_community=data.get("is_community"),
      is_hostable=data.get("is_hostable"),
      is_metorial=data.get("is_metorial"),
      is_verified=data.get("is_verified"),
      server=mapServersListingsGetOutputServer.from_dict(data.get("server"))
      if data.get("server")
      else None,
      vendor=mapServersListingsGetOutputVendor.from_dict(data.get("vendor"))
      if data.get("vendor")
      else None,
      repository=mapServersListingsGetOutputRepository.from_dict(data.get("repository"))
      if data.get("repository")
      else None,
      installation=mapServersListingsGetOutputInstallation.from_dict(
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
    value: Union[ServersListingsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersListingsGetQuery:
  instance_id: Optional[str] = None


class mapServersListingsGetQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsGetQuery:
    return ServersListingsGetQuery(instance_id=data.get("instance_id"))

  @staticmethod
  def to_dict(
    value: Union[ServersListingsGetQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
