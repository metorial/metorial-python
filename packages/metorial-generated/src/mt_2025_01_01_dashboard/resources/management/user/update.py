from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ManagementUserUpdateOutput:
  object: str
  id: str
  status: str
  type: str
  email: str
  name: str
  first_name: str
  last_name: str
  image_url: str
  created_at: datetime
  updated_at: datetime


class mapManagementUserUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementUserUpdateOutput:
    return ManagementUserUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      email=data.get("email"),
      name=data.get("name"),
      first_name=data.get("first_name"),
      last_name=data.get("last_name"),
      image_url=data.get("image_url"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementUserUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementUserUpdateBody:
  name: Optional[str] = None
  email: Optional[str] = None


class mapManagementUserUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementUserUpdateBody:
    return ManagementUserUpdateBody(name=data.get("name"), email=data.get("email"))

  @staticmethod
  def to_dict(
    value: Union[ManagementUserUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
