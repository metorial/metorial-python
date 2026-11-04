from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMcpAvailabilityGetOutput:
    object: str
    skill_id: str
    available: bool
    exceeded_limits: List[str]
    file_count: float
    size: float
    max_file_count: float
    max_size: float


class mapManagementInstanceSkillsMcpAvailabilityGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMcpAvailabilityGetOutput:
        return ManagementInstanceSkillsMcpAvailabilityGetOutput(
        object=data.get('object'),
        skill_id=data.get('skill_id'),
        available=data.get('available'),
        exceeded_limits=data.get('exceeded_limits', []),
        file_count=data.get('file_count'),
        size=data.get('size'),
        max_file_count=data.get('max_file_count'),
        max_size=data.get('max_size')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMcpAvailabilityGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

