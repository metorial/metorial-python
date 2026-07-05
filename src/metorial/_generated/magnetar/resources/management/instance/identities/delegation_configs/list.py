from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesDelegationConfigsListOutputItems:
    object: str
    id: str
    status: str
    is_default: bool
    sub_delegation_behavior: str
    sub_delegation_depth: float
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceIdentitiesDelegationConfigsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceIdentitiesDelegationConfigsListOutput:
    items: List[ManagementInstanceIdentitiesDelegationConfigsListOutputItems]
    pagination: ManagementInstanceIdentitiesDelegationConfigsListOutputPagination


class mapManagementInstanceIdentitiesDelegationConfigsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationConfigsListOutputItems:
        return ManagementInstanceIdentitiesDelegationConfigsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        sub_delegation_behavior=data.get('sub_delegation_behavior'),
        sub_delegation_depth=data.get('sub_delegation_depth'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationConfigsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationConfigsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationConfigsListOutputPagination:
        return ManagementInstanceIdentitiesDelegationConfigsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationConfigsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationConfigsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationConfigsListOutput:
        return ManagementInstanceIdentitiesDelegationConfigsListOutput(
        items=[mapManagementInstanceIdentitiesDelegationConfigsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceIdentitiesDelegationConfigsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationConfigsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIdentitiesDelegationConfigsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationConfigsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationConfigsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceIdentitiesDelegationConfigsListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceIdentitiesDelegationConfigsListQueryUpdatedAt] = None


class mapManagementInstanceIdentitiesDelegationConfigsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationConfigsListQuery:
        return ManagementInstanceIdentitiesDelegationConfigsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        created_at=mapManagementInstanceIdentitiesDelegationConfigsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceIdentitiesDelegationConfigsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationConfigsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

