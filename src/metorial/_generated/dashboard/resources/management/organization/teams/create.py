from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationTeamsCreateOutputProjectsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationTeamsCreateOutputProjectsRolesRole:
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
class ManagementOrganizationTeamsCreateOutputProjectsRoles:
  id: str
  role: ManagementOrganizationTeamsCreateOutputProjectsRolesRole
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationTeamsCreateOutputProjects:
  id: str
  created_at: datetime
  updated_at: datetime
  project: ManagementOrganizationTeamsCreateOutputProjectsProject
  roles: List[ManagementOrganizationTeamsCreateOutputProjectsRoles]


@dataclass
class ManagementOrganizationTeamsCreateOutput:
  object: str
  id: str
  organization_id: str
  name: str
  slug: str
  projects: List[ManagementOrganizationTeamsCreateOutputProjects]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementOrganizationTeamsCreateOutputProjectsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsCreateOutputProjectsProject:
    return ManagementOrganizationTeamsCreateOutputProjectsProject(
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
      ManagementOrganizationTeamsCreateOutputProjectsProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsCreateOutputProjectsRolesRole:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsCreateOutputProjectsRolesRole:
    return ManagementOrganizationTeamsCreateOutputProjectsRolesRole(
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
      ManagementOrganizationTeamsCreateOutputProjectsRolesRole, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsCreateOutputProjectsRoles:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsCreateOutputProjectsRoles:
    return ManagementOrganizationTeamsCreateOutputProjectsRoles(
      id=data.get("id"),
      role=mapManagementOrganizationTeamsCreateOutputProjectsRolesRole.from_dict(
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
      ManagementOrganizationTeamsCreateOutputProjectsRoles, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsCreateOutputProjects:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsCreateOutputProjects:
    return ManagementOrganizationTeamsCreateOutputProjects(
      id=data.get("id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      project=mapManagementOrganizationTeamsCreateOutputProjectsProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      roles=[
        mapManagementOrganizationTeamsCreateOutputProjectsRoles.from_dict(item)
        for item in data.get("roles", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsCreateOutputProjects, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsCreateOutput:
    return ManagementOrganizationTeamsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      slug=data.get("slug"),
      description=data.get("description"),
      projects=[
        mapManagementOrganizationTeamsCreateOutputProjects.from_dict(item)
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
    value: Union[ManagementOrganizationTeamsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationTeamsCreateBody:
  name: str
  description: Optional[str] = None


class mapManagementOrganizationTeamsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsCreateBody:
    return ManagementOrganizationTeamsCreateBody(
      name=data.get("name"), description=data.get("description")
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
