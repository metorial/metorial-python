from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsTemplatesItemsListOutputItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
@dataclass
class SkillsTemplatesItemsListOutputItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: SkillsTemplatesItemsListOutputItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class SkillsTemplatesItemsListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsTemplatesItemsListOutputItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[SkillsTemplatesItemsListOutputItemsIntegration] = None
    provider: Optional[SkillsTemplatesItemsListOutputItemsProvider] = None
@dataclass
class SkillsTemplatesItemsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsTemplatesItemsListOutput:
    items: List[SkillsTemplatesItemsListOutputItems]
    pagination: SkillsTemplatesItemsListOutputPagination


class mapSkillsTemplatesItemsListOutputItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListOutputItemsIntegrationConfiguration:
        return SkillsTemplatesItemsListOutputItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListOutputItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesItemsListOutputItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListOutputItemsIntegration:
        return SkillsTemplatesItemsListOutputItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapSkillsTemplatesItemsListOutputItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListOutputItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesItemsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListOutputItemsProvider:
        return SkillsTemplatesItemsListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesItemsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListOutputItems:
        return SkillsTemplatesItemsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapSkillsTemplatesItemsListOutputItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapSkillsTemplatesItemsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesItemsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListOutputPagination:
        return SkillsTemplatesItemsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesItemsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListOutput:
        return SkillsTemplatesItemsListOutput(
        items=[mapSkillsTemplatesItemsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsTemplatesItemsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsTemplatesItemsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSkillsTemplatesItemsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesItemsListQuery:
        return SkillsTemplatesItemsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesItemsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

