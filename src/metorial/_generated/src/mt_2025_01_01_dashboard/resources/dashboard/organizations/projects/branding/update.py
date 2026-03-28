from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsProjectsBrandingUpdateOutput:
    object: str
    id: str
    identifier: str
    name: str
    image_url: str
    project_id: str
    created_at: datetime
    updated_at: datetime


class mapDashboardOrganizationsProjectsBrandingUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsProjectsBrandingUpdateOutput:
        return DashboardOrganizationsProjectsBrandingUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        project_id=data.get('project_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsProjectsBrandingUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsProjectsBrandingUpdateBody:
    name: Optional[str] = None
    image_file_id: Optional[str] = None


class mapDashboardOrganizationsProjectsBrandingUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsProjectsBrandingUpdateBody:
        return DashboardOrganizationsProjectsBrandingUpdateBody(
        name=data.get('name'),
        image_file_id=data.get('image_file_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsProjectsBrandingUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

