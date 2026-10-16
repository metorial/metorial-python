from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxImagesListOutputItems:
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
class SandboxImagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxImagesListOutput:
    items: List[SandboxImagesListOutputItems]
    pagination: SandboxImagesListOutputPagination


class mapSandboxImagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesListOutputItems:
        return SandboxImagesListOutputItems(
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
    def to_dict(value: Union[SandboxImagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesListOutputPagination:
        return SandboxImagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesListOutput:
        return SandboxImagesListOutput(
        items=[mapSandboxImagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxImagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxImagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    owner: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapSandboxImagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesListQuery:
        return SandboxImagesListQuery(
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
    def to_dict(value: Union[SandboxImagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

