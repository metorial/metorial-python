from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class OrganizationsProfileUpdateOutputBadges:
  type: str
  name: str


@dataclass
class OrganizationsProfileUpdateOutput:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[OrganizationsProfileUpdateOutputBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapOrganizationsProfileUpdateOutputBadges:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> OrganizationsProfileUpdateOutputBadges:
    return OrganizationsProfileUpdateOutputBadges(
      type=data.get("type"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[OrganizationsProfileUpdateOutputBadges, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapOrganizationsProfileUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> OrganizationsProfileUpdateOutput:
    return OrganizationsProfileUpdateOutput(
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
        mapOrganizationsProfileUpdateOutputBadges.from_dict(item)
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
    value: Union[OrganizationsProfileUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class OrganizationsProfileUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None


class mapOrganizationsProfileUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> OrganizationsProfileUpdateBody:
    return OrganizationsProfileUpdateBody(
      name=data.get("name"), description=data.get("description")
    )

  @staticmethod
  def to_dict(
    value: Union[OrganizationsProfileUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
