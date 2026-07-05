from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsTemplatesUpdateOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsTemplatesUpdateOutputItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration] = None
    provider: Optional[DashboardInstanceSkillsTemplatesUpdateOutputItemsProvider] = None
@dataclass
class DashboardInstanceSkillsTemplatesUpdateOutput:
    object: str
    id: str
    status: str
    owner: str
    slug: str
    name: str
    metadata: Dict[str, Any]
    store_id: str
    items: List[DashboardInstanceSkillsTemplatesUpdateOutputItems]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration:
        return DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration:
        return DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapDashboardInstanceSkillsTemplatesUpdateOutputItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesUpdateOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesUpdateOutputItemsProvider:
        return DashboardInstanceSkillsTemplatesUpdateOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesUpdateOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesUpdateOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesUpdateOutputItems:
        return DashboardInstanceSkillsTemplatesUpdateOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapDashboardInstanceSkillsTemplatesUpdateOutputItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapDashboardInstanceSkillsTemplatesUpdateOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesUpdateOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesUpdateOutput:
        return DashboardInstanceSkillsTemplatesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        owner=data.get('owner'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        store_id=data.get('store_id'),
        items=[mapDashboardInstanceSkillsTemplatesUpdateOutputItems.from_dict(item) for item in data.get('items', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsTemplatesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSkillsTemplatesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesUpdateBody:
        return DashboardInstanceSkillsTemplatesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

