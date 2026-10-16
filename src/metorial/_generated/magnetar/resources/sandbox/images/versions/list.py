from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxImagesVersionsListOutputItems:
    object: str
    id: str
    image_id: str
    status: str
    regions: List[str]
    created_at: datetime
    updated_at: datetime
    version_number: Optional[float] = None
    build_id: Optional[str] = None
@dataclass
class SandboxImagesVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxImagesVersionsListOutput:
    items: List[SandboxImagesVersionsListOutputItems]
    pagination: SandboxImagesVersionsListOutputPagination


class mapSandboxImagesVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesVersionsListOutputItems:
        return SandboxImagesVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        image_id=data.get('image_id'),
        version_number=data.get('version_number'),
        build_id=data.get('build_id'),
        status=data.get('status'),
        regions=data.get('regions', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImagesVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesVersionsListOutputPagination:
        return SandboxImagesVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImagesVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesVersionsListOutput:
        return SandboxImagesVersionsListOutput(
        items=[mapSandboxImagesVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxImagesVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxImagesVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSandboxImagesVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesVersionsListQuery:
        return SandboxImagesVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

