from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardScmReposCreateOutputAccount:
  id: str
  external_id: str
  name: str
  identifier: str
  provider: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardScmReposCreateOutput:
  object: str
  id: str
  provider: str
  name: str
  identifier: str
  external_id: str
  account: DashboardScmReposCreateOutputAccount
  created_at: datetime
  updated_at: datetime


class mapDashboardScmReposCreateOutputAccount:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposCreateOutputAccount:
    return DashboardScmReposCreateOutputAccount(
      id=data.get("id"),
      external_id=data.get("external_id"),
      name=data.get("name"),
      identifier=data.get("identifier"),
      provider=data.get("provider"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmReposCreateOutputAccount, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmReposCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposCreateOutput:
    return DashboardScmReposCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      provider=data.get("provider"),
      name=data.get("name"),
      identifier=data.get("identifier"),
      external_id=data.get("external_id"),
      account=mapDashboardScmReposCreateOutputAccount.from_dict(data.get("account"))
      if data.get("account")
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
    value: Union[DashboardScmReposCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


DashboardScmReposCreateBody = Dict[str, Any]


class mapDashboardScmReposCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposCreateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[DashboardScmReposCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
