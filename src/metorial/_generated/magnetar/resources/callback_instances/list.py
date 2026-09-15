from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbackInstancesListOutputItems:
    object: str
    id: str
    status: str
    callback_id: str
    integration_instance_id: str
    integration_instance_provider_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class CallbackInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbackInstancesListOutput:
    items: List[CallbackInstancesListOutputItems]
    pagination: CallbackInstancesListOutputPagination


class mapCallbackInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackInstancesListOutputItems:
        return CallbackInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        callback_id=data.get('callback_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackInstancesListOutputPagination:
        return CallbackInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbackInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackInstancesListOutput:
        return CallbackInstancesListOutput(
        items=[mapCallbackInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbackInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbackInstancesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbackInstancesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbackInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    callback_id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    integration_instance_provider_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    created_at: Optional[CallbackInstancesListQueryCreatedAt] = None
    updated_at: Optional[CallbackInstancesListQueryUpdatedAt] = None


class mapCallbackInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackInstancesListQuery:
        return CallbackInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        callback_id=data.get('callback_id'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        status=data.get('status'),
        created_at=mapCallbackInstancesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCallbackInstancesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

