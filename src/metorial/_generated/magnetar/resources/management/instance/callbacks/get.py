from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksGetOutputProviderDeployment:
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
class ManagementInstanceCallbacksGetOutputDestinations:
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
class ManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
@dataclass
class ManagementInstanceCallbacksGetOutputProviderTriggers:
    object: str
    id: str
    provider_trigger: ManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger
    event_types: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceCallbacksGetOutput:
    object: str
    id: str
    status: str
    name: str
    provider_deployment: ManagementInstanceCallbacksGetOutputProviderDeployment
    destinations: List[ManagementInstanceCallbacksGetOutputDestinations]
    provider_triggers: List[ManagementInstanceCallbacksGetOutputProviderTriggers]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None


class mapManagementInstanceCallbacksGetOutputProviderDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksGetOutputProviderDeployment:
        return ManagementInstanceCallbacksGetOutputProviderDeployment(
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
    def to_dict(value: Union[ManagementInstanceCallbacksGetOutputProviderDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksGetOutputDestinations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksGetOutputDestinations:
        return ManagementInstanceCallbacksGetOutputDestinations(
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
    def to_dict(value: Union[ManagementInstanceCallbacksGetOutputDestinations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger:
        return ManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksGetOutputProviderTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksGetOutputProviderTriggers:
        return ManagementInstanceCallbacksGetOutputProviderTriggers(
        object=data.get('object'),
        id=data.get('id'),
        provider_trigger=mapManagementInstanceCallbacksGetOutputProviderTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None,
        event_types=data.get('event_types', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksGetOutputProviderTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksGetOutput:
        return ManagementInstanceCallbacksGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        provider_deployment=mapManagementInstanceCallbacksGetOutputProviderDeployment.from_dict(data.get('provider_deployment')) if data.get('provider_deployment') else None,
        destinations=[mapManagementInstanceCallbacksGetOutputDestinations.from_dict(item) for item in data.get('destinations', []) if item],
        provider_triggers=[mapManagementInstanceCallbacksGetOutputProviderTriggers.from_dict(item) for item in data.get('provider_triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

