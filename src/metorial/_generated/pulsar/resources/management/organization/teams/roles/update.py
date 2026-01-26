from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationTeamsRolesUpdateOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  permissions: List[str]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementOrganizationTeamsRolesUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsRolesUpdateOutput:
    return ManagementOrganizationTeamsRolesUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      permissions=data.get("permissions", []),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsRolesUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationTeamsRolesUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  permissions: Optional[List[str]] = None


class mapManagementOrganizationTeamsRolesUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsRolesUpdateBody:
    return ManagementOrganizationTeamsRolesUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      permissions=data.get("permissions", []),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsRolesUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
