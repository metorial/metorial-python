from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbacksInstancesGetOutputDeployment:
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
class DashboardInstanceCallbacksInstancesGetOutputConfig:
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
class DashboardInstanceCallbacksInstancesGetOutputAuthConfig:
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
class DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger:
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
    input_schema: Optional[DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema] = None
    output_schema: Optional[DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema] = None
@dataclass
class DashboardInstanceCallbacksInstancesGetOutputTriggers:
    object: str
    id: str
    source: str
    poll_interval_seconds: Optional[float] = None
    next_poll_at: Optional[datetime] = None
    last_polled_at: Optional[datetime] = None
    webhook_url: Optional[str] = None
    is_webhook_registered: Optional[bool] = None
    provider_trigger: Optional[DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger] = None
@dataclass
class DashboardInstanceCallbacksInstancesGetOutput:
    object: str
    id: str
    status: str
    deployment: DashboardInstanceCallbacksInstancesGetOutputDeployment
    config: DashboardInstanceCallbacksInstancesGetOutputConfig
    triggers: List[DashboardInstanceCallbacksInstancesGetOutputTriggers]
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[DashboardInstanceCallbacksInstancesGetOutputAuthConfig] = None
    webhook_url: Optional[str] = None


class mapDashboardInstanceCallbacksInstancesGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputDeployment:
        return DashboardInstanceCallbacksInstancesGetOutputDeployment(
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
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputConfig:
        return DashboardInstanceCallbacksInstancesGetOutputConfig(
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
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputAuthConfig:
        return DashboardInstanceCallbacksInstancesGetOutputAuthConfig(
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
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema:
        return DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema:
        return DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger:
        return DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapDashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceCallbacksInstancesGetOutputTriggersProviderTriggerOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutputTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutputTriggers:
        return DashboardInstanceCallbacksInstancesGetOutputTriggers(
        object=data.get('object'),
        id=data.get('id'),
        source=data.get('source'),
        poll_interval_seconds=data.get('poll_interval_seconds'),
        next_poll_at=datetime.fromisoformat(data.get('next_poll_at').replace('Z', '+00:00')) if data.get('next_poll_at') else None,
        last_polled_at=datetime.fromisoformat(data.get('last_polled_at').replace('Z', '+00:00')) if data.get('last_polled_at') else None,
        webhook_url=data.get('webhook_url'),
        is_webhook_registered=data.get('is_webhook_registered'),
        provider_trigger=mapDashboardInstanceCallbacksInstancesGetOutputTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutputTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksInstancesGetOutput:
        return DashboardInstanceCallbacksInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        deployment=mapDashboardInstanceCallbacksInstancesGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceCallbacksInstancesGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceCallbacksInstancesGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        webhook_url=data.get('webhook_url'),
        triggers=[mapDashboardInstanceCallbacksInstancesGetOutputTriggers.from_dict(item) for item in data.get('triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

