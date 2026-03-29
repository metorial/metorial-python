from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksUpdateOutputProviderDeployment:
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
class ManagementInstanceCallbacksUpdateOutputDestinations:
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
class ManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger:
    object: str
    id: str
    key: str
    name: str
@dataclass
class ManagementInstanceCallbacksUpdateOutputProviderTriggers:
    object: str
    id: str
    provider_trigger: ManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger
    event_types: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceCallbacksUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    provider_deployment: ManagementInstanceCallbacksUpdateOutputProviderDeployment
    destinations: List[ManagementInstanceCallbacksUpdateOutputDestinations]
    provider_triggers: List[ManagementInstanceCallbacksUpdateOutputProviderTriggers]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None


class mapManagementInstanceCallbacksUpdateOutputProviderDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutputProviderDeployment:
        return ManagementInstanceCallbacksUpdateOutputProviderDeployment(
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
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutputProviderDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksUpdateOutputDestinations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutputDestinations:
        return ManagementInstanceCallbacksUpdateOutputDestinations(
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
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutputDestinations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger:
        return ManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksUpdateOutputProviderTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutputProviderTriggers:
        return ManagementInstanceCallbacksUpdateOutputProviderTriggers(
        object=data.get('object'),
        id=data.get('id'),
        provider_trigger=mapManagementInstanceCallbacksUpdateOutputProviderTriggersProviderTrigger.from_dict(data.get('provider_trigger')) if data.get('provider_trigger') else None,
        event_types=data.get('event_types', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutputProviderTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutput:
        return ManagementInstanceCallbacksUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        provider_deployment=mapManagementInstanceCallbacksUpdateOutputProviderDeployment.from_dict(data.get('provider_deployment')) if data.get('provider_deployment') else None,
        destinations=[mapManagementInstanceCallbacksUpdateOutputDestinations.from_dict(item) for item in data.get('destinations', []) if item],
        provider_triggers=[mapManagementInstanceCallbacksUpdateOutputProviderTriggers.from_dict(item) for item in data.get('provider_triggers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCallbacksUpdateBodyTriggers:
    trigger_id: str
    event_types: Optional[List[str]] = None
@dataclass
class ManagementInstanceCallbacksUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    poll_interval_seconds_override: Optional[float] = None
    destination_ids: Optional[List[str]] = None
    triggers: Optional[List[ManagementInstanceCallbacksUpdateBodyTriggers]] = None


class mapManagementInstanceCallbacksUpdateBodyTriggers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateBodyTriggers:
        return ManagementInstanceCallbacksUpdateBodyTriggers(
        trigger_id=data.get('trigger_id'),
        event_types=data.get('event_types', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateBodyTriggers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateBody:
        return ManagementInstanceCallbacksUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        poll_interval_seconds_override=data.get('poll_interval_seconds_override'),
        destination_ids=data.get('destination_ids', []),
        triggers=[mapManagementInstanceCallbacksUpdateBodyTriggers.from_dict(item) for item in data.get('triggers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

