from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class OrganizationsProfileGetOutputBadges:
  type: str
  name: str


@dataclass
class OrganizationsProfileGetOutput:
  object: str
  id: str
  name: str
  slug: str
  image_url: str
  is_official: bool
  is_metorial: bool
  is_verified: bool
  badges: List[OrganizationsProfileGetOutputBadges]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapOrganizationsProfileGetOutputBadges:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> OrganizationsProfileGetOutputBadges:
    return OrganizationsProfileGetOutputBadges(
      type=data.get("type"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[OrganizationsProfileGetOutputBadges, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapOrganizationsProfileGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> OrganizationsProfileGetOutput:
    return OrganizationsProfileGetOutput(
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
        mapOrganizationsProfileGetOutputBadges.from_dict(item)
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
    value: Union[OrganizationsProfileGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
