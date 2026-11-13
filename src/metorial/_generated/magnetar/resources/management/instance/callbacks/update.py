from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksUpdateOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksUpdateOutputTriggerGroups:
    object: str
    key: str
    name: str
    selection_schema: Dict[str, Any]
    status: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_provider_id: str
    provider: ManagementInstanceCallbacksUpdateOutputProvider
    trigger_groups: List[ManagementInstanceCallbacksUpdateOutputTriggerGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    trigger_group_selections: Optional[Dict[str, Dict[str, Any]]] = None


class mapManagementInstanceCallbacksUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutputProvider:
        return ManagementInstanceCallbacksUpdateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksUpdateOutputTriggerGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateOutputTriggerGroups:
        return ManagementInstanceCallbacksUpdateOutputTriggerGroups(
        object=data.get('object'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        selection_schema=data.get('selection_schema'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateOutputTriggerGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider=mapManagementInstanceCallbacksUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        trigger_group_selections=data.get('trigger_group_selections'),
        trigger_groups=[mapManagementInstanceCallbacksUpdateOutputTriggerGroups.from_dict(item) for item in data.get('trigger_groups', []) if item],
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
class ManagementInstanceCallbacksUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    trigger_group_selections: Optional[Dict[str, Dict[str, Any]]] = None


class mapManagementInstanceCallbacksUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksUpdateBody:
        return ManagementInstanceCallbacksUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        trigger_group_selections=data.get('trigger_group_selections')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

