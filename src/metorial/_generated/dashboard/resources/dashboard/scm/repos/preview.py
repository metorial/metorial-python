from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardScmReposPreviewOutputItemsAccount:
  external_id: str
  name: str
  identifier: str
  provider: str


@dataclass
class DashboardScmReposPreviewOutputItems:
  provider: str
  name: str
  identifier: str
  external_id: str
  created_at: datetime
  updated_at: datetime
  account: DashboardScmReposPreviewOutputItemsAccount
  last_pushed_at: Optional[datetime] = None


@dataclass
class DashboardScmReposPreviewOutput:
  object: str
  items: List[DashboardScmReposPreviewOutputItems]


class mapDashboardScmReposPreviewOutputItemsAccount:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposPreviewOutputItemsAccount:
    return DashboardScmReposPreviewOutputItemsAccount(
      external_id=data.get("external_id"),
      name=data.get("name"),
      identifier=data.get("identifier"),
      provider=data.get("provider"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmReposPreviewOutputItemsAccount, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmReposPreviewOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposPreviewOutputItems:
    return DashboardScmReposPreviewOutputItems(
      provider=data.get("provider"),
      name=data.get("name"),
      identifier=data.get("identifier"),
      external_id=data.get("external_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      last_pushed_at=parse_iso_datetime(data.get("lastPushed_at"))
      if data.get("lastPushed_at")
      else None,
      account=mapDashboardScmReposPreviewOutputItemsAccount.from_dict(
        data.get("account")
      )
      if data.get("account")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmReposPreviewOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmReposPreviewOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposPreviewOutput:
    return DashboardScmReposPreviewOutput(
      object=data.get("object"),
      items=[
        mapDashboardScmReposPreviewOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmReposPreviewOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardScmReposPreviewQuery:
  installation_id: str
  external_account_id: str


class mapDashboardScmReposPreviewQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmReposPreviewQuery:
    return DashboardScmReposPreviewQuery(
      installation_id=data.get("installation_id"),
      external_account_id=data.get("external_account_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmReposPreviewQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
