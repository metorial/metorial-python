from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksCreateOutputProviderDeployment:
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
class ManagementInstanceCallbacksCreateOutputDestinations:
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
class ManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
@dataclass
class ManagementInstanceCallbacksCreateOutputProviderTriggers:
    object: str
    id: str
    provider_trigger: ManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger
    event_types: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceCallbacksCreateOutput:
    object: str
    id: str
    status: str
    name: str
    provider_deployment: ManagementInstanceCallbacksCreateOutputProviderDeployment
    destinations: List[ManagementInstanceCallbacksCreateOutputDestinations]
    provider_triggers: List[ManagementInstanceCallbacksCreateOutputProviderTriggers]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None


class mapManagementInstanceCallbacksCreateOutputProviderDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutputProviderDeployment:
        return ManagementInstanceCallbacksCreateOutputProviderDeployment(
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
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutputProviderDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksCreateOutputDestinations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutputDestinations:
        return ManagementInstanceCallbacksCreateOutputDestinations(
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
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutputDestinations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger:
        return ManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksCreateOutputProviderTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutputProviderTriggers:
        return ManagementInstanceCallbacksCreateOutputProviderTriggers(
        object=data.get('object'),
        id=data.get('id'),
        provider_trigger=mapManagementInstanceCallbacksCreateOutputProviderTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None,
        event_types=data.get('event_types', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutputProviderTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutput:
        return ManagementInstanceCallbacksCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        provider_deployment=mapManagementInstanceCallbacksCreateOutputProviderDeployment.from_dict(data.get('provider_deployment')) if data.get('provider_deployment') else None,
        destinations=[mapManagementInstanceCallbacksCreateOutputDestinations.from_dict(item) for item in data.get('destinations', []) if item],
        provider_triggers=[mapManagementInstanceCallbacksCreateOutputProviderTriggers.from_dict(item) for item in data.get('provider_triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCallbacksCreateBodyTriggers:
    trigger_id: str
    event_types: Optional[List[str]] = None
@dataclass
class ManagementInstanceCallbacksCreateBody:
    provider_deployment_id: str
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None
    destination_ids: Optional[List[str]] = None
    triggers: Optional[List[ManagementInstanceCallbacksCreateBodyTriggers]] = None


class mapManagementInstanceCallbacksCreateBodyTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateBodyTriggers:
        return ManagementInstanceCallbacksCreateBodyTriggers(
        trigger_id=data.get('trigger_id'),
        event_types=data.get('event_types', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateBodyTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateBody:
        return ManagementInstanceCallbacksCreateBody(
        provider_deployment_id=data.get('provider_deployment_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        destination_ids=data.get('destination_ids', []),
        triggers=[mapManagementInstanceCallbacksCreateBodyTriggers.from_dict(item) for item in data.get('triggers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

