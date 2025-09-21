from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class FilesDeleteOutputPurpose:
  name: str
  identifier: str


@dataclass
class FilesDeleteOutput:
  object: str
  id: str
  status: str
  file_name: str
  file_size: float
  file_type: str
  purpose: FilesDeleteOutputPurpose
  created_at: datetime
  updated_at: datetime
  title: Optional[str] = None


class mapFilesDeleteOutputPurpose:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesDeleteOutputPurpose:
    return FilesDeleteOutputPurpose(
      name=data.get("name"), identifier=data.get("identifier")
    )

  @staticmethod
  def to_dict(
    value: Union[FilesDeleteOutputPurpose, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapFilesDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> FilesDeleteOutput:
    return FilesDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      file_name=data.get("file_name"),
      file_size=data.get("file_size"),
      file_type=data.get("file_type"),
      title=data.get("title"),
      purpose=mapFilesDeleteOutputPurpose.from_dict(data.get("purpose"))
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
    value: Union[FilesDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
