from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmInstallationListOutputItemsUser:
    id: str
    name: str
    email: str
    image_url: Optional[str] = None
@dataclass
class ManagementInstanceScmInstallationListOutputItems:
    object: str
    id: str
    provider: str
    user: ManagementInstanceScmInstallationListOutputItemsUser
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceScmInstallationListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceScmInstallationListOutput:
    items: List[ManagementInstanceScmInstallationListOutputItems]
    pagination: ManagementInstanceScmInstallationListOutputPagination


class mapManagementInstanceScmInstallationListOutputItemsUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationListOutputItemsUser:
        return ManagementInstanceScmInstallationListOutputItemsUser(
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationListOutputItemsUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmInstallationListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationListOutputItems:
        return ManagementInstanceScmInstallationListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        user=mapManagementInstanceScmInstallationListOutputItemsUser.from_dict(data.get('user')) if data.get('user') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmInstallationListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationListOutputPagination:
        return ManagementInstanceScmInstallationListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmInstallationListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationListOutput:
        return ManagementInstanceScmInstallationListOutput(
        items=[mapManagementInstanceScmInstallationListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceScmInstallationListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmInstallationListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceScmInstallationListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationListQuery:
        return ManagementInstanceScmInstallationListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
