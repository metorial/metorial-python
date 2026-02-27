from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmInstallationListOutputItemsUser:
    id: str
    name: str
    email: str
    image_url: Optional[str] = None
@dataclass
class DashboardInstanceScmInstallationListOutputItems:
    object: str
    id: str
    provider: str
    user: DashboardInstanceScmInstallationListOutputItemsUser
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceScmInstallationListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceScmInstallationListOutput:
    items: List[DashboardInstanceScmInstallationListOutputItems]
    pagination: DashboardInstanceScmInstallationListOutputPagination


class mapDashboardInstanceScmInstallationListOutputItemsUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationListOutputItemsUser:
        return DashboardInstanceScmInstallationListOutputItemsUser(
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationListOutputItemsUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmInstallationListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationListOutputItems:
        return DashboardInstanceScmInstallationListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        user=mapDashboardInstanceScmInstallationListOutputItemsUser.from_dict(data.get('user')) if data.get('user') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmInstallationListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationListOutputPagination:
        return DashboardInstanceScmInstallationListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmInstallationListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationListOutput:
        return DashboardInstanceScmInstallationListOutput(
        items=[mapDashboardInstanceScmInstallationListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceScmInstallationListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmInstallationListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceScmInstallationListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationListQuery:
        return DashboardInstanceScmInstallationListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
