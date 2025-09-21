from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class DashboardOrganizationsInstancesCreateOutputProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsInstancesCreateOutput:
  object: str
  id: str
  status: str
  slug: str
  name: str
  type: str
  organization_id: str
  project: DashboardOrganizationsInstancesCreateOutputProject
  created_at: datetime
  updated_at: datetime


class mapDashboardOrganizationsInstancesCreateOutputProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsInstancesCreateOutputProject:
    return DashboardOrganizationsInstancesCreateOutputProject(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsInstancesCreateOutputProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsInstancesCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInstancesCreateOutput:
    return DashboardOrganizationsInstancesCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      project=mapDashboardOrganizationsInstancesCreateOutputProject.from_dict(
        data.get("project")
      )
      if data.get("project")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsInstancesCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsInstancesCreateBody:
  name: str
  type: str
  project_id: str


class mapDashboardOrganizationsInstancesCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInstancesCreateBody:
    return DashboardOrganizationsInstancesCreateBody(
      name=data.get("name"), type=data.get("type"), project_id=data.get("project_id")
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsInstancesCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
