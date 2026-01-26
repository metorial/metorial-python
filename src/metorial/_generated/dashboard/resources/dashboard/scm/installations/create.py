from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardScmInstallationsCreateOutput:
  object: str
  authorization_url: str


class mapDashboardScmInstallationsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsCreateOutput:
    return DashboardScmInstallationsCreateOutput(
      object=data.get("object"), authorization_url=data.get("authorization_url")
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardScmInstallationsCreateBody:
  provider: str
  redirect_url: str


class mapDashboardScmInstallationsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmInstallationsCreateBody:
    return DashboardScmInstallationsCreateBody(
      provider=data.get("provider"), redirect_url=data.get("redirect_url")
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmInstallationsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
