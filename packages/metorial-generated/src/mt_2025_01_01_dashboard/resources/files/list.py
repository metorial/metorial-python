from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class FilesListOutputItemsPurpose:
  name: str
  identifier: str


@dataclass
class FilesListOutputItems:
  object: str
  id: str
  status: str
  file_name: str
  file_size: float
  file_type: str
  purpose: FilesListOutputItemsPurpose
  created_at: datetime
  updated_at: datetime
  title: Optional[str] = None


@dataclass
class FilesListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class FilesListOutput:
  items: List[FilesListOutputItems]
  pagination: FilesListOutputPagination


class mapFilesListOutputItemsPurpose:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesListOutputItemsPurpose:
    return FilesListOutputItemsPurpose(
      name=data.get("name"), identifier=data.get("identifier")
    )

  @staticmethod
  def to_dict(
    value: Union[FilesListOutputItemsPurpose, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapFilesListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesListOutputItems:
    return FilesListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      file_name=data.get("file_name"),
      file_size=data.get("file_size"),
      file_type=data.get("file_type"),
      title=data.get("title"),
      purpose=mapFilesListOutputItemsPurpose.from_dict(data.get("purpose"))
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
    value: Union[FilesListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapFilesListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesListOutputPagination:
    return FilesListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[FilesListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapFilesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesListOutput:
    return FilesListOutput(
      items=[
        mapFilesListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapFilesListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[FilesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


FilesListQuery = Any


class mapFilesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesListQuery:
    data

  @staticmethod
  def to_dict(
    value: Union[FilesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
