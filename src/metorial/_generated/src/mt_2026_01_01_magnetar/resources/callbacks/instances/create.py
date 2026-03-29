from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksInstancesCreateOutputDeployment:
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
class CallbacksInstancesCreateOutputConfig:
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
class CallbacksInstancesCreateOutputAuthConfig:
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
class CallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CallbacksInstancesCreateOutputTriggersProviderTrigger:
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
    input_schema: Optional[CallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema] = None
    output_schema: Optional[CallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema] = None
@dataclass
class CallbacksInstancesCreateOutputTriggers:
    object: str
    id: str
    source: str
    poll_interval_seconds: Optional[float] = None
    next_poll_at: Optional[datetime] = None
    last_polled_at: Optional[datetime] = None
    webhook_url: Optional[str] = None
    is_webhook_registered: Optional[bool] = None
    provider_trigger: Optional[CallbacksInstancesCreateOutputTriggersProviderTrigger] = None
@dataclass
class CallbacksInstancesCreateOutput:
    object: str
    id: str
    status: str
    deployment: CallbacksInstancesCreateOutputDeployment
    config: CallbacksInstancesCreateOutputConfig
    triggers: List[CallbacksInstancesCreateOutputTriggers]
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[CallbacksInstancesCreateOutputAuthConfig] = None


class mapCallbacksInstancesCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputDeployment:
        return CallbacksInstancesCreateOutputDeployment(
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
    def to_dict(value: Union[CallbacksInstancesCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputConfig:
        return CallbacksInstancesCreateOutputConfig(
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
    def to_dict(value: Union[CallbacksInstancesCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputAuthConfig:
        return CallbacksInstancesCreateOutputAuthConfig(
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
    def to_dict(value: Union[CallbacksInstancesCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema:
        return CallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema:
        return CallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutputTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputTriggersProviderTrigger:
        return CallbacksInstancesCreateOutputTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesCreateOutputTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutputTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutputTriggers:
        return CallbacksInstancesCreateOutputTriggers(
        object=data.get('object'),
        id=data.get('id'),
        source=data.get('source'),
        poll_interval_seconds=data.get('poll_interval_seconds'),
        next_poll_at=datetime.fromisoformat(data.get('next_poll_at').replace('Z', '+00:00')) if data.get('next_poll_at') else None,
        last_polled_at=datetime.fromisoformat(data.get('last_polled_at').replace('Z', '+00:00')) if data.get('last_polled_at') else None,
        webhook_url=data.get('webhook_url'),
        is_webhook_registered=data.get('is_webhook_registered'),
        provider_trigger=mapCallbacksInstancesCreateOutputTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesCreateOutputTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksInstancesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateOutput:
        return CallbacksInstancesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        deployment=mapCallbacksInstancesCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapCallbacksInstancesCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapCallbacksInstancesCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        triggers=[mapCallbacksInstancesCreateOutputTriggers.from_dict(item) for item in data.get('triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksInstancesCreateBody:
    provider_config_id: str
    provider_auth_config_id: Optional[str] = None


class mapCallbacksInstancesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksInstancesCreateBody:
        return CallbacksInstancesCreateBody(
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksInstancesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

