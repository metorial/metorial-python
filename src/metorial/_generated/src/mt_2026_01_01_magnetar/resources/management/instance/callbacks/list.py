from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksListOutputItemsProviderDeployment:
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
class ManagementInstanceCallbacksListOutputItemsDestinations:
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
    signing_secret: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
@dataclass
class ManagementInstanceCallbacksListOutputItemsProviderTriggers:
    object: str
    id: str
    provider_trigger: ManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger
    event_types: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceCallbacksListOutputItems:
    object: str
    id: str
    status: str
    name: str
    provider_deployment: ManagementInstanceCallbacksListOutputItemsProviderDeployment
    destinations: List[ManagementInstanceCallbacksListOutputItemsDestinations]
    provider_triggers: List[ManagementInstanceCallbacksListOutputItemsProviderTriggers]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None
@dataclass
class ManagementInstanceCallbacksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCallbacksListOutput:
    items: List[ManagementInstanceCallbacksListOutputItems]
    pagination: ManagementInstanceCallbacksListOutputPagination


class mapManagementInstanceCallbacksListOutputItemsProviderDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutputItemsProviderDeployment:
        return ManagementInstanceCallbacksListOutputItemsProviderDeployment(
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
    def to_dict(value: Union[ManagementInstanceCallbacksListOutputItemsProviderDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksListOutputItemsDestinations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutputItemsDestinations:
        return ManagementInstanceCallbacksListOutputItemsDestinations(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListOutputItemsDestinations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger:
        return ManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksListOutputItemsProviderTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutputItemsProviderTriggers:
        return ManagementInstanceCallbacksListOutputItemsProviderTriggers(
        object=data.get('object'),
        id=data.get('id'),
        provider_trigger=mapManagementInstanceCallbacksListOutputItemsProviderTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None,
        event_types=data.get('event_types', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListOutputItemsProviderTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutputItems:
        return ManagementInstanceCallbacksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        provider_deployment=mapManagementInstanceCallbacksListOutputItemsProviderDeployment.from_dict(data.get('provider_deployment')) if data.get('provider_deployment') else None,
        destinations=[mapManagementInstanceCallbacksListOutputItemsDestinations.from_dict(item) for item in data.get('destinations', []) if item],
        provider_triggers=[mapManagementInstanceCallbacksListOutputItemsProviderTriggers.from_dict(item) for item in data.get('provider_triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutputPagination:
        return ManagementInstanceCallbacksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListOutput:
        return ManagementInstanceCallbacksListOutput(
        items=[mapManagementInstanceCallbacksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCallbacksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCallbacksListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbacksListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbacksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceCallbacksListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceCallbacksListQueryUpdatedAt] = None


class mapManagementInstanceCallbacksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksListQuery:
        return ManagementInstanceCallbacksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        status=data.get('status'),
        created_at=mapManagementInstanceCallbacksListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceCallbacksListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

