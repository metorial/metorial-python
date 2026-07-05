from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsConfigurationsGetOutput:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


class mapDashboardInstanceSkillsConfigurationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsConfigurationsGetOutput:
        return DashboardInstanceSkillsConfigurationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories'),
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsConfigurationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

