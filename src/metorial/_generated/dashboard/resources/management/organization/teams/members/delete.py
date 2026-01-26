from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationTeamsMembersDeleteOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole:
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
class ManagementOrganizationTeamsMembersDeleteOutputProjectsRoles:
  id: str
  role: ManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationTeamsMembersDeleteOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: ManagementOrganizationTeamsMembersDeleteOutputProjectsProject
  roles: List[ManagementOrganizationTeamsMembersDeleteOutputProjectsRoles]


@dataclass
class ManagementOrganizationTeamsMembersDeleteOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[ManagementOrganizationTeamsMembersDeleteOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementOrganizationTeamsMembersDeleteOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersDeleteOutputProjectsProject:
    return ManagementOrganizationTeamsMembersDeleteOutputProjectsProject(
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
      ManagementOrganizationTeamsMembersDeleteOutputProjectsProject,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole:
    return ManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole(
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
      ManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersDeleteOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersDeleteOutputProjectsRoles:
    return ManagementOrganizationTeamsMembersDeleteOutputProjectsRoles(
      id=data.get("id"),
      role=mapManagementOrganizationTeamsMembersDeleteOutputProjectsRolesRole.from_dict(
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
      ManagementOrganizationTeamsMembersDeleteOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersDeleteOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsMembersDeleteOutputProjects:
    return ManagementOrganizationTeamsMembersDeleteOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapManagementOrganizationTeamsMembersDeleteOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapManagementOrganizationTeamsMembersDeleteOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementOrganizationTeamsMembersDeleteOutputProjects, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsMembersDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersDeleteOutput:
    return ManagementOrganizationTeamsMembersDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapManagementOrganizationTeamsMembersDeleteOutputProjects.from_dict(item)
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
    value: Union[ManagementOrganizationTeamsMembersDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
