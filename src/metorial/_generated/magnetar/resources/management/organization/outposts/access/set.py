from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationOutpostsAccessSetOutputItems:
    object: str
    id: str
    outpost_id: str
    project_id: str
    instance_id: str
    organization_id: str
    services: List[str]
    created_at: datetime
@dataclass
class ManagementOrganizationOutpostsAccessSetOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationOutpostsAccessSetOutput:
    items: List[ManagementOrganizationOutpostsAccessSetOutputItems]
    pagination: ManagementOrganizationOutpostsAccessSetOutputPagination


class mapManagementOrganizationOutpostsAccessSetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsAccessSetOutputItems:
        return ManagementOrganizationOutpostsAccessSetOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        outpost_id=data.get('outpost_id'),
        project_id=data.get('project_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        services=data.get('services', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsAccessSetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOutpostsAccessSetOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsAccessSetOutputPagination:
        return ManagementOrganizationOutpostsAccessSetOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsAccessSetOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOutpostsAccessSetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsAccessSetOutput:
        return ManagementOrganizationOutpostsAccessSetOutput(
        items=[mapManagementOrganizationOutpostsAccessSetOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationOutpostsAccessSetOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsAccessSetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationOutpostsAccessSetBodyGrants:
    instance_id: str
    services: List[str]
@dataclass
class ManagementOrganizationOutpostsAccessSetBody:
    grants: List[ManagementOrganizationOutpostsAccessSetBodyGrants]


class mapManagementOrganizationOutpostsAccessSetBodyGrants:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsAccessSetBodyGrants:
        return ManagementOrganizationOutpostsAccessSetBodyGrants(
        instance_id=data.get('instance_id'),
        services=data.get('services', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsAccessSetBodyGrants, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOutpostsAccessSetBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsAccessSetBody:
        return ManagementOrganizationOutpostsAccessSetBody(
        grants=[mapManagementOrganizationOutpostsAccessSetBodyGrants.from_dict(item) for item in data.get('grants', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsAccessSetBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

