from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksInstancesListOutputItemsDeployment:
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
class CallbacksInstancesListOutputItemsConfig:
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
class CallbacksInstancesListOutputItemsAuthConfig:
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
class CallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CallbacksInstancesListOutputItemsTriggersProviderTrigger:
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
    input_schema: Optional[CallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema] = None
    output_schema: Optional[CallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema] = None
@dataclass
class CallbacksInstancesListOutputItemsTriggers:
    object: str
    id: str
    source: str
    poll_interval_seconds: Optional[float] = None
    next_poll_at: Optional[datetime] = None
    last_polled_at: Optional[datetime] = None
    webhook_url: Optional[str] = None
    is_webhook_registered: Optional[bool] = None
    provider_trigger: Optional[CallbacksInstancesListOutputItemsTriggersProviderTrigger] = None
@dataclass
class CallbacksInstancesListOutputItems:
    object: str
    id: str
    status: str
    deployment: CallbacksInstancesListOutputItemsDeployment
    config: CallbacksInstancesListOutputItemsConfig
    triggers: List[CallbacksInstancesListOutputItemsTriggers]
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[CallbacksInstancesListOutputItemsAuthConfig] = None
    webhook_url: Optional[str] = None
@dataclass
class CallbacksInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbacksInstancesListOutput:
    items: List[CallbacksInstancesListOutputItems]
    pagination: CallbacksInstancesListOutputPagination


class mapCallbacksInstancesListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsDeployment:
        return CallbacksInstancesListOutputItemsDeployment(
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
    def to_dict(value: Union[CallbacksInstancesListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsConfig:
        return CallbacksInstancesListOutputItemsConfig(
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
    def to_dict(value: Union[CallbacksInstancesListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsAuthConfig:
        return CallbacksInstancesListOutputItemsAuthConfig(
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
    def to_dict(value: Union[CallbacksInstancesListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema:
        return CallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema:
        return CallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItemsTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsTriggersProviderTrigger:
        return CallbacksInstancesListOutputItemsTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapCallbacksInstancesListOutputItemsTriggersProviderTriggerInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapCallbacksInstancesListOutputItemsTriggersProviderTriggerOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutputItemsTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItemsTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItemsTriggers:
        return CallbacksInstancesListOutputItemsTriggers(
        object=data.get('object'),
        id=data.get('id'),
        source=data.get('source'),
        poll_interval_seconds=data.get('poll_interval_seconds'),
        next_poll_at=datetime.fromisoformat(data.get('next_poll_at').replace('Z', '+00:00')) if data.get('next_poll_at') else None,
        last_polled_at=datetime.fromisoformat(data.get('last_polled_at').replace('Z', '+00:00')) if data.get('last_polled_at') else None,
        webhook_url=data.get('webhook_url'),
        is_webhook_registered=data.get('is_webhook_registered'),
        provider_trigger=mapCallbacksInstancesListOutputItemsTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutputItemsTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputItems:
        return CallbacksInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        deployment=mapCallbacksInstancesListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapCallbacksInstancesListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapCallbacksInstancesListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        webhook_url=data.get('webhook_url'),
        triggers=[mapCallbacksInstancesListOutputItemsTriggers.from_dict(item) for item in data.get('triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutputPagination:
        return CallbacksInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListOutput:
        return CallbacksInstancesListOutput(
        items=[mapCallbacksInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbacksInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksInstancesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksInstancesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[CallbacksInstancesListQueryCreatedAt] = None
    updated_at: Optional[CallbacksInstancesListQueryUpdatedAt] = None


class mapCallbacksInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesListQuery:
        return CallbacksInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        created_at=mapCallbacksInstancesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCallbacksInstancesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

