from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementOrganizationTeamsPermissionsOutputPermissions:
  id: str
  name: str


@dataclass
class ManagementOrganizationTeamsPermissionsOutput:
  object: str
  permissions: List[ManagementOrganizationTeamsPermissionsOutputPermissions]


class mapManagementOrganizationTeamsPermissionsOutputPermissions:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationTeamsPermissionsOutputPermissions:
    return ManagementOrganizationTeamsPermissionsOutputPermissions(
      id=data.get("id"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementOrganizationTeamsPermissionsOutputPermissions, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationTeamsPermissionsOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsPermissionsOutput:
    return ManagementOrganizationTeamsPermissionsOutput(
      object=data.get("object"),
      permissions=[
        mapManagementOrganizationTeamsPermissionsOutputPermissions.from_dict(item)
        for item in data.get("permissions", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationTeamsPermissionsOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
