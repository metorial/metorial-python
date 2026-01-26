from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceProviderOauthTakeoutsGetOutput:
  object: str
  id: str
  status: str
  metadata: Dict[str, Any]
  created_at: datetime
  note: Optional[str] = None
  access_token: Optional[str] = None
  id_token: Optional[str] = None
  scope: Optional[str] = None
  expires_at: Optional[datetime] = None


class mapDashboardInstanceProviderOauthTakeoutsGetOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceProviderOauthTakeoutsGetOutput:
    return DashboardInstanceProviderOauthTakeoutsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      note=data.get("note"),
      metadata=data.get("metadata"),
      access_token=data.get("access_token"),
      id_token=data.get("id_token"),
      scope=data.get("scope"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      expires_at=parse_iso_datetime(data.get("expires_at"))
      if data.get("expires_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceProviderOauthTakeoutsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
