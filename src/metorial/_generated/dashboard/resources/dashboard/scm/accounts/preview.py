from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardScmAccountsPreviewOutputItems:
  provider: str
  name: str
  identifier: str
  external_id: str


@dataclass
class DashboardScmAccountsPreviewOutput:
  object: str
  items: List[DashboardScmAccountsPreviewOutputItems]


class mapDashboardScmAccountsPreviewOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmAccountsPreviewOutputItems:
    return DashboardScmAccountsPreviewOutputItems(
      provider=data.get("provider"),
      name=data.get("name"),
      identifier=data.get("identifier"),
      external_id=data.get("external_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmAccountsPreviewOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardScmAccountsPreviewOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmAccountsPreviewOutput:
    return DashboardScmAccountsPreviewOutput(
      object=data.get("object"),
      items=[
        mapDashboardScmAccountsPreviewOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardScmAccountsPreviewOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardScmAccountsPreviewQuery:
  installation_id: str


class mapDashboardScmAccountsPreviewQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardScmAccountsPreviewQuery:
    return DashboardScmAccountsPreviewQuery(installation_id=data.get("installation_id"))

  @staticmethod
  def to_dict(
    value: Union[DashboardScmAccountsPreviewQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
