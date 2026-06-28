from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsTemplatesListOutputItemsItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsTemplatesListOutputItemsItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration] = None
    provider: Optional[DashboardInstanceSkillsTemplatesListOutputItemsItemsProvider] = None
@dataclass
class DashboardInstanceSkillsTemplatesListOutputItems:
    object: str
    id: str
    status: str
    owner: str
    slug: str
    name: str
    metadata: Dict[str, Any]
    store_id: str
    items: List[DashboardInstanceSkillsTemplatesListOutputItemsItems]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsTemplatesListOutput:
    items: List[DashboardInstanceSkillsTemplatesListOutputItems]
    pagination: DashboardInstanceSkillsTemplatesListOutputPagination


class mapDashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration:
        return DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration:
        return DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapDashboardInstanceSkillsTemplatesListOutputItemsItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesListOutputItemsItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutputItemsItemsProvider:
        return DashboardInstanceSkillsTemplatesListOutputItemsItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutputItemsItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesListOutputItemsItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutputItemsItems:
        return DashboardInstanceSkillsTemplatesListOutputItemsItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapDashboardInstanceSkillsTemplatesListOutputItemsItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapDashboardInstanceSkillsTemplatesListOutputItemsItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutputItemsItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutputItems:
        return DashboardInstanceSkillsTemplatesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        owner=data.get('owner'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        store_id=data.get('store_id'),
        items=[mapDashboardInstanceSkillsTemplatesListOutputItemsItems.from_dict(item) for item in data.get('items', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutputPagination:
        return DashboardInstanceSkillsTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListOutput:
        return DashboardInstanceSkillsTemplatesListOutput(
        items=[mapDashboardInstanceSkillsTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsTemplatesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsTemplatesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsTemplatesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    owner: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceSkillsTemplatesListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceSkillsTemplatesListQueryUpdatedAt] = None


class mapDashboardInstanceSkillsTemplatesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsTemplatesListQuery:
        return DashboardInstanceSkillsTemplatesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        owner=data.get('owner'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        integration_id=data.get('integration_id'),
        created_at=mapDashboardInstanceSkillsTemplatesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceSkillsTemplatesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsTemplatesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

