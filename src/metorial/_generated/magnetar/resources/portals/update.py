from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsUpdateOutputSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class PortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsUpdateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[PortalsUpdateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class PortalsUpdateOutputUrls:
    type: str
    url: str
@dataclass
class PortalsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: PortalsUpdateOutputSkillConfiguration
    auth: PortalsUpdateOutputAuth
    urls: List[PortalsUpdateOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsUpdateOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputSkillConfiguration:
        return PortalsUpdateOutputSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputAuthAllowedRedirectUrlFilters:
        return PortalsUpdateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputAuth:
        return PortalsUpdateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapPortalsUpdateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputUrls:
        return PortalsUpdateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutput:
        return PortalsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapPortalsUpdateOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapPortalsUpdateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsUpdateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsUpdateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsUpdateBodySkillConfiguration:
    allow_scripts: Optional[bool] = None
    allowed_file_extensions: Optional[List[str]] = None
    allow_non_standard_directories: Optional[bool] = None
@dataclass
class PortalsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[PortalsUpdateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None
    allow_consumer_skill_authoring: Optional[bool] = None
    allow_consumer_skill_publishing: Optional[bool] = None
    skill_configuration: Optional[PortalsUpdateBodySkillConfiguration] = None


class mapPortalsUpdateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateBodyAllowedRedirectUrlFilters:
        return PortalsUpdateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateBodySkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateBodySkillConfiguration:
        return PortalsUpdateBodySkillConfiguration(
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateBodySkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateBody:
        return PortalsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapPortalsUpdateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapPortalsUpdateBodySkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

