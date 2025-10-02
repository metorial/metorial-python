from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersCodeGetCodeEditorTokenOutput:
  object: str
  id: str
  token: str
  expires_at: datetime


class mapCustomServersCodeGetCodeEditorTokenOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersCodeGetCodeEditorTokenOutput:
    return CustomServersCodeGetCodeEditorTokenOutput(
      object=data.get("object"),
      id=data.get("id"),
      token=data.get("token"),
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersCodeGetCodeEditorTokenOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
