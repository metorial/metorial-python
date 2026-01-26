from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CustomServersRemoteServersListOutputItems:
  object: str
  id: str
  remote_url: str
  remote_protocol: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[Dict[str, Any]] = None


@dataclass
class CustomServersRemoteServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class CustomServersRemoteServersListOutput:
  items: List[CustomServersRemoteServersListOutputItems]
  pagination: CustomServersRemoteServersListOutputPagination


class mapCustomServersRemoteServersListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersRemoteServersListOutputItems:
    return CustomServersRemoteServersListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      remote_url=data.get("remote_url"),
      remote_protocol=data.get("remote_protocol"),
      provider_oauth=data.get("provider_oauth"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersRemoteServersListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersRemoteServersListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersRemoteServersListOutputPagination:
    return CustomServersRemoteServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersRemoteServersListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersRemoteServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersRemoteServersListOutput:
    return CustomServersRemoteServersListOutput(
      items=[
        mapCustomServersRemoteServersListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapCustomServersRemoteServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersRemoteServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class CustomServersRemoteServersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapCustomServersRemoteServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersRemoteServersListQuery:
    return CustomServersRemoteServersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersRemoteServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
