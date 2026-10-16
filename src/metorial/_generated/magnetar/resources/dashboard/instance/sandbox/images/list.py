from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxImagesListOutputItems:
    object: str
    metadata: Dict[str, Any]
    id: str
    owner: str
    status: str
    regions: List[str]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    identifier: Optional[str] = None
    latest_version_id: Optional[str] = None
    latest_version_number: Optional[float] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSandboxImagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxImagesListOutput:
    items: List[DashboardInstanceSandboxImagesListOutputItems]
    pagination: DashboardInstanceSandboxImagesListOutputPagination


class mapDashboardInstanceSandboxImagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImagesListOutputItems:
        return DashboardInstanceSandboxImagesListOutputItems(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        owner=data.get('owner'),
        status=data.get('status'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        regions=data.get('regions', []),
        latest_version_id=data.get('latest_version_id'),
        latest_version_number=data.get('latest_version_number'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxImagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImagesListOutputPagination:
        return DashboardInstanceSandboxImagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxImagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImagesListOutput:
        return DashboardInstanceSandboxImagesListOutput(
        items=[mapDashboardInstanceSandboxImagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxImagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxImagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    owner: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapDashboardInstanceSandboxImagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImagesListQuery:
        return DashboardInstanceSandboxImagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        owner=data.get('owner'),
        status=data.get('status'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

