from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksListOutputItemsProviderDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CallbacksListOutputItemsDestinations:
    object: str
    id: str
    status: str
    name: str
    url: str
    method: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CallbacksListOutputItemsProviderTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
@dataclass
class CallbacksListOutputItemsProviderTriggers:
    object: str
    id: str
    provider_trigger: CallbacksListOutputItemsProviderTriggersProviderTrigger
    event_types: List[str]
    created_at: datetime
@dataclass
class CallbacksListOutputItems:
    object: str
    id: str
    status: str
    name: str
    provider_deployment: CallbacksListOutputItemsProviderDeployment
    destinations: List[CallbacksListOutputItemsDestinations]
    provider_triggers: List[CallbacksListOutputItemsProviderTriggers]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None
@dataclass
class CallbacksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbacksListOutput:
    items: List[CallbacksListOutputItems]
    pagination: CallbacksListOutputPagination


class mapCallbacksListOutputItemsProviderDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItemsProviderDeployment:
        return CallbacksListOutputItemsProviderDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItemsProviderDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputItemsDestinations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItemsDestinations:
        return CallbacksListOutputItemsDestinations(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItemsDestinations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputItemsProviderTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItemsProviderTriggersProviderTrigger:
        return CallbacksListOutputItemsProviderTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItemsProviderTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputItemsProviderTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItemsProviderTriggers:
        return CallbacksListOutputItemsProviderTriggers(
        object=data.get('object'),
        id=data.get('id'),
        provider_trigger=mapCallbacksListOutputItemsProviderTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None,
        event_types=data.get('event_types', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItemsProviderTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItems:
        return CallbacksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        provider_deployment=mapCallbacksListOutputItemsProviderDeployment.from_dict(data.get('provider_deployment')) if data.get('provider_deployment') else None,
        destinations=[mapCallbacksListOutputItemsDestinations.from_dict(item) for item in data.get('destinations', []) if item],
        provider_triggers=[mapCallbacksListOutputItemsProviderTriggers.from_dict(item) for item in data.get('provider_triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputPagination:
        return CallbacksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutput:
        return CallbacksListOutput(
        items=[mapCallbacksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbacksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    created_at: Optional[CallbacksListQueryCreatedAt] = None
    updated_at: Optional[CallbacksListQueryUpdatedAt] = None


class mapCallbacksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListQuery:
        return CallbacksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        status=data.get('status'),
        created_at=mapCallbacksListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCallbacksListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

