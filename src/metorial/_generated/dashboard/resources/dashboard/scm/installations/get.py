from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardScmInstallationsGetOutputUser:
  id: str
  name: str
  email: str
  image_url: str


@dataclass
class DashboardScmInstallationsGetOutput:
  object: str
  id: str
  provider: str
  user: DashboardScmInstallationsGetOutputUser
  created_at: datetime
  updated_at: datetime


class mapDashboardScmInstallationsGetOutputUser:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsGetOutputUser:
    return DashboardScmInstallationsGetOutputUser(
      id=data.get("id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsGetOutputUser, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmInstallationsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsGetOutput:
    return DashboardScmInstallationsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      provider=data.get("provider"),
      user=mapDashboardScmInstallationsGetOutputUser.from_dict(data.get("user"))
      if data.get("user")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
