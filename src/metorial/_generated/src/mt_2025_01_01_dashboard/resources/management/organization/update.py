from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationUpdateOutput:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime


class mapManagementOrganizationUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationUpdateOutput:
        return ManagementOrganizationUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationUpdateBody:
    name: Optional[str] = None


class mapManagementOrganizationUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationUpdateBody:
        return ManagementOrganizationUpdateBody(
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

