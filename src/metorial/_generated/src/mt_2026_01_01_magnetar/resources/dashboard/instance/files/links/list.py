from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFilesLinksListOutputItems:
    object: str
    id: str
    file_id: str
    url: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class DashboardInstanceFilesLinksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceFilesLinksListOutput:
    items: List[DashboardInstanceFilesLinksListOutputItems]
    pagination: DashboardInstanceFilesLinksListOutputPagination


class mapDashboardInstanceFilesLinksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesLinksListOutputItems:
        return DashboardInstanceFilesLinksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesLinksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesLinksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesLinksListOutputPagination:
        return DashboardInstanceFilesLinksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesLinksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesLinksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesLinksListOutput:
        return DashboardInstanceFilesLinksListOutput(
        items=[mapDashboardInstanceFilesLinksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceFilesLinksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesLinksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceFilesLinksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    file_id: Optional[str] = None


class mapDashboardInstanceFilesLinksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesLinksListQuery:
        return DashboardInstanceFilesLinksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        file_id=data.get('file_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesLinksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

