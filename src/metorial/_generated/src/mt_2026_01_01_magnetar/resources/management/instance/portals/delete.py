from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsDeleteOutputSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class ManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class ManagementInstancePortalsDeleteOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[ManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters]
@dataclass
class ManagementInstancePortalsDeleteOutputUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: ManagementInstancePortalsDeleteOutputSkillConfiguration
    auth: ManagementInstancePortalsDeleteOutputAuth
    urls: List[ManagementInstancePortalsDeleteOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsDeleteOutputSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputSkillConfiguration:
        return ManagementInstancePortalsDeleteOutputSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters:
        return ManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputAuth:
        return ManagementInstancePortalsDeleteOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapManagementInstancePortalsDeleteOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputUrls:
        return ManagementInstancePortalsDeleteOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutput:
        return ManagementInstancePortalsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapManagementInstancePortalsDeleteOutputSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapManagementInstancePortalsDeleteOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsDeleteOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

