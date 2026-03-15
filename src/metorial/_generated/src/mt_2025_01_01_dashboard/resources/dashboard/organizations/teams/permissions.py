from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsTeamsPermissionsOutputPermissions:
    identifier: str
    name: str
    description: str
    dependencies: List[str]
@dataclass
class DashboardOrganizationsTeamsPermissionsOutput:
    object: str
    permissions: List[DashboardOrganizationsTeamsPermissionsOutputPermissions]


class mapDashboardOrganizationsTeamsPermissionsOutputPermissions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsPermissionsOutputPermissions:
        return DashboardOrganizationsTeamsPermissionsOutputPermissions(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        dependencies=data.get('dependencies', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsPermissionsOutputPermissions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsPermissionsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsPermissionsOutput:
        return DashboardOrganizationsTeamsPermissionsOutput(
        object=data.get('object'),
        permissions=[mapDashboardOrganizationsTeamsPermissionsOutputPermissions.from_dict(item) for item in data.get('permissions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsPermissionsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

