from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersListingsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ServersListingsListOutput:
  items: List[Dict[str, Any]]
  pagination: ServersListingsListOutputPagination


class mapServersListingsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsListOutputPagination:
    return ServersListingsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersListingsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsListOutput:
    return ServersListingsListOutput(
      items=data.get("items", []),
      pagination=mapServersListingsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersListingsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  search: Optional[str] = None
  collection_id: Optional[Union[List[str], str]] = None
  category_id: Optional[Union[List[str], str]] = None
  profile_id: Optional[Union[List[str], str]] = None
  instance_id: Optional[str] = None
  order_by_rank: Optional[bool] = None
  is_public: Optional[bool] = None
  only_from_organization: Optional[bool] = None


class mapServersListingsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersListingsListQuery:
    return ServersListingsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      search=data.get("search"),
      collection_id=data.get("collection_id"),
      category_id=data.get("category_id"),
      profile_id=data.get("profile_id"),
      instance_id=data.get("instance_id"),
      order_by_rank=data.get("order_by_rank"),
      is_public=data.get("is_public"),
      only_from_organization=data.get("only_from_organization"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersListingsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
