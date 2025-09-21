from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ManagementOrganizationInstancesListOutputItemsProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationInstancesListOutputItems:
  object: str
  id: str
  status: str
  slug: str
  name: str
  type: str
  organization_id: str
  project: ManagementOrganizationInstancesListOutputItemsProject
  created_at: datetime
  updated_at: datetime


@dataclass
class ManagementOrganizationInstancesListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementOrganizationInstancesListOutput:
  items: List[ManagementOrganizationInstancesListOutputItems]
  pagination: ManagementOrganizationInstancesListOutputPagination


class mapManagementOrganizationInstancesListOutputItemsProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInstancesListOutputItemsProject:
    return ManagementOrganizationInstancesListOutputItemsProject(
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
      ManagementOrganizationInstancesListOutputItemsProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInstancesListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesListOutputItems:
    return ManagementOrganizationInstancesListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      project=mapManagementOrganizationInstancesListOutputItemsProject.from_dict(
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
    value: Union[ManagementOrganizationInstancesListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInstancesListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInstancesListOutputPagination:
    return ManagementOrganizationInstancesListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementOrganizationInstancesListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInstancesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesListOutput:
    return ManagementOrganizationInstancesListOutput(
      items=[
        mapManagementOrganizationInstancesListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementOrganizationInstancesListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationInstancesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


ManagementOrganizationInstancesListQuery = Any


class mapManagementOrganizationInstancesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesListQuery:
    data

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationInstancesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
