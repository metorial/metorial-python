from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpTokensListOutputItems:
  object: str
  id: str
  status: str
  secret: str
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpTokensListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceMagicMcpTokensListOutput:
  items: List[ManagementInstanceMagicMcpTokensListOutputItems]
  pagination: ManagementInstanceMagicMcpTokensListOutputPagination


class mapManagementInstanceMagicMcpTokensListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpTokensListOutputItems:
    return ManagementInstanceMagicMcpTokensListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      secret=data.get("secret"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpTokensListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpTokensListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpTokensListOutputPagination:
    return ManagementInstanceMagicMcpTokensListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpTokensListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpTokensListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensListOutput:
    return ManagementInstanceMagicMcpTokensListOutput(
      items=[
        mapManagementInstanceMagicMcpTokensListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementInstanceMagicMcpTokensListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpTokensListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceMagicMcpTokensListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceMagicMcpTokensListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensListQuery:
    return ManagementInstanceMagicMcpTokensListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpTokensListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
