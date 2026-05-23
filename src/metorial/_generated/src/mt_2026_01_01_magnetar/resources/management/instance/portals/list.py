from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsListOutputItemsSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class ManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class ManagementInstancePortalsListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[ManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters]
@dataclass
class ManagementInstancePortalsListOutputItemsUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: ManagementInstancePortalsListOutputItemsSkillConfiguration
    auth: ManagementInstancePortalsListOutputItemsAuth
    urls: List[ManagementInstancePortalsListOutputItemsUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstancePortalsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsListOutput:
    items: List[ManagementInstancePortalsListOutputItems]
    pagination: ManagementInstancePortalsListOutputPagination


class mapManagementInstancePortalsListOutputItemsSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutputItemsSkillConfiguration:
        return ManagementInstancePortalsListOutputItemsSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutputItemsSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters:
        return ManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutputItemsAuth:
        return ManagementInstancePortalsListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapManagementInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListOutputItemsUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutputItemsUrls:
        return ManagementInstancePortalsListOutputItemsUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutputItemsUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutputItems:
        return ManagementInstancePortalsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapManagementInstancePortalsListOutputItemsSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapManagementInstancePortalsListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsListOutputItemsUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutputPagination:
        return ManagementInstancePortalsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListOutput:
        return ManagementInstancePortalsListOutput(
        items=[mapManagementInstancePortalsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstancePortalsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListQuery:
        return ManagementInstancePortalsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

