from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsCreateOutputSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class DashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class DashboardInstancePortalsCreateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[DashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class DashboardInstancePortalsCreateOutputUrls:
    type: str
    url: str
@dataclass
class DashboardInstancePortalsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: DashboardInstancePortalsCreateOutputSkillConfiguration
    auth: DashboardInstancePortalsCreateOutputAuth
    urls: List[DashboardInstancePortalsCreateOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstancePortalsCreateOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateOutputSkillConfiguration:
        return DashboardInstancePortalsCreateOutputSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters:
        return DashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsCreateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateOutputAuth:
        return DashboardInstancePortalsCreateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapDashboardInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsCreateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateOutputUrls:
        return DashboardInstancePortalsCreateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateOutput:
        return DashboardInstancePortalsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapDashboardInstancePortalsCreateOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapDashboardInstancePortalsCreateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapDashboardInstancePortalsCreateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class DashboardInstancePortalsCreateBody:
    name: str
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[DashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None
    allow_consumer_skill_authoring: Optional[bool] = None
    allow_consumer_skill_publishing: Optional[bool] = None


class mapDashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters:
        return DashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsCreateBody:
        return DashboardInstancePortalsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapDashboardInstancePortalsCreateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

