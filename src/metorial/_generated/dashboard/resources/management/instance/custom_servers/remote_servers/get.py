from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceCustomServersRemoteServersGetOutput:
  object: str
  id: str
  remote_url: str
  remote_protocol: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[Dict[str, Any]] = None


class mapManagementInstanceCustomServersRemoteServersGetOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceCustomServersRemoteServersGetOutput:
    return ManagementInstanceCustomServersRemoteServersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      remote_url=data.get("remote_url"),
      remote_protocol=data.get("remote_protocol"),
      provider_oauth=data.get("provider_oauth"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceCustomServersRemoteServersGetOutput, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
