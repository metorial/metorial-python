from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsConfigurationsUpdateOutput:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


class mapSkillsConfigurationsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsConfigurationsUpdateOutput:
        return SkillsConfigurationsUpdateOutput(
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
    def to_dict(value: Union[SkillsConfigurationsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsConfigurationsUpdateBody:
    allow_scripts: Optional[bool] = None
    allowed_file_extensions: Optional[List[str]] = None
    allow_non_standard_directories: Optional[bool] = None


class mapSkillsConfigurationsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsConfigurationsUpdateBody:
        return SkillsConfigurationsUpdateBody(
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[SkillsConfigurationsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

