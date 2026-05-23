from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMarketplacesPluginsListOutputItemsSkillPluginSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsMarketplacesPluginsListOutputItemsSkillPlugin:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    skills: List[SkillsMarketplacesPluginsListOutputItemsSkillPluginSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsMarketplacesPluginsListOutputItems:
    object: str
    id: str
    status: str
    identifier: str
    created_at: datetime
    updated_at: datetime
    skill_configuration_id: Optional[str] = None
    skill_marketplace_id: Optional[str] = None
    skill_plugin_id: Optional[str] = None
    skill_plugin: Optional[SkillsMarketplacesPluginsListOutputItemsSkillPlugin] = None
@dataclass
class SkillsMarketplacesPluginsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsMarketplacesPluginsListOutput:
    items: List[SkillsMarketplacesPluginsListOutputItems]
    pagination: SkillsMarketplacesPluginsListOutputPagination


class mapSkillsMarketplacesPluginsListOutputItemsSkillPluginSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesPluginsListOutputItemsSkillPluginSkills:
        return SkillsMarketplacesPluginsListOutputItemsSkillPluginSkills(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        status=data.get('status'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        client_metadata=data.get('client_metadata'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_id=data.get('skill_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesPluginsListOutputItemsSkillPluginSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesPluginsListOutputItemsSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesPluginsListOutputItemsSkillPlugin:
        return SkillsMarketplacesPluginsListOutputItemsSkillPlugin(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sync_status=data.get('sync_status'),
        image_url=data.get('image_url'),
        name=data.get('name'),
        description=data.get('description'),
        long_description=data.get('long_description'),
        category=data.get('category'),
        slug=data.get('slug'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skills=[mapSkillsMarketplacesPluginsListOutputItemsSkillPluginSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesPluginsListOutputItemsSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesPluginsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesPluginsListOutputItems:
        return SkillsMarketplacesPluginsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        identifier=data.get('identifier'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_marketplace_id=data.get('skill_marketplace_id'),
        skill_plugin_id=data.get('skill_plugin_id'),
        skill_plugin=mapSkillsMarketplacesPluginsListOutputItemsSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesPluginsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesPluginsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesPluginsListOutputPagination:
        return SkillsMarketplacesPluginsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesPluginsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesPluginsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesPluginsListOutput:
        return SkillsMarketplacesPluginsListOutput(
        items=[mapSkillsMarketplacesPluginsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsMarketplacesPluginsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesPluginsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsMarketplacesPluginsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsMarketplacesPluginsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsMarketplacesPluginsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    skill_plugin_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    skill_configuration_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SkillsMarketplacesPluginsListQueryCreatedAt] = None
    updated_at: Optional[SkillsMarketplacesPluginsListQueryUpdatedAt] = None


class mapSkillsMarketplacesPluginsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesPluginsListQuery:
        return SkillsMarketplacesPluginsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        skill_plugin_id=data.get('skill_plugin_id'),
        status=data.get('status'),
        skill_configuration_id=data.get('skill_configuration_id'),
        created_at=mapSkillsMarketplacesPluginsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSkillsMarketplacesPluginsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesPluginsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

