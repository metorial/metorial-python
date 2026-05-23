from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsUpdateOutputSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class ManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class ManagementInstancePortalsUpdateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[ManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class ManagementInstancePortalsUpdateOutputUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: ManagementInstancePortalsUpdateOutputSkillConfiguration
    auth: ManagementInstancePortalsUpdateOutputAuth
    urls: List[ManagementInstancePortalsUpdateOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsUpdateOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputSkillConfiguration:
        return ManagementInstancePortalsUpdateOutputSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters:
        return ManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputAuth:
        return ManagementInstancePortalsUpdateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapManagementInstancePortalsUpdateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputUrls:
        return ManagementInstancePortalsUpdateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutput:
        return ManagementInstancePortalsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapManagementInstancePortalsUpdateOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapManagementInstancePortalsUpdateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsUpdateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class ManagementInstancePortalsUpdateBodySkillConfiguration:
    allow_scripts: Optional[bool] = None
    allowed_file_extensions: Optional[List[str]] = None
    allow_non_standard_directories: Optional[bool] = None
@dataclass
class ManagementInstancePortalsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[ManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None
    allow_consumer_skill_authoring: Optional[bool] = None
    allow_consumer_skill_publishing: Optional[bool] = None
    skill_configuration: Optional[ManagementInstancePortalsUpdateBodySkillConfiguration] = None


class mapManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters:
        return ManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateBodySkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateBodySkillConfiguration:
        return ManagementInstancePortalsUpdateBodySkillConfiguration(
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateBodySkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateBody:
        return ManagementInstancePortalsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapManagementInstancePortalsUpdateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapManagementInstancePortalsUpdateBodySkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

