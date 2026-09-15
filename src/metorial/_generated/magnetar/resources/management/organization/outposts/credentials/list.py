from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationOutpostsCredentialsListOutputItems:
    object: str
    id: str
    status: str
    outpost_id: str
    name: str
    envelope_preview: str
    created_at: datetime
    updated_at: datetime
    envelope: Optional[str] = None
    expires_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationOutpostsCredentialsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationOutpostsCredentialsListOutput:
    items: List[ManagementOrganizationOutpostsCredentialsListOutputItems]
    pagination: ManagementOrganizationOutpostsCredentialsListOutputPagination


class mapManagementOrganizationOutpostsCredentialsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsCredentialsListOutputItems:
        return ManagementOrganizationOutpostsCredentialsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        outpost_id=data.get('outpost_id'),
        name=data.get('name'),
        envelope_preview=data.get('envelope_preview'),
        envelope=data.get('envelope'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsCredentialsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOutpostsCredentialsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsCredentialsListOutputPagination:
        return ManagementOrganizationOutpostsCredentialsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsCredentialsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOutpostsCredentialsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsCredentialsListOutput:
        return ManagementOrganizationOutpostsCredentialsListOutput(
        items=[mapManagementOrganizationOutpostsCredentialsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationOutpostsCredentialsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsCredentialsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationOutpostsCredentialsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationOutpostsCredentialsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOutpostsCredentialsListQuery:
        return ManagementOrganizationOutpostsCredentialsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOutpostsCredentialsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

