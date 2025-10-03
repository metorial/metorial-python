from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersManagedServerTemplatesListOutputItems:
  object: str
  id: str
  slug: str
  name: str
  created_at: datetime


@dataclass
class CustomServersManagedServerTemplatesListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CustomServersManagedServerTemplatesListOutput:
  items: List[CustomServersManagedServerTemplatesListOutputItems]
  pagination: CustomServersManagedServerTemplatesListOutputPagination


class mapCustomServersManagedServerTemplatesListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CustomServersManagedServerTemplatesListOutputItems:
    return CustomServersManagedServerTemplatesListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      slug=data.get("slug"),
      name=data.get("name"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      CustomServersManagedServerTemplatesListOutputItems, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersManagedServerTemplatesListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CustomServersManagedServerTemplatesListOutputPagination:
    return CustomServersManagedServerTemplatesListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      CustomServersManagedServerTemplatesListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersManagedServerTemplatesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersManagedServerTemplatesListOutput:
    return CustomServersManagedServerTemplatesListOutput(
      items=[
        mapCustomServersManagedServerTemplatesListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapCustomServersManagedServerTemplatesListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersManagedServerTemplatesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersManagedServerTemplatesListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapCustomServersManagedServerTemplatesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersManagedServerTemplatesListQuery:
    return CustomServersManagedServerTemplatesListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersManagedServerTemplatesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
