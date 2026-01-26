from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationTeamsMembersCreateOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  permissions: List[str]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementOrganizationTeamsMembersCreateOutputProjectsRoles:
  id: str
  role: ManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationTeamsMembersCreateOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: ManagementOrganizationTeamsMembersCreateOutputProjectsProject
  roles: List[ManagementOrganizationTeamsMembersCreateOutputProjectsRoles]


@dataclass
class ManagementOrganizationTeamsMembersCreateOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[ManagementOrganizationTeamsMembersCreateOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementOrganizationTeamsMembersCreateOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersCreateOutputProjectsProject:
    return ManagementOrganizationTeamsMembersCreateOutputProjectsProject(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
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
      ManagementOrganizationTeamsMembersCreateOutputProjectsProject,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole:
    return ManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole(
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
    value: Union[
      ManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersCreateOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersCreateOutputProjectsRoles:
    return ManagementOrganizationTeamsMembersCreateOutputProjectsRoles(
      id=data.get("id"),
      role=mapManagementOrganizationTeamsMembersCreateOutputProjectsRolesRole.from_dict(
        data.get("role")
      )
      if data.get("role")
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
    value: Union[
      ManagementOrganizationTeamsMembersCreateOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersCreateOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersCreateOutputProjects:
    return ManagementOrganizationTeamsMembersCreateOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapManagementOrganizationTeamsMembersCreateOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapManagementOrganizationTeamsMembersCreateOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementOrganizationTeamsMembersCreateOutputProjects, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateOutput:
    return ManagementOrganizationTeamsMembersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapManagementOrganizationTeamsMembersCreateOutputProjects.from_dict(item)
        for item in data.get("projects", [])
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
    value: Union[ManagementOrganizationTeamsMembersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationTeamsMembersCreateBody:
  actor_id: str


class mapManagementOrganizationTeamsMembersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateBody:
    return ManagementOrganizationTeamsMembersCreateBody(actor_id=data.get("actor_id"))

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsMembersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
