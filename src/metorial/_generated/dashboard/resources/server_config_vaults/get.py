from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ServerConfigVaultsGetOutput:
  object: str
  id: str
  name: str
  metadata: Dict[str, Any]
  secret_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapServerConfigVaultsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServerConfigVaultsGetOutput:
    return ServerConfigVaultsGetOutput(
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
    value: Union[ServerConfigVaultsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
