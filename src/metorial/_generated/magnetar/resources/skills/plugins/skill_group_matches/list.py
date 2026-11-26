from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
    id: str
    name: str
@dataclass
class SkillsPluginsSkillGroupMatchesListOutputItems:
    object: str
    skill_plugin_id: str
    skill_group: SkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup
    shared_skill_count: float
    skill_ids_to_add: List[str]
    skill_ids_to_remove: List[str]
@dataclass
class SkillsPluginsSkillGroupMatchesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class SkillsPluginsSkillGroupMatchesListOutput:
    object: str
    items: List[SkillsPluginsSkillGroupMatchesListOutputItems]
    pagination: SkillsPluginsSkillGroupMatchesListOutputPagination


class mapSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
        return SkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsSkillGroupMatchesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillGroupMatchesListOutputItems:
        return SkillsPluginsSkillGroupMatchesListOutputItems(
        object=data.get('object'),
        skill_plugin_id=data.get('skill_plugin_id'),
        skill_group=mapSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup.from_dict(data.get('skill_group')) if data.get('skill_group') else None,
        shared_skill_count=data.get('shared_skill_count'),
        skill_ids_to_add=data.get('skill_ids_to_add', []),
        skill_ids_to_remove=data.get('skill_ids_to_remove', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillGroupMatchesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsSkillGroupMatchesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillGroupMatchesListOutputPagination:
        return SkillsPluginsSkillGroupMatchesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillGroupMatchesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsSkillGroupMatchesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillGroupMatchesListOutput:
        return SkillsPluginsSkillGroupMatchesListOutput(
        object=data.get('object'),
        items=[mapSkillsPluginsSkillGroupMatchesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsPluginsSkillGroupMatchesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillGroupMatchesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsPluginsSkillGroupMatchesListQuery:
    skill_group_id: Optional[Union[str, List[str]]] = None


class mapSkillsPluginsSkillGroupMatchesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillGroupMatchesListQuery:
        return SkillsPluginsSkillGroupMatchesListQuery(
        skill_group_id=data.get('skill_group_id')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillGroupMatchesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

