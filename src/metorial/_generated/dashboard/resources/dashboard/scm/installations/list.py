from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardScmInstallationsListOutputItemsUser:
  id: str
  name: str
  email: str
  image_url: str


@dataclass
class DashboardScmInstallationsListOutputItems:
  object: str
  id: str
  provider: str
  user: DashboardScmInstallationsListOutputItemsUser
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardScmInstallationsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class DashboardScmInstallationsListOutput:
  items: List[DashboardScmInstallationsListOutputItems]
  pagination: DashboardScmInstallationsListOutputPagination


class mapDashboardScmInstallationsListOutputItemsUser:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsListOutputItemsUser:
    return DashboardScmInstallationsListOutputItemsUser(
      id=data.get("id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsListOutputItemsUser, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmInstallationsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsListOutputItems:
    return DashboardScmInstallationsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      provider=data.get("provider"),
      user=mapDashboardScmInstallationsListOutputItemsUser.from_dict(data.get("user"))
      if data.get("user")
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
    value: Union[DashboardScmInstallationsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmInstallationsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsListOutputPagination:
    return DashboardScmInstallationsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmInstallationsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsListOutput:
    return DashboardScmInstallationsListOutput(
      items=[
        mapDashboardScmInstallationsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapDashboardScmInstallationsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardScmInstallationsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapDashboardScmInstallationsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsListQuery:
    return DashboardScmInstallationsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
