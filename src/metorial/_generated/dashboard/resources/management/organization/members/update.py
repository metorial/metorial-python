from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationMembersUpdateOutputActorTeams:
  id: str
  name: str
  slug: str
  assignment_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationMembersUpdateOutputActor:
  object: str
  id: str
  type: str
  organization_id: str
  name: str
  image_url: str
  teams: List[ManagementOrganizationMembersUpdateOutputActorTeams]
  created_at: datetime
  updated_at: datetime
  email: Optional[str] = None


@dataclass
class ManagementOrganizationMembersUpdateOutput:
  object: str
  id: str
  status: str
  role: str
  user_id: str
  organization_id: str
  actor_id: str
  actor: ManagementOrganizationMembersUpdateOutputActor
  last_active_at: datetime
  deleted_at: datetime
  created_at: datetime
  updated_at: datetime


class mapManagementOrganizationMembersUpdateOutputActorTeams:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationMembersUpdateOutputActorTeams:
    return ManagementOrganizationMembersUpdateOutputActorTeams(
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
      ManagementOrganizationMembersUpdateOutputActorTeams, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationMembersUpdateOutputActor:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersUpdateOutputActor:
    return ManagementOrganizationMembersUpdateOutputActor(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
      teams=[
        mapManagementOrganizationMembersUpdateOutputActorTeams.from_dict(item)
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
    value: Union[ManagementOrganizationMembersUpdateOutputActor, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationMembersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersUpdateOutput:
    return ManagementOrganizationMembersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      user_id=data.get("user_id"),
      organization_id=data.get("organization_id"),
      actor_id=data.get("actor_id"),
      actor=mapManagementOrganizationMembersUpdateOutputActor.from_dict(
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
    value: Union[ManagementOrganizationMembersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationMembersUpdateBody:
  role: str


class mapManagementOrganizationMembersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationMembersUpdateBody:
    return ManagementOrganizationMembersUpdateBody(role=data.get("role"))

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationMembersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
