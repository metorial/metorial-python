from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbacksInstancesCreateOutputDeployment:
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
class DashboardInstanceCallbacksInstancesCreateOutputConfig:
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
class DashboardInstanceCallbacksInstancesCreateOutputAuthConfig:
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
class DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger:
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
    input_schema: Optional[DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema] = None
    output_schema: Optional[DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema] = None
@dataclass
class DashboardInstanceCallbacksInstancesCreateOutputTriggers:
    object: str
    id: str
    source: str
    poll_interval_seconds: Optional[float] = None
    next_poll_at: Optional[datetime] = None
    last_polled_at: Optional[datetime] = None
    webhook_url: Optional[str] = None
    is_webhook_registered: Optional[bool] = None
    provider_trigger: Optional[DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger] = None
@dataclass
class DashboardInstanceCallbacksInstancesCreateOutput:
    object: str
    id: str
    status: str
    deployment: DashboardInstanceCallbacksInstancesCreateOutputDeployment
    config: DashboardInstanceCallbacksInstancesCreateOutputConfig
    triggers: List[DashboardInstanceCallbacksInstancesCreateOutputTriggers]
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[DashboardInstanceCallbacksInstancesCreateOutputAuthConfig] = None
    webhook_url: Optional[str] = None


class mapDashboardInstanceCallbacksInstancesCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputDeployment:
        return DashboardInstanceCallbacksInstancesCreateOutputDeployment(
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
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputConfig:
        return DashboardInstanceCallbacksInstancesCreateOutputConfig(
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
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputAuthConfig:
        return DashboardInstanceCallbacksInstancesCreateOutputAuthConfig(
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
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema:
        return DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema:
        return DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger:
        return DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapDashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTriggerOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutputTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutputTriggers:
        return DashboardInstanceCallbacksInstancesCreateOutputTriggers(
        object=data.get('object'),
        id=data.get('id'),
        source=data.get('source'),
        poll_interval_seconds=data.get('poll_interval_seconds'),
        next_poll_at=datetime.fromisoformat(data.get('next_poll_at').replace('Z', '+00:00')) if data.get('next_poll_at') else None,
        last_polled_at=datetime.fromisoformat(data.get('last_polled_at').replace('Z', '+00:00')) if data.get('last_polled_at') else None,
        webhook_url=data.get('webhook_url'),
        is_webhook_registered=data.get('is_webhook_registered'),
        provider_trigger=mapDashboardInstanceCallbacksInstancesCreateOutputTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutputTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateOutput:
        return DashboardInstanceCallbacksInstancesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        deployment=mapDashboardInstanceCallbacksInstancesCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceCallbacksInstancesCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceCallbacksInstancesCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        webhook_url=data.get('webhook_url'),
        triggers=[mapDashboardInstanceCallbacksInstancesCreateOutputTriggers.from_dict(item) for item in data.get('triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCallbacksInstancesCreateBody:
    provider_config_id: str
    provider_auth_config_id: Optional[str] = None


class mapDashboardInstanceCallbacksInstancesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesCreateBody:
        return DashboardInstanceCallbacksInstancesCreateBody(
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

