from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsTemplatesListOutputItemsItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class SkillsTemplatesListOutputItemsItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: SkillsTemplatesListOutputItemsItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class SkillsTemplatesListOutputItemsItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsTemplatesListOutputItemsItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[SkillsTemplatesListOutputItemsItemsIntegration] = None
    provider: Optional[SkillsTemplatesListOutputItemsItemsProvider] = None
@dataclass
class SkillsTemplatesListOutputItems:
    object: str
    id: str
    status: str
    owner: str
    slug: str
    name: str
    metadata: Dict[str, Any]
    store_id: str
    items: List[SkillsTemplatesListOutputItemsItems]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsTemplatesListOutput:
    items: List[SkillsTemplatesListOutputItems]
    pagination: SkillsTemplatesListOutputPagination


class mapSkillsTemplatesListOutputItemsItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutputItemsItemsIntegrationConfiguration:
        return SkillsTemplatesListOutputItemsItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutputItemsItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesListOutputItemsItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutputItemsItemsIntegration:
        return SkillsTemplatesListOutputItemsItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapSkillsTemplatesListOutputItemsItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutputItemsItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesListOutputItemsItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutputItemsItemsProvider:
        return SkillsTemplatesListOutputItemsItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutputItemsItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesListOutputItemsItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutputItemsItems:
        return SkillsTemplatesListOutputItemsItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapSkillsTemplatesListOutputItemsItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapSkillsTemplatesListOutputItemsItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutputItemsItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutputItems:
        return SkillsTemplatesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        owner=data.get('owner'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        store_id=data.get('store_id'),
        items=[mapSkillsTemplatesListOutputItemsItems.from_dict(item) for item in data.get('items', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutputPagination:
        return SkillsTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListOutput:
        return SkillsTemplatesListOutput(
        items=[mapSkillsTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsTemplatesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsTemplatesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsTemplatesListQuery:
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
    created_at: Optional[SkillsTemplatesListQueryCreatedAt] = None
    updated_at: Optional[SkillsTemplatesListQueryUpdatedAt] = None


class mapSkillsTemplatesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesListQuery:
        return SkillsTemplatesListQuery(
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
        created_at=mapSkillsTemplatesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSkillsTemplatesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

