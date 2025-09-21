from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class FilesUpdateOutputPurpose:
  name: str
  identifier: str


@dataclass
class FilesUpdateOutput:
  object: str
  id: str
  status: str
  file_name: str
  file_size: float
  file_type: str
  purpose: FilesUpdateOutputPurpose
  created_at: datetime
  updated_at: datetime
  title: Optional[str] = None


class mapFilesUpdateOutputPurpose:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesUpdateOutputPurpose:
    return FilesUpdateOutputPurpose(
      name=data.get("name"), identifier=data.get("identifier")
    )

  @staticmethod
  def to_dict(
    value: Union[FilesUpdateOutputPurpose, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapFilesUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesUpdateOutput:
    return FilesUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      file_name=data.get("file_name"),
      file_size=data.get("file_size"),
      file_type=data.get("file_type"),
      title=data.get("title"),
      purpose=mapFilesUpdateOutputPurpose.from_dict(data.get("purpose"))
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
    value: Union[FilesUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class FilesUpdateBody:
  title: Optional[str] = None


class mapFilesUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesUpdateBody:
    return FilesUpdateBody(title=data.get("title"))

  @staticmethod
  def to_dict(
    value: Union[FilesUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
