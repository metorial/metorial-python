from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxImagesListOutputItems:
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
class ManagementInstanceSandboxImagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSandboxImagesListOutput:
    items: List[ManagementInstanceSandboxImagesListOutputItems]
    pagination: ManagementInstanceSandboxImagesListOutputPagination


class mapManagementInstanceSandboxImagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesListOutputItems:
        return ManagementInstanceSandboxImagesListOutputItems(
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
    def to_dict(value: Union[ManagementInstanceSandboxImagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesListOutputPagination:
        return ManagementInstanceSandboxImagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesListOutput:
        return ManagementInstanceSandboxImagesListOutput(
        items=[mapManagementInstanceSandboxImagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSandboxImagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxImagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    owner: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapManagementInstanceSandboxImagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesListQuery:
        return ManagementInstanceSandboxImagesListQuery(
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
    def to_dict(value: Union[ManagementInstanceSandboxImagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

