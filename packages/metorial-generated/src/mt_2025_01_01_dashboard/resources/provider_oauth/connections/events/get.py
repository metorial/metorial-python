from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsEventsGetOutput:
  object: str
  id: str
  status: str
  type: str
  metadata: Dict[str, Any]
  connection_id: str
  created_at: datetime


class mapProviderOauthConnectionsEventsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsEventsGetOutput:
    return ProviderOauthConnectionsEventsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      metadata=data.get("metadata"),
      connection_id=data.get("connection_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsEventsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
