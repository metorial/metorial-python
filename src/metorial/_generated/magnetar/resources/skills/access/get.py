from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsAccessGetOutputGrantsSubject:
    type: str
    consumer_profile_id: Optional[str] = None
    consumer_group_id: Optional[str] = None
    name: Optional[str] = None
@dataclass
class SkillsAccessGetOutputGrantsSourceSkillGroup:
    id: str
    name: str
@dataclass
class SkillsAccessGetOutputGrantsSource:
    type: str
    skill_group: Optional[SkillsAccessGetOutputGrantsSourceSkillGroup] = None
@dataclass
class SkillsAccessGetOutputGrants:
    object: str
    level: str
    subject: SkillsAccessGetOutputGrantsSubject
    source: SkillsAccessGetOutputGrantsSource
@dataclass
class SkillsAccessGetOutput:
    object: str
    skill_id: str
    grants: List[SkillsAccessGetOutputGrants]


class mapSkillsAccessGetOutputGrantsSubject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAccessGetOutputGrantsSubject:
        return SkillsAccessGetOutputGrantsSubject(
        type=data.get('type'),
        consumer_profile_id=data.get('consumer_profile_id'),
        consumer_group_id=data.get('consumer_group_id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SkillsAccessGetOutputGrantsSubject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsAccessGetOutputGrantsSourceSkillGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAccessGetOutputGrantsSourceSkillGroup:
        return SkillsAccessGetOutputGrantsSourceSkillGroup(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SkillsAccessGetOutputGrantsSourceSkillGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsAccessGetOutputGrantsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAccessGetOutputGrantsSource:
        return SkillsAccessGetOutputGrantsSource(
        type=data.get('type'),
        skill_group=mapSkillsAccessGetOutputGrantsSourceSkillGroup.from_dict(data.get('skill_group')) if data.get('skill_group') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsAccessGetOutputGrantsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsAccessGetOutputGrants:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAccessGetOutputGrants:
        return SkillsAccessGetOutputGrants(
        object=data.get('object'),
        level=data.get('level'),
        subject=mapSkillsAccessGetOutputGrantsSubject.from_dict(data.get('subject')) if data.get('subject') else None,
        source=mapSkillsAccessGetOutputGrantsSource.from_dict(data.get('source')) if data.get('source') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsAccessGetOutputGrants, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsAccessGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAccessGetOutput:
        return SkillsAccessGetOutput(
        object=data.get('object'),
        skill_id=data.get('skill_id'),
        grants=[mapSkillsAccessGetOutputGrants.from_dict(item) for item in data.get('grants', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsAccessGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

