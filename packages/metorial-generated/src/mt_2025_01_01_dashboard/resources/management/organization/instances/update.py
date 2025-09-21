from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ManagementOrganizationInstancesUpdateOutputProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationInstancesUpdateOutput:
  object: str
  id: str
  status: str
  slug: str
  name: str
  type: str
  organization_id: str
  project: ManagementOrganizationInstancesUpdateOutputProject
  created_at: datetime
  updated_at: datetime


class mapManagementOrganizationInstancesUpdateOutputProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInstancesUpdateOutputProject:
    return ManagementOrganizationInstancesUpdateOutputProject(
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
      ManagementOrganizationInstancesUpdateOutputProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInstancesUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesUpdateOutput:
    return ManagementOrganizationInstancesUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      project=mapManagementOrganizationInstancesUpdateOutputProject.from_dict(
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
    value: Union[ManagementOrganizationInstancesUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationInstancesUpdateBody:
  name: Optional[str] = None


class mapManagementOrganizationInstancesUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesUpdateBody:
    return ManagementOrganizationInstancesUpdateBody(name=data.get("name"))

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationInstancesUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
