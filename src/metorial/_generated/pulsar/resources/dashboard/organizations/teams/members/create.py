from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsTeamsMembersCreateOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole:
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
class DashboardOrganizationsTeamsMembersCreateOutputProjectsRoles:
  id: str
  role: DashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsMembersCreateOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: DashboardOrganizationsTeamsMembersCreateOutputProjectsProject
  roles: List[DashboardOrganizationsTeamsMembersCreateOutputProjectsRoles]


@dataclass
class DashboardOrganizationsTeamsMembersCreateOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[DashboardOrganizationsTeamsMembersCreateOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardOrganizationsTeamsMembersCreateOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersCreateOutputProjectsProject:
    return DashboardOrganizationsTeamsMembersCreateOutputProjectsProject(
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
      DashboardOrganizationsTeamsMembersCreateOutputProjectsProject,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole:
    return DashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole(
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
      DashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersCreateOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersCreateOutputProjectsRoles:
    return DashboardOrganizationsTeamsMembersCreateOutputProjectsRoles(
      id=data.get("id"),
      role=mapDashboardOrganizationsTeamsMembersCreateOutputProjectsRolesRole.from_dict(
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
      DashboardOrganizationsTeamsMembersCreateOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersCreateOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsMembersCreateOutputProjects:
    return DashboardOrganizationsTeamsMembersCreateOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapDashboardOrganizationsTeamsMembersCreateOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapDashboardOrganizationsTeamsMembersCreateOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsTeamsMembersCreateOutputProjects, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsMembersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsMembersCreateOutput:
    return DashboardOrganizationsTeamsMembersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapDashboardOrganizationsTeamsMembersCreateOutputProjects.from_dict(item)
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
    value: Union[DashboardOrganizationsTeamsMembersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsTeamsMembersCreateBody:
  actor_id: str


class mapDashboardOrganizationsTeamsMembersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsMembersCreateBody:
    return DashboardOrganizationsTeamsMembersCreateBody(actor_id=data.get("actor_id"))

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsMembersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
