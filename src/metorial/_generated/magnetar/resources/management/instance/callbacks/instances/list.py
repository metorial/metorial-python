from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksInstancesListOutputItemsDeployment:
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
class ManagementInstanceCallbacksInstancesListOutputItemsConfig:
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
class ManagementInstanceCallbacksInstancesListOutputItemsAuthConfig:
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
class ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
    invocation: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema] = None
    output_schema: Optional[ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema] = None
@dataclass
class ManagementInstanceCallbacksInstancesListOutputItemsTriggers:
    object: str
    id: str
    source: str
    poll_interval_seconds: Optional[float] = None
    next_poll_at: Optional[datetime] = None
    last_polled_at: Optional[datetime] = None
    webhook_url: Optional[str] = None
    is_webhook_registered: Optional[bool] = None
    provider_trigger: Optional[ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger] = None
@dataclass
class ManagementInstanceCallbacksInstancesListOutputItems:
    object: str
    id: str
    status: str
    deployment: ManagementInstanceCallbacksInstancesListOutputItemsDeployment
    config: ManagementInstanceCallbacksInstancesListOutputItemsConfig
    triggers: List[ManagementInstanceCallbacksInstancesListOutputItemsTriggers]
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[ManagementInstanceCallbacksInstancesListOutputItemsAuthConfig] = None
    webhook_url: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCallbacksInstancesListOutput:
    items: List[ManagementInstanceCallbacksInstancesListOutputItems]
    pagination: ManagementInstanceCallbacksInstancesListOutputPagination


class mapManagementInstanceCallbacksInstancesListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsDeployment:
        return ManagementInstanceCallbacksInstancesListOutputItemsDeployment(
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
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsConfig:
        return ManagementInstanceCallbacksInstancesListOutputItemsConfig(
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
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsAuthConfig:
        return ManagementInstanceCallbacksInstancesListOutputItemsAuthConfig(
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
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema:
        return ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema:
        return ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger:
        return ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItemsTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItemsTriggers:
        return ManagementInstanceCallbacksInstancesListOutputItemsTriggers(
        object=data.get('object'),
        id=data.get('id'),
        source=data.get('source'),
        poll_interval_seconds=data.get('poll_interval_seconds'),
        next_poll_at=datetime.fromisoformat(data.get('next_poll_at').replace('Z', '+00:00')) if data.get('next_poll_at') else None,
        last_polled_at=datetime.fromisoformat(data.get('last_polled_at').replace('Z', '+00:00')) if data.get('last_polled_at') else None,
        webhook_url=data.get('webhook_url'),
        is_webhook_registered=data.get('is_webhook_registered'),
        provider_trigger=mapManagementInstanceCallbacksInstancesListOutputItemsTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItemsTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputItems:
        return ManagementInstanceCallbacksInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        deployment=mapManagementInstanceCallbacksInstancesListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceCallbacksInstancesListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceCallbacksInstancesListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        webhook_url=data.get('webhook_url'),
        triggers=[mapManagementInstanceCallbacksInstancesListOutputItemsTriggers.from_dict(item) for item in data.get('triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutputPagination:
        return ManagementInstanceCallbacksInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListOutput:
        return ManagementInstanceCallbacksInstancesListOutput(
        items=[mapManagementInstanceCallbacksInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCallbacksInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCallbacksInstancesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbacksInstancesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbacksInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceCallbacksInstancesListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceCallbacksInstancesListQueryUpdatedAt] = None


class mapManagementInstanceCallbacksInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksInstancesListQuery:
        return ManagementInstanceCallbacksInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        created_at=mapManagementInstanceCallbacksInstancesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceCallbacksInstancesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

