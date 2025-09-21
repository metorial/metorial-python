from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class LinksListOutputItemsPurpose:
  name: str
  identifier: str


@dataclass
class LinksListOutputItems:
  object: str
  id: str
  status: str
  file_name: str
  file_size: float
  file_type: str
  purpose: LinksListOutputItemsPurpose
  created_at: datetime
  updated_at: datetime
  title: Optional[str] = None


@dataclass
class LinksListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class LinksListOutput:
  items: List[LinksListOutputItems]
  pagination: LinksListOutputPagination


class mapLinksListOutputItemsPurpose:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> LinksListOutputItemsPurpose:
    return LinksListOutputItemsPurpose(
      name=data.get("name"), identifier=data.get("identifier")
    )

  @staticmethod
  def to_dict(
    value: Union[LinksListOutputItemsPurpose, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapLinksListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> LinksListOutputItems:
    return LinksListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      file_name=data.get("file_name"),
      file_size=data.get("file_size"),
      file_type=data.get("file_type"),
      title=data.get("title"),
      purpose=mapLinksListOutputItemsPurpose.from_dict(data.get("purpose"))
      if data.get("purpose")
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
    value: Union[LinksListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapLinksListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> LinksListOutputPagination:
    return LinksListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[LinksListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapLinksListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> LinksListOutput:
    return LinksListOutput(
      items=[
        mapLinksListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapLinksListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[LinksListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
