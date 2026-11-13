from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksDeleteOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksDeleteOutputTriggerGroups:
    object: str
    key: str
    name: str
    selection_schema: Dict[str, Any]
    status: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceCallbacksDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_provider_id: str
    provider: ManagementInstanceCallbacksDeleteOutputProvider
    trigger_groups: List[ManagementInstanceCallbacksDeleteOutputTriggerGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    trigger_group_selections: Optional[Dict[str, Dict[str, Any]]] = None


class mapManagementInstanceCallbacksDeleteOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksDeleteOutputProvider:
        return ManagementInstanceCallbacksDeleteOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksDeleteOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksDeleteOutputTriggerGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksDeleteOutputTriggerGroups:
        return ManagementInstanceCallbacksDeleteOutputTriggerGroups(
        object=data.get('object'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        selection_schema=data.get('selection_schema'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksDeleteOutputTriggerGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksDeleteOutput:
        return ManagementInstanceCallbacksDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider=mapManagementInstanceCallbacksDeleteOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        trigger_group_selections=data.get('trigger_group_selections'),
        trigger_groups=[mapManagementInstanceCallbacksDeleteOutputTriggerGroups.from_dict(item) for item in data.get('trigger_groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

