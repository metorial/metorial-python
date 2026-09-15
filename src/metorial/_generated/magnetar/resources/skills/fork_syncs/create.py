from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsForkSyncsCreateOutput:
    object: str
    id: str
    status: str
    fork_skill_id: str
    upstream_skill_id: str
    created_at: datetime
    updated_at: datetime
    merge_request_id: Optional[str] = None
    error: Optional[str] = None
    processing_started_at: Optional[datetime] = None
    action_required_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    failed_at: Optional[datetime] = None
    cancelled_at: Optional[datetime] = None


class mapSkillsForkSyncsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsForkSyncsCreateOutput:
        return SkillsForkSyncsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        fork_skill_id=data.get('fork_skill_id'),
        upstream_skill_id=data.get('upstream_skill_id'),
        merge_request_id=data.get('merge_request_id'),
        error=data.get('error'),
        processing_started_at=datetime.fromisoformat(data.get('processing_started_at').replace('Z', '+00:00')) if data.get('processing_started_at') else None,
        action_required_at=datetime.fromisoformat(data.get('action_required_at').replace('Z', '+00:00')) if data.get('action_required_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        failed_at=datetime.fromisoformat(data.get('failed_at').replace('Z', '+00:00')) if data.get('failed_at') else None,
        cancelled_at=datetime.fromisoformat(data.get('cancelled_at').replace('Z', '+00:00')) if data.get('cancelled_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsForkSyncsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsForkSyncsCreateBody:
    skill_id: str


class mapSkillsForkSyncsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsForkSyncsCreateBody:
        return SkillsForkSyncsCreateBody(
        skill_id=data.get('skill_id')
        )

    @staticmethod
    def to_dict(value: Union[SkillsForkSyncsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

