from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
    id: str
    name: str
@dataclass
class ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems:
    object: str
    skill_plugin_id: str
    skill_group: ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup
    shared_skill_count: float
    skill_ids_to_add: List[str]
    skill_ids_to_remove: List[str]
@dataclass
class ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceSkillsPluginsSkillGroupMatchesListOutput:
    object: str
    items: List[ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems]
    pagination: ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination


class mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
        return ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems:
        return ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems(
        object=data.get('object'),
        skill_plugin_id=data.get('skill_plugin_id'),
        skill_group=mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup.from_dict(data.get('skill_group')) if data.get('skill_group') else None,
        shared_skill_count=data.get('shared_skill_count'),
        skill_ids_to_add=data.get('skill_ids_to_add', []),
        skill_ids_to_remove=data.get('skill_ids_to_remove', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination:
        return ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsPluginsSkillGroupMatchesListOutput:
        return ManagementInstanceSkillsPluginsSkillGroupMatchesListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsPluginsSkillGroupMatchesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsPluginsSkillGroupMatchesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsPluginsSkillGroupMatchesListQuery:
    skill_group_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSkillsPluginsSkillGroupMatchesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsPluginsSkillGroupMatchesListQuery:
        return ManagementInstanceSkillsPluginsSkillGroupMatchesListQuery(
        skill_group_id=data.get('skill_group_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsPluginsSkillGroupMatchesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

