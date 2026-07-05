from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsUpdateOutputSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class DashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class DashboardInstancePortalsUpdateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[DashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class DashboardInstancePortalsUpdateOutputUrls:
    type: str
    url: str
@dataclass
class DashboardInstancePortalsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: DashboardInstancePortalsUpdateOutputSkillConfiguration
    auth: DashboardInstancePortalsUpdateOutputAuth
    urls: List[DashboardInstancePortalsUpdateOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstancePortalsUpdateOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputSkillConfiguration:
        return DashboardInstancePortalsUpdateOutputSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters:
        return DashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputAuth:
        return DashboardInstancePortalsUpdateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapDashboardInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputUrls:
        return DashboardInstancePortalsUpdateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutput:
        return DashboardInstancePortalsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapDashboardInstancePortalsUpdateOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapDashboardInstancePortalsUpdateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapDashboardInstancePortalsUpdateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class DashboardInstancePortalsUpdateBodySkillConfiguration:
    allow_scripts: Optional[bool] = None
    allowed_file_extensions: Optional[List[str]] = None
    allow_non_standard_directories: Optional[bool] = None
@dataclass
class DashboardInstancePortalsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[DashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None
    allow_consumer_skill_authoring: Optional[bool] = None
    allow_consumer_skill_publishing: Optional[bool] = None
    skill_configuration: Optional[DashboardInstancePortalsUpdateBodySkillConfiguration] = None


class mapDashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters:
        return DashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateBodySkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateBodySkillConfiguration:
        return DashboardInstancePortalsUpdateBodySkillConfiguration(
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateBodySkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateBody:
        return DashboardInstancePortalsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapDashboardInstancePortalsUpdateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapDashboardInstancePortalsUpdateBodySkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

