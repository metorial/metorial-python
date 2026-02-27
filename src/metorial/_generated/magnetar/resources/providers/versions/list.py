from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersVersionsListOutputItems:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProvidersVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersVersionsListOutput:
    items: List[ProvidersVersionsListOutputItems]
    pagination: ProvidersVersionsListOutputPagination


class mapProvidersVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersVersionsListOutputItems:
        return ProvidersVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersVersionsListOutputPagination:
        return ProvidersVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersVersionsListOutput:
        return ProvidersVersionsListOutput(
        items=[mapProvidersVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProvidersVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersVersionsListQuery:
        return ProvidersVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
