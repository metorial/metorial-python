from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsCreateOutputSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class ManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class ManagementInstancePortalsCreateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[ManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class ManagementInstancePortalsCreateOutputUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: ManagementInstancePortalsCreateOutputSkillConfiguration
    auth: ManagementInstancePortalsCreateOutputAuth
    urls: List[ManagementInstancePortalsCreateOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsCreateOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputSkillConfiguration:
        return ManagementInstancePortalsCreateOutputSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters:
        return ManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputAuth:
        return ManagementInstancePortalsCreateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapManagementInstancePortalsCreateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputUrls:
        return ManagementInstancePortalsCreateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutput:
        return ManagementInstancePortalsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapManagementInstancePortalsCreateOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapManagementInstancePortalsCreateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsCreateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class ManagementInstancePortalsCreateBody:
    name: str
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[ManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None
    allow_consumer_skill_authoring: Optional[bool] = None
    allow_consumer_skill_publishing: Optional[bool] = None


class mapManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters:
        return ManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateBody:
        return ManagementInstancePortalsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapManagementInstancePortalsCreateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

