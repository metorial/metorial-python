from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class DashboardBootOutputUser:
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


@dataclass
class DashboardBootOutput:
  object: str
  user: DashboardBootOutputUser
  organizations: List[Dict[str, Any]]
  projects: List[Dict[str, Any]]
  instances: List[Dict[str, Any]]


class mapDashboardBootOutputUser:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardBootOutputUser:
    return DashboardBootOutputUser(
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
    value: Union[DashboardBootOutputUser, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardBootOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardBootOutput:
    return DashboardBootOutput(
      object=data.get("object"),
      user=mapDashboardBootOutputUser.from_dict(data.get("user"))
      if data.get("user")
      else None,
      organizations=data.get("organizations", []),
      projects=data.get("projects", []),
      instances=data.get("instances", []),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardBootOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardBootBody:
  pass


class mapDashboardBootBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardBootBody:
    return DashboardBootBody()

  @staticmethod
  def to_dict(
    value: Union[DashboardBootBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
