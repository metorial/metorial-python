from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxSpecsListOutputItems:
    object: str
    id: str
    identifier: str
    memory_gib: float
    cpus: float
    available: bool
    regions: List[str]
    created_at: datetime
@dataclass
class SandboxSpecsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxSpecsListOutput:
    items: List[SandboxSpecsListOutputItems]
    pagination: SandboxSpecsListOutputPagination


class mapSandboxSpecsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxSpecsListOutputItems:
        return SandboxSpecsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus'),
        available=data.get('available'),
        regions=data.get('regions', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxSpecsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxSpecsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxSpecsListOutputPagination:
        return SandboxSpecsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxSpecsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxSpecsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxSpecsListOutput:
        return SandboxSpecsListOutput(
        items=[mapSandboxSpecsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxSpecsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxSpecsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxSpecsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSandboxSpecsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxSpecsListQuery:
        return SandboxSpecsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SandboxSpecsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

