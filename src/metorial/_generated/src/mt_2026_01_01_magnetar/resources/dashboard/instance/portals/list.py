from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsListOutputItemsSkillConfiguration:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class DashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class DashboardInstancePortalsListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[DashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters]
@dataclass
class DashboardInstancePortalsListOutputItemsUrls:
    type: str
    url: str
@dataclass
class DashboardInstancePortalsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    slug: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: DashboardInstancePortalsListOutputItemsSkillConfiguration
    auth: DashboardInstancePortalsListOutputItemsAuth
    urls: List[DashboardInstancePortalsListOutputItemsUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsListOutput:
    items: List[DashboardInstancePortalsListOutputItems]
    pagination: DashboardInstancePortalsListOutputPagination


class mapDashboardInstancePortalsListOutputItemsSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutputItemsSkillConfiguration:
        return DashboardInstancePortalsListOutputItemsSkillConfiguration(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutputItemsSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters:
        return DashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutputItemsAuth:
        return DashboardInstancePortalsListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapDashboardInstancePortalsListOutputItemsAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListOutputItemsUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutputItemsUrls:
        return DashboardInstancePortalsListOutputItemsUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutputItemsUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutputItems:
        return DashboardInstancePortalsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapDashboardInstancePortalsListOutputItemsSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapDashboardInstancePortalsListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapDashboardInstancePortalsListOutputItemsUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutputPagination:
        return DashboardInstancePortalsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListOutput:
        return DashboardInstancePortalsListOutput(
        items=[mapDashboardInstancePortalsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None


class mapDashboardInstancePortalsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListQuery:
        return DashboardInstancePortalsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

