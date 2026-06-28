from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConsumerSurfacesGetOutputSkillConfiguration:
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class DashboardInstanceConsumerSurfacesGetOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class DashboardInstanceConsumerSurfacesGetOutput:
    object: str
    id: str
    status: str
    name: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: DashboardInstanceConsumerSurfacesGetOutputSkillConfiguration
    auth: DashboardInstanceConsumerSurfacesGetOutputAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstanceConsumerSurfacesGetOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesGetOutputSkillConfiguration:
        return DashboardInstanceConsumerSurfacesGetOutputSkillConfiguration(
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesGetOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumerSurfacesGetOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesGetOutputAuth:
        return DashboardInstanceConsumerSurfacesGetOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        email_whitelist=data.get('email_whitelist', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesGetOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumerSurfacesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesGetOutput:
        return DashboardInstanceConsumerSurfacesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapDashboardInstanceConsumerSurfacesGetOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapDashboardInstanceConsumerSurfacesGetOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

