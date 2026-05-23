from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration:
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
@dataclass
class ManagementInstanceConsumerSurfacesListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class ManagementInstanceConsumerSurfacesListOutputItems:
    object: str
    id: str
    status: str
    name: str
    allow_consumer_skill_authoring: bool
    allow_consumer_skill_publishing: bool
    skill_configuration: ManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration
    auth: ManagementInstanceConsumerSurfacesListOutputItemsAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceConsumerSurfacesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceConsumerSurfacesListOutput:
    items: List[ManagementInstanceConsumerSurfacesListOutputItems]
    pagination: ManagementInstanceConsumerSurfacesListOutputPagination


class mapManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration:
        return ManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration(
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumerSurfacesListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumerSurfacesListOutputItemsAuth:
        return ManagementInstanceConsumerSurfacesListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        email_whitelist=data.get('email_whitelist', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumerSurfacesListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumerSurfacesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumerSurfacesListOutputItems:
        return ManagementInstanceConsumerSurfacesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        allow_consumer_skill_authoring=data.get('allow_consumer_skill_authoring'),
        allow_consumer_skill_publishing=data.get('allow_consumer_skill_publishing'),
        skill_configuration=mapManagementInstanceConsumerSurfacesListOutputItemsSkillConfiguration.from_dict(data.get('skill_configuration')) if data.get('skill_configuration') else None,
        auth=mapManagementInstanceConsumerSurfacesListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumerSurfacesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumerSurfacesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumerSurfacesListOutputPagination:
        return ManagementInstanceConsumerSurfacesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumerSurfacesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumerSurfacesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumerSurfacesListOutput:
        return ManagementInstanceConsumerSurfacesListOutput(
        items=[mapManagementInstanceConsumerSurfacesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceConsumerSurfacesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumerSurfacesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConsumerSurfacesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceConsumerSurfacesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumerSurfacesListQuery:
        return ManagementInstanceConsumerSurfacesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumerSurfacesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

