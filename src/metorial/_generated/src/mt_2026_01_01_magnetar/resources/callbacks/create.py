from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksCreateOutputProviderDeployment:
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
class CallbacksCreateOutputDestinations:
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
class CallbacksCreateOutputProviderTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
@dataclass
class CallbacksCreateOutputProviderTriggers:
    object: str
    id: str
    provider_trigger: CallbacksCreateOutputProviderTriggersProviderTrigger
    event_types: List[str]
    created_at: datetime
@dataclass
class CallbacksCreateOutput:
    object: str
    id: str
    status: str
    name: str
    provider_deployment: CallbacksCreateOutputProviderDeployment
    destinations: List[CallbacksCreateOutputDestinations]
    provider_triggers: List[CallbacksCreateOutputProviderTriggers]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None


class mapCallbacksCreateOutputProviderDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateOutputProviderDeployment:
        return CallbacksCreateOutputProviderDeployment(
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
    def to_dict(value: Union[CallbacksCreateOutputProviderDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksCreateOutputDestinations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateOutputDestinations:
        return CallbacksCreateOutputDestinations(
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
    def to_dict(value: Union[CallbacksCreateOutputDestinations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksCreateOutputProviderTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateOutputProviderTriggersProviderTrigger:
        return CallbacksCreateOutputProviderTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksCreateOutputProviderTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksCreateOutputProviderTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateOutputProviderTriggers:
        return CallbacksCreateOutputProviderTriggers(
        object=data.get('object'),
        id=data.get('id'),
        provider_trigger=mapCallbacksCreateOutputProviderTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None,
        event_types=data.get('event_types', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksCreateOutputProviderTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateOutput:
        return CallbacksCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        provider_deployment=mapCallbacksCreateOutputProviderDeployment.from_dict(data.get('provider_deployment')) if data.get('provider_deployment') else None,
        destinations=[mapCallbacksCreateOutputDestinations.from_dict(item) for item in data.get('destinations', []) if item],
        provider_triggers=[mapCallbacksCreateOutputProviderTriggers.from_dict(item) for item in data.get('provider_triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksCreateBodyTriggers:
    trigger_id: str
    event_types: Optional[List[str]] = None
@dataclass
class CallbacksCreateBody:
    provider_deployment_id: str
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None
    destination_ids: Optional[List[str]] = None
    triggers: Optional[List[CallbacksCreateBodyTriggers]] = None


class mapCallbacksCreateBodyTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateBodyTriggers:
        return CallbacksCreateBodyTriggers(
        trigger_id=data.get('trigger_id'),
        event_types=data.get('event_types', [])
        )

    @staticmethod
    def to_dict(value: Union[CallbacksCreateBodyTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksCreateBody:
        return CallbacksCreateBody(
        provider_deployment_id=data.get('provider_deployment_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        destination_ids=data.get('destination_ids', []),
        triggers=[mapCallbacksCreateBodyTriggers.from_dict(item) for item in data.get('triggers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[CallbacksCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

