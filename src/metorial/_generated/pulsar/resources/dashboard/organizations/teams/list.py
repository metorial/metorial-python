from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsTeamsListOutputItemsProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsListOutputItemsProjectsRolesRole:
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
class DashboardOrganizationsTeamsListOutputItemsProjectsRoles:
  id: str
  role: DashboardOrganizationsTeamsListOutputItemsProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsTeamsListOutputItemsProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: DashboardOrganizationsTeamsListOutputItemsProjectsProject
  roles: List[DashboardOrganizationsTeamsListOutputItemsProjectsRoles]


@dataclass
class DashboardOrganizationsTeamsListOutputItems:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[DashboardOrganizationsTeamsListOutputItemsProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardOrganizationsTeamsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardOrganizationsTeamsListOutput:
  items: List[DashboardOrganizationsTeamsListOutputItems]
  pagination: DashboardOrganizationsTeamsListOutputPagination


class mapDashboardOrganizationsTeamsListOutputItemsProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsListOutputItemsProjectsProject:
    return DashboardOrganizationsTeamsListOutputItemsProjectsProject(
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
      DashboardOrganizationsTeamsListOutputItemsProjectsProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsListOutputItemsProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsListOutputItemsProjectsRolesRole:
    return DashboardOrganizationsTeamsListOutputItemsProjectsRolesRole(
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
      DashboardOrganizationsTeamsListOutputItemsProjectsRolesRole, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsListOutputItemsProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsListOutputItemsProjectsRoles:
    return DashboardOrganizationsTeamsListOutputItemsProjectsRoles(
      id=data.get("id"),
      role=mapDashboardOrganizationsTeamsListOutputItemsProjectsRolesRole.from_dict(
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
      DashboardOrganizationsTeamsListOutputItemsProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsListOutputItemsProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsListOutputItemsProjects:
    return DashboardOrganizationsTeamsListOutputItemsProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapDashboardOrganizationsTeamsListOutputItemsProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapDashboardOrganizationsTeamsListOutputItemsProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsTeamsListOutputItemsProjects, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsListOutputItems:
    return DashboardOrganizationsTeamsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapDashboardOrganizationsTeamsListOutputItemsProjects.from_dict(item)
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
    value: Union[DashboardOrganizationsTeamsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsListOutputPagination:
    return DashboardOrganizationsTeamsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsListOutput:
    return DashboardOrganizationsTeamsListOutput(
      items=[
        mapDashboardOrganizationsTeamsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapDashboardOrganizationsTeamsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsTeamsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapDashboardOrganizationsTeamsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsListQuery:
    return DashboardOrganizationsTeamsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
