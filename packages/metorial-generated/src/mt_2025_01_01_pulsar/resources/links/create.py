from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class LinksCreateOutput:
  object: str
  id: str
  file_id: str
  url: str
  created_at: datetime
  expires_at: Optional[datetime] = None


class mapLinksCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> LinksCreateOutput:
    return LinksCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      file_id=data.get("file_id"),
      url=data.get("url"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[LinksCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class LinksCreateBody:
  expires_at: Optional[datetime] = None


class mapLinksCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> LinksCreateBody:
    return LinksCreateBody(
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None
    )

  @staticmethod
  def to_dict(
    value: Union[LinksCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
