from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsTeamsUpdateOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsUpdateOutputProjectsRolesRole:
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
class DashboardOrganizationsTeamsUpdateOutputProjectsRoles:
  id: str
  role: DashboardOrganizationsTeamsUpdateOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsUpdateOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: DashboardOrganizationsTeamsUpdateOutputProjectsProject
  roles: List[DashboardOrganizationsTeamsUpdateOutputProjectsRoles]


@dataclass
class DashboardOrganizationsTeamsUpdateOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[DashboardOrganizationsTeamsUpdateOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardOrganizationsTeamsUpdateOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsUpdateOutputProjectsProject:
    return DashboardOrganizationsTeamsUpdateOutputProjectsProject(
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
      DashboardOrganizationsTeamsUpdateOutputProjectsProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsUpdateOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsUpdateOutputProjectsRolesRole:
    return DashboardOrganizationsTeamsUpdateOutputProjectsRolesRole(
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
      DashboardOrganizationsTeamsUpdateOutputProjectsRolesRole, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsUpdateOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsUpdateOutputProjectsRoles:
    return DashboardOrganizationsTeamsUpdateOutputProjectsRoles(
      id=data.get("id"),
      role=mapDashboardOrganizationsTeamsUpdateOutputProjectsRolesRole.from_dict(
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
      DashboardOrganizationsTeamsUpdateOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsUpdateOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsUpdateOutputProjects:
    return DashboardOrganizationsTeamsUpdateOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapDashboardOrganizationsTeamsUpdateOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapDashboardOrganizationsTeamsUpdateOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsUpdateOutputProjects, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateOutput:
    return DashboardOrganizationsTeamsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapDashboardOrganizationsTeamsUpdateOutputProjects.from_dict(item)
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
    value: Union[DashboardOrganizationsTeamsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsTeamsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None


class mapDashboardOrganizationsTeamsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateBody:
    return DashboardOrganizationsTeamsUpdateBody(
      name=data.get("name"), description=data.get("description")
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
