from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationTeamsRolesListOutputItems:
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
class ManagementOrganizationTeamsRolesListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementOrganizationTeamsRolesListOutput:
  items: List[ManagementOrganizationTeamsRolesListOutputItems]
  pagination: ManagementOrganizationTeamsRolesListOutputPagination


class mapManagementOrganizationTeamsRolesListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsRolesListOutputItems:
    return ManagementOrganizationTeamsRolesListOutputItems(
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
    value: Union[ManagementOrganizationTeamsRolesListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsRolesListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsRolesListOutputPagination:
    return ManagementOrganizationTeamsRolesListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementOrganizationTeamsRolesListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsRolesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsRolesListOutput:
    return ManagementOrganizationTeamsRolesListOutput(
      items=[
        mapManagementOrganizationTeamsRolesListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementOrganizationTeamsRolesListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsRolesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementOrganizationTeamsRolesListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapManagementOrganizationTeamsRolesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsRolesListQuery:
    return ManagementOrganizationTeamsRolesListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsRolesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
