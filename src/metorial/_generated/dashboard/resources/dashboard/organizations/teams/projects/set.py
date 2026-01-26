from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsTeamsProjectsSetOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole:
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
class DashboardOrganizationsTeamsProjectsSetOutputProjectsRoles:
  id: str
  role: DashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsProjectsSetOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: DashboardOrganizationsTeamsProjectsSetOutputProjectsProject
  roles: List[DashboardOrganizationsTeamsProjectsSetOutputProjectsRoles]


@dataclass
class DashboardOrganizationsTeamsProjectsSetOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[DashboardOrganizationsTeamsProjectsSetOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardOrganizationsTeamsProjectsSetOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsProjectsSetOutputProjectsProject:
    return DashboardOrganizationsTeamsProjectsSetOutputProjectsProject(
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
      DashboardOrganizationsTeamsProjectsSetOutputProjectsProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole:
    return DashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole(
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
      DashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsProjectsSetOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsProjectsSetOutputProjectsRoles:
    return DashboardOrganizationsTeamsProjectsSetOutputProjectsRoles(
      id=data.get("id"),
      role=mapDashboardOrganizationsTeamsProjectsSetOutputProjectsRolesRole.from_dict(
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
      DashboardOrganizationsTeamsProjectsSetOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsProjectsSetOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsProjectsSetOutputProjects:
    return DashboardOrganizationsTeamsProjectsSetOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapDashboardOrganizationsTeamsProjectsSetOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapDashboardOrganizationsTeamsProjectsSetOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsTeamsProjectsSetOutputProjects, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsProjectsSetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsProjectsSetOutput:
    return DashboardOrganizationsTeamsProjectsSetOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapDashboardOrganizationsTeamsProjectsSetOutputProjects.from_dict(item)
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
    value: Union[DashboardOrganizationsTeamsProjectsSetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsTeamsProjectsSetBody:
  project_id: str
  team_role_ids: List[str]


class mapDashboardOrganizationsTeamsProjectsSetBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsProjectsSetBody:
    return DashboardOrganizationsTeamsProjectsSetBody(
      project_id=data.get("project_id"), team_role_ids=data.get("team_role_ids", [])
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsProjectsSetBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
