from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsAccessGetOutputGrantsSubject:
    type: str
    consumer_profile_id: Optional[str] = None
    consumer_group_id: Optional[str] = None
    name: Optional[str] = None
@dataclass
class ManagementInstanceSkillsAccessGetOutputGrants:
    object: str
    level: str
    subject: ManagementInstanceSkillsAccessGetOutputGrantsSubject
@dataclass
class ManagementInstanceSkillsAccessGetOutput:
    object: str
    skill_id: str
    grants: List[ManagementInstanceSkillsAccessGetOutputGrants]


class mapManagementInstanceSkillsAccessGetOutputGrantsSubject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAccessGetOutputGrantsSubject:
        return ManagementInstanceSkillsAccessGetOutputGrantsSubject(
        type=data.get('type'),
        consumer_profile_id=data.get('consumer_profile_id'),
        consumer_group_id=data.get('consumer_group_id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAccessGetOutputGrantsSubject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsAccessGetOutputGrants:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAccessGetOutputGrants:
        return ManagementInstanceSkillsAccessGetOutputGrants(
        object=data.get('object'),
        level=data.get('level'),
        subject=mapManagementInstanceSkillsAccessGetOutputGrantsSubject.from_dict(data.get('subject')) if data.get('subject') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAccessGetOutputGrants, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsAccessGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAccessGetOutput:
        return ManagementInstanceSkillsAccessGetOutput(
        object=data.get('object'),
        skill_id=data.get('skill_id'),
        grants=[mapManagementInstanceSkillsAccessGetOutputGrants.from_dict(item) for item in data.get('grants', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAccessGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

