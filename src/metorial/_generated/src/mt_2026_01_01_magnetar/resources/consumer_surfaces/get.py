from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerSurfacesGetOutputSkillConfiguration:
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class ConsumerSurfacesGetOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class ConsumerSurfacesGetOutput:
    object: str
    id: str
    status: str
    name: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: ConsumerSurfacesGetOutputSkillConfiguration
    auth: ConsumerSurfacesGetOutputAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapConsumerSurfacesGetOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesGetOutputSkillConfiguration:
        return ConsumerSurfacesGetOutputSkillConfiguration(
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesGetOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSurfacesGetOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesGetOutputAuth:
        return ConsumerSurfacesGetOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        email_whitelist=data.get('email_whitelist', [])
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesGetOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSurfacesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesGetOutput:
        return ConsumerSurfacesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapConsumerSurfacesGetOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapConsumerSurfacesGetOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

