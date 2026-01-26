from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceServerConfigVaultsUpdateOutput:
  object: str
  id: str
  name: str
  metadata: Dict[str, Any]
  secret_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardInstanceServerConfigVaultsUpdateOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceServerConfigVaultsUpdateOutput:
    return DashboardInstanceServerConfigVaultsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      secret_id=data.get("secret_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceServerConfigVaultsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceServerConfigVaultsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceServerConfigVaultsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerConfigVaultsUpdateBody:
    return DashboardInstanceServerConfigVaultsUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceServerConfigVaultsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
