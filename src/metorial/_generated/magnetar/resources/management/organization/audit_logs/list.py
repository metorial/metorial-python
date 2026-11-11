from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAuditLogsListOutputItemsActor:
    type: str
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    record: Optional[Any] = None
@dataclass
class ManagementOrganizationAuditLogsListOutputItemsContext:
    ip: Optional[str] = None
    ua: Optional[str] = None
@dataclass
class ManagementOrganizationAuditLogsListOutputItems:
    object: str
    id: str
    event_id: str
    resource: str
    action: str
    organization_id: str
    context: ManagementOrganizationAuditLogsListOutputItemsContext
    recorded_at: datetime
    instance_id: Optional[str] = None
    organization_actor_id: Optional[str] = None
    actor: Optional[ManagementOrganizationAuditLogsListOutputItemsActor] = None
    payload: Optional[Dict[str, Any]] = None
    previous_attributes: Optional[Dict[str, Any]] = None
@dataclass
class ManagementOrganizationAuditLogsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationAuditLogsListOutput:
    items: List[ManagementOrganizationAuditLogsListOutputItems]
    pagination: ManagementOrganizationAuditLogsListOutputPagination


class mapManagementOrganizationAuditLogsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAuditLogsListOutputItemsActor:
        return ManagementOrganizationAuditLogsListOutputItemsActor(
        type=data.get('type'),
        id=data.get('id'),
        metadata=data.get('metadata'),
        record=data.get('record')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAuditLogsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAuditLogsListOutputItemsContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAuditLogsListOutputItemsContext:
        return ManagementOrganizationAuditLogsListOutputItemsContext(
        ip=data.get('ip'),
        ua=data.get('ua')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAuditLogsListOutputItemsContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAuditLogsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAuditLogsListOutputItems:
        return ManagementOrganizationAuditLogsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        event_id=data.get('event_id'),
        resource=data.get('resource'),
        action=data.get('action'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        organization_actor_id=data.get('organization_actor_id'),
        actor=mapManagementOrganizationAuditLogsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        context=mapManagementOrganizationAuditLogsListOutputItemsContext.from_dict(data.get('context')) if data.get('context') else None,
        payload=data.get('payload'),
        previous_attributes=data.get('previous_attributes'),
        recorded_at=datetime.fromisoformat(data.get('recorded_at').replace('Z', '+00:00')) if data.get('recorded_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAuditLogsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAuditLogsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAuditLogsListOutputPagination:
        return ManagementOrganizationAuditLogsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAuditLogsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAuditLogsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAuditLogsListOutput:
        return ManagementOrganizationAuditLogsListOutput(
        items=[mapManagementOrganizationAuditLogsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationAuditLogsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAuditLogsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAuditLogsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationAuditLogsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAuditLogsListQuery:
        return ManagementOrganizationAuditLogsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAuditLogsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

