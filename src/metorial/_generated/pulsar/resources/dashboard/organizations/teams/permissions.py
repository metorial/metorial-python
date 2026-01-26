from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsTeamsPermissionsOutputPermissions:
  id: str
  name: str


@dataclass
class DashboardOrganizationsTeamsPermissionsOutput:
  object: str
  permissions: List[DashboardOrganizationsTeamsPermissionsOutputPermissions]


class mapDashboardOrganizationsTeamsPermissionsOutputPermissions:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsTeamsPermissionsOutputPermissions:
    return DashboardOrganizationsTeamsPermissionsOutputPermissions(
      id=data.get("id"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsTeamsPermissionsOutputPermissions, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsTeamsPermissionsOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsPermissionsOutput:
    return DashboardOrganizationsTeamsPermissionsOutput(
      object=data.get("object"),
      permissions=[
        mapDashboardOrganizationsTeamsPermissionsOutputPermissions.from_dict(item)
        for item in data.get("permissions", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsTeamsPermissionsOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
