from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpTokensCreateOutput:
  object: str
  id: str
  status: str
  secret: str
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardInstanceMagicMcpTokensCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateOutput:
    return DashboardInstanceMagicMcpTokensCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      secret=data.get("secret"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpTokensCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceMagicMcpTokensCreateBody:
  name: str
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceMagicMcpTokensCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateBody:
    return DashboardInstanceMagicMcpTokensCreateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpTokensCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
