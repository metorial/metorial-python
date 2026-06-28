from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsListOutputItemsSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class PortalsListOutputItemsAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[PortalsListOutputItemsAuthAllowedRedirectUrlFilters]
@dataclass
class PortalsListOutputItemsUrls:
    type: str
    url: str
@dataclass
class PortalsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: PortalsListOutputItemsSkillConfiguration
    auth: PortalsListOutputItemsAuth
    urls: List[PortalsListOutputItemsUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsListOutput:
    items: List[PortalsListOutputItems]
    pagination: PortalsListOutputPagination


class mapPortalsListOutputItemsSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsSkillConfiguration:
        return PortalsListOutputItemsSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItemsAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsAuthAllowedRedirectUrlFilters:
        return PortalsListOutputItemsAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsAuth:
        return PortalsListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapPortalsListOutputItemsAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItemsUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsUrls:
        return PortalsListOutputItemsUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItems:
        return PortalsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapPortalsListOutputItemsSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapPortalsListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsListOutputItemsUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputPagination:
        return PortalsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutput:
        return PortalsListOutput(
        items=[mapPortalsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapPortalsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None


class mapPortalsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListQuery:
        return PortalsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

