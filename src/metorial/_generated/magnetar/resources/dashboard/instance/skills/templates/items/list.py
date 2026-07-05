from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsTemplatesItemsListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsTemplatesItemsListOutputItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration] = None
    provider: Optional[DashboardInstanceSkillsTemplatesItemsListOutputItemsProvider] = None
@dataclass
class DashboardInstanceSkillsTemplatesItemsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsTemplatesItemsListOutput:
    items: List[DashboardInstanceSkillsTemplatesItemsListOutputItems]
    pagination: DashboardInstanceSkillsTemplatesItemsListOutputPagination


class mapDashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration:
        return DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration:
        return DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapDashboardInstanceSkillsTemplatesItemsListOutputItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesItemsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListOutputItemsProvider:
        return DashboardInstanceSkillsTemplatesItemsListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesItemsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListOutputItems:
        return DashboardInstanceSkillsTemplatesItemsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapDashboardInstanceSkillsTemplatesItemsListOutputItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapDashboardInstanceSkillsTemplatesItemsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesItemsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListOutputPagination:
        return DashboardInstanceSkillsTemplatesItemsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesItemsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListOutput:
        return DashboardInstanceSkillsTemplatesItemsListOutput(
        items=[mapDashboardInstanceSkillsTemplatesItemsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsTemplatesItemsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsTemplatesItemsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceSkillsTemplatesItemsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesItemsListQuery:
        return DashboardInstanceSkillsTemplatesItemsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesItemsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

