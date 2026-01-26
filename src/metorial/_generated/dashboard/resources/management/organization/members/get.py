from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationMembersGetOutputActorTeams:
  id: str
  name: str
  slug: str
  assignment_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationMembersGetOutputActor:
  object: str
  id: str
  type: str
  organization_id: str
  name: str
  image_url: str
  teams: List[ManagementOrganizationMembersGetOutputActorTeams]
  created_at: datetime
  updated_at: datetime
  email: Optional[str] = None


@dataclass
class ManagementOrganizationMembersGetOutput:
  object: str
  id: str
  status: str
  role: str
  user_id: str
  organization_id: str
  actor_id: str
  actor: ManagementOrganizationMembersGetOutputActor
  last_active_at: datetime
  deleted_at: datetime
  created_at: datetime
  updated_at: datetime


class mapManagementOrganizationMembersGetOutputActorTeams:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationMembersGetOutputActorTeams:
    return ManagementOrganizationMembersGetOutputActorTeams(
      id=data.get("id"),
      name=data.get("name"),
      slug=data.get("slug"),
      assignment_id=data.get("assignment_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationMembersGetOutputActorTeams, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationMembersGetOutputActor:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersGetOutputActor:
    return ManagementOrganizationMembersGetOutputActor(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
      teams=[
        mapManagementOrganizationMembersGetOutputActorTeams.from_dict(item)
        for item in data.get("teams", [])
        if item
      ],
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationMembersGetOutputActor, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationMembersGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersGetOutput:
    return ManagementOrganizationMembersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      user_id=data.get("user_id"),
      organization_id=data.get("organization_id"),
      actor_id=data.get("actor_id"),
      actor=mapManagementOrganizationMembersGetOutputActor.from_dict(data.get("actor"))
      if data.get("actor")
      else None,
      last_active_at=parse_iso_datetime(data.get("last_active_at"))
      if data.get("last_active_at")
      else None,
      deleted_at=parse_iso_datetime(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationMembersGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
