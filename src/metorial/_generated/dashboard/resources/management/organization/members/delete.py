from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationMembersDeleteOutputActorTeams:
  id: str
  name: str
  slug: str
  assignment_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationMembersDeleteOutputActor:
  object: str
  id: str
  type: str
  organization_id: str
  name: str
  image_url: str
  teams: List[ManagementOrganizationMembersDeleteOutputActorTeams]
  created_at: datetime
  updated_at: datetime
  email: Optional[str] = None


@dataclass
class ManagementOrganizationMembersDeleteOutput:
  object: str
  id: str
  status: str
  role: str
  user_id: str
  organization_id: str
  actor_id: str
  actor: ManagementOrganizationMembersDeleteOutputActor
  last_active_at: datetime
  deleted_at: datetime
  created_at: datetime
  updated_at: datetime


class mapManagementOrganizationMembersDeleteOutputActorTeams:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationMembersDeleteOutputActorTeams:
    return ManagementOrganizationMembersDeleteOutputActorTeams(
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
    value: Union[
      ManagementOrganizationMembersDeleteOutputActorTeams, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationMembersDeleteOutputActor:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersDeleteOutputActor:
    return ManagementOrganizationMembersDeleteOutputActor(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
      teams=[
        mapManagementOrganizationMembersDeleteOutputActorTeams.from_dict(item)
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
    value: Union[ManagementOrganizationMembersDeleteOutputActor, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationMembersDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersDeleteOutput:
    return ManagementOrganizationMembersDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      user_id=data.get("user_id"),
      organization_id=data.get("organization_id"),
      actor_id=data.get("actor_id"),
      actor=mapManagementOrganizationMembersDeleteOutputActor.from_dict(
        data.get("actor")
      )
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
    value: Union[ManagementOrganizationMembersDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
