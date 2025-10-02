from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersManagedServerTemplatesGetOutput:
  object: str
  id: str
  slug: str
  name: str
  created_at: datetime


class mapCustomServersManagedServerTemplatesGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersManagedServerTemplatesGetOutput:
    return CustomServersManagedServerTemplatesGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      slug=data.get("slug"),
      name=data.get("name"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersManagedServerTemplatesGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
