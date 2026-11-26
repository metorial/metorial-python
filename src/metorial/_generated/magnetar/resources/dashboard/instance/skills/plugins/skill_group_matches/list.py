from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
    id: str
    name: str
@dataclass
class DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems:
    object: str
    skill_plugin_id: str
    skill_group: DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup
    shared_skill_count: float
    skill_ids_to_add: List[str]
    skill_ids_to_remove: List[str]
@dataclass
class DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput:
    object: str
    items: List[DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems]
    pagination: DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination


class mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup:
        return DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems:
        return DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems(
        object=data.get('object'),
        skill_plugin_id=data.get('skill_plugin_id'),
        skill_group=mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItemsSkillGroup.from_dict(data.get('skill_group')) if data.get('skill_group') else None,
        shared_skill_count=data.get('shared_skill_count'),
        skill_ids_to_add=data.get('skill_ids_to_add', []),
        skill_ids_to_remove=data.get('skill_ids_to_remove', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination:
        return DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput:
        return DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsPluginsSkillGroupMatchesListQuery:
    skill_group_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSkillsPluginsSkillGroupMatchesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsSkillGroupMatchesListQuery:
        return DashboardInstanceSkillsPluginsSkillGroupMatchesListQuery(
        skill_group_id=data.get('skill_group_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsSkillGroupMatchesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

