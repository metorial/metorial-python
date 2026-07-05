from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsVersionsGetOutput:
    object: str
    id: str
    skill_id: str
    store_id: str
    store_version_id: str
    version_number: float
    created_at: datetime


class mapManagementInstanceSkillsVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsVersionsGetOutput:
        return ManagementInstanceSkillsVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        store_id=data.get('store_id'),
        store_version_id=data.get('store_version_id'),
        version_number=data.get('version_number'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

