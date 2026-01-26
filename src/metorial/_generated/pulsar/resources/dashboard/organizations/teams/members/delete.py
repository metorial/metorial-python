from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsTeamsMembersDeleteOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole:
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
class DashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles:
  id: str
  role: DashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsMembersDeleteOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: DashboardOrganizationsTeamsMembersDeleteOutputProjectsProject
  roles: List[DashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles]


@dataclass
class DashboardOrganizationsTeamsMembersDeleteOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[DashboardOrganizationsTeamsMembersDeleteOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardOrganizationsTeamsMembersDeleteOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersDeleteOutputProjectsProject:
    return DashboardOrganizationsTeamsMembersDeleteOutputProjectsProject(
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
      DashboardOrganizationsTeamsMembersDeleteOutputProjectsProject,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole:
    return DashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole(
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
      DashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles:
    return DashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles(
      id=data.get("id"),
      role=mapDashboardOrganizationsTeamsMembersDeleteOutputProjectsRolesRole.from_dict(
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
      DashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersDeleteOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersDeleteOutputProjects:
    return DashboardOrganizationsTeamsMembersDeleteOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapDashboardOrganizationsTeamsMembersDeleteOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapDashboardOrganizationsTeamsMembersDeleteOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsTeamsMembersDeleteOutputProjects, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsMembersDeleteOutput:
    return DashboardOrganizationsTeamsMembersDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapDashboardOrganizationsTeamsMembersDeleteOutputProjects.from_dict(item)
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
    value: Union[DashboardOrganizationsTeamsMembersDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
