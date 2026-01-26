from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsMembersListOutputItemsActorTeams:
  id: str
  name: str
  slug: str
  assignment_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsMembersListOutputItemsActor:
  object: str
  id: str
  type: str
  organization_id: str
  name: str
  image_url: str
  teams: List[DashboardOrganizationsMembersListOutputItemsActorTeams]
  created_at: datetime
  updated_at: datetime
  email: Optional[str] = None


@dataclass
class DashboardOrganizationsMembersListOutputItems:
  object: str
  id: str
  status: str
  role: str
  user_id: str
  organization_id: str
  actor_id: str
  actor: DashboardOrganizationsMembersListOutputItemsActor
  last_active_at: datetime
  deleted_at: datetime
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsMembersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardOrganizationsMembersListOutput:
  items: List[DashboardOrganizationsMembersListOutputItems]
  pagination: DashboardOrganizationsMembersListOutputPagination


class mapDashboardOrganizationsMembersListOutputItemsActorTeams:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsMembersListOutputItemsActorTeams:
    return DashboardOrganizationsMembersListOutputItemsActorTeams(
      id=data.get("id"),
      name=data.get("name"),
      slug=data.get("slug"),
      assignment_id=data.get("assignment_id"),
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
      DashboardOrganizationsMembersListOutputItemsActorTeams, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsMembersListOutputItemsActor:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsMembersListOutputItemsActor:
    return DashboardOrganizationsMembersListOutputItemsActor(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
      teams=[
        mapDashboardOrganizationsMembersListOutputItemsActorTeams.from_dict(item)
        for item in data.get("teams", [])
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
    value: Union[
      DashboardOrganizationsMembersListOutputItemsActor, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsMembersListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersListOutputItems:
    return DashboardOrganizationsMembersListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      user_id=data.get("user_id"),
      organization_id=data.get("organization_id"),
      actor_id=data.get("actor_id"),
      actor=mapDashboardOrganizationsMembersListOutputItemsActor.from_dict(
        data.get("actor")
      )
      if data.get("actor")
      else None,
      last_active_at=parse_iso_datetime(data.get("last_active_at"))
      if data.get("last_active_at")
      else None,
      deleted_at=parse_iso_datetime(data.get("deleted_at"))
      if data.get("deleted_at")
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
    value: Union[DashboardOrganizationsMembersListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsMembersListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsMembersListOutputPagination:
    return DashboardOrganizationsMembersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsMembersListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsMembersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersListOutput:
    return DashboardOrganizationsMembersListOutput(
      items=[
        mapDashboardOrganizationsMembersListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapDashboardOrganizationsMembersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsMembersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsMembersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  team_id: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsMembersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersListQuery:
    return DashboardOrganizationsMembersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      team_id=data.get("team_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsMembersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
