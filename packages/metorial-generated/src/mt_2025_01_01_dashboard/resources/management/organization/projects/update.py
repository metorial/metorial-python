from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ManagementOrganizationProjectsUpdateOutput:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


class mapManagementOrganizationProjectsUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationProjectsUpdateOutput:
    return ManagementOrganizationProjectsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationProjectsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationProjectsUpdateBody:
  name: Optional[str] = None


class mapManagementOrganizationProjectsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationProjectsUpdateBody:
    return ManagementOrganizationProjectsUpdateBody(name=data.get("name"))

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationProjectsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
