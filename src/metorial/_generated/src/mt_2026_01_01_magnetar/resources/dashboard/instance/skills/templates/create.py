from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceSkillsTemplatesCreateOutputItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: DashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsTemplatesCreateOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsTemplatesCreateOutputItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[DashboardInstanceSkillsTemplatesCreateOutputItemsIntegration] = None
    provider: Optional[DashboardInstanceSkillsTemplatesCreateOutputItemsProvider] = None
@dataclass
class DashboardInstanceSkillsTemplatesCreateOutput:
    object: str
    id: str
    status: str
    owner: str
    slug: str
    name: str
    metadata: Dict[str, Any]
    store_id: str
    items: List[DashboardInstanceSkillsTemplatesCreateOutputItems]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration:
        return DashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesCreateOutputItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesCreateOutputItemsIntegration:
        return DashboardInstanceSkillsTemplatesCreateOutputItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapDashboardInstanceSkillsTemplatesCreateOutputItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesCreateOutputItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesCreateOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesCreateOutputItemsProvider:
        return DashboardInstanceSkillsTemplatesCreateOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesCreateOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesCreateOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesCreateOutputItems:
        return DashboardInstanceSkillsTemplatesCreateOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapDashboardInstanceSkillsTemplatesCreateOutputItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapDashboardInstanceSkillsTemplatesCreateOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesCreateOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesCreateOutput:
        return DashboardInstanceSkillsTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        owner=data.get('owner'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        store_id=data.get('store_id'),
        items=[mapDashboardInstanceSkillsTemplatesCreateOutputItems.from_dict(item) for item in data.get('items', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    from_skill_id: Optional[str] = None


class mapDashboardInstanceSkillsTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesCreateBody:
        return DashboardInstanceSkillsTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_skill_id=data.get('from_skill_Id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

