from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class DashboardOrganizationsProjectsDeleteOutput:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


class mapDashboardOrganizationsProjectsDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsProjectsDeleteOutput:
    return DashboardOrganizationsProjectsDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsProjectsDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
