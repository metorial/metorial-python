from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxRegionsListOutputItemsArea:
    id: str
    name: str
@dataclass
class SandboxRegionsListOutputItems:
    object: str
    id: str
    name: str
    area: SandboxRegionsListOutputItemsArea
    is_default: bool
    availability: str
@dataclass
class SandboxRegionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxRegionsListOutput:
    items: List[SandboxRegionsListOutputItems]
    pagination: SandboxRegionsListOutputPagination


class mapSandboxRegionsListOutputItemsArea:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsListOutputItemsArea:
        return SandboxRegionsListOutputItemsArea(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsListOutputItemsArea, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxRegionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsListOutputItems:
        return SandboxRegionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        area=mapSandboxRegionsListOutputItemsArea.from_dict(data.get('area')) if data.get('area') else None,
        is_default=data.get('is_default'),
        availability=data.get('availability')
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxRegionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsListOutputPagination:
        return SandboxRegionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxRegionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsListOutput:
        return SandboxRegionsListOutput(
        items=[mapSandboxRegionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxRegionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxRegionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSandboxRegionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsListQuery:
        return SandboxRegionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

