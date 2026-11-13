from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksCreateOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksCreateOutputTriggerGroups:
    object: str
    key: str
    name: str
    selection_schema: Dict[str, Any]
    status: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksCreateOutput:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_provider_id: str
    provider: ManagementInstanceCallbacksCreateOutputProvider
    trigger_groups: List[ManagementInstanceCallbacksCreateOutputTriggerGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    trigger_group_selections: Optional[Dict[str, Dict[str, Any]]] = None


class mapManagementInstanceCallbacksCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutputProvider:
        return ManagementInstanceCallbacksCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksCreateOutputTriggerGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateOutputTriggerGroups:
        return ManagementInstanceCallbacksCreateOutputTriggerGroups(
        object=data.get('object'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        selection_schema=data.get('selection_schema'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateOutputTriggerGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider=mapManagementInstanceCallbacksCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        trigger_group_selections=data.get('trigger_group_selections'),
        trigger_groups=[mapManagementInstanceCallbacksCreateOutputTriggerGroups.from_dict(item) for item in data.get('trigger_groups', []) if item],
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
class ManagementInstanceCallbacksCreateBody:
    integration_id: str
    integration_provider_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    trigger_group_selections: Optional[Dict[str, Dict[str, Any]]] = None


class mapManagementInstanceCallbacksCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksCreateBody:
        return ManagementInstanceCallbacksCreateBody(
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        name=data.get('name'),
        description=data.get('description'),
        trigger_group_selections=data.get('trigger_group_selections')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

