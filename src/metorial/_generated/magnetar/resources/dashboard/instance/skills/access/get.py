from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsAccessGetOutputGrantsSubject:
    type: str
    consumer_profile_id: Optional[str] = None
    consumer_group_id: Optional[str] = None
    name: Optional[str] = None
@dataclass
class DashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup:
    id: str
    name: str
@dataclass
class DashboardInstanceSkillsAccessGetOutputGrantsSource:
    type: str
    skill_group: Optional[DashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup] = None
@dataclass
class DashboardInstanceSkillsAccessGetOutputGrants:
    object: str
    level: str
    subject: DashboardInstanceSkillsAccessGetOutputGrantsSubject
    source: DashboardInstanceSkillsAccessGetOutputGrantsSource
@dataclass
class DashboardInstanceSkillsAccessGetOutput:
    object: str
    skill_id: str
    grants: List[DashboardInstanceSkillsAccessGetOutputGrants]


class mapDashboardInstanceSkillsAccessGetOutputGrantsSubject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsAccessGetOutputGrantsSubject:
        return DashboardInstanceSkillsAccessGetOutputGrantsSubject(
        type=data.get('type'),
        consumer_profile_id=data.get('consumer_profile_id'),
        consumer_group_id=data.get('consumer_group_id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsAccessGetOutputGrantsSubject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup:
        return DashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsAccessGetOutputGrantsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsAccessGetOutputGrantsSource:
        return DashboardInstanceSkillsAccessGetOutputGrantsSource(
        type=data.get('type'),
        skill_group=mapDashboardInstanceSkillsAccessGetOutputGrantsSourceSkillGroup.from_dict(data.get('skill_group')) if data.get('skill_group') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsAccessGetOutputGrantsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsAccessGetOutputGrants:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsAccessGetOutputGrants:
        return DashboardInstanceSkillsAccessGetOutputGrants(
        object=data.get('object'),
        level=data.get('level'),
        subject=mapDashboardInstanceSkillsAccessGetOutputGrantsSubject.from_dict(data.get('subject')) if data.get('subject') else None,
        source=mapDashboardInstanceSkillsAccessGetOutputGrantsSource.from_dict(data.get('source')) if data.get('source') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsAccessGetOutputGrants, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsAccessGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsAccessGetOutput:
        return DashboardInstanceSkillsAccessGetOutput(
        object=data.get('object'),
        skill_id=data.get('skill_id'),
        grants=[mapDashboardInstanceSkillsAccessGetOutputGrants.from_dict(item) for item in data.get('grants', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsAccessGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

