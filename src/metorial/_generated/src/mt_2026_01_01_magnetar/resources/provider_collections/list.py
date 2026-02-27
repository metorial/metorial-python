from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderCollectionsListOutputItems:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderCollectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderCollectionsListOutput:
    items: List[ProviderCollectionsListOutputItems]
    pagination: ProviderCollectionsListOutputPagination


class mapProviderCollectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderCollectionsListOutputItems:
        return ProviderCollectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderCollectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderCollectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderCollectionsListOutputPagination:
        return ProviderCollectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderCollectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderCollectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderCollectionsListOutput:
        return ProviderCollectionsListOutput(
        items=[mapProviderCollectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderCollectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderCollectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderCollectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_listing_id: Optional[Union[str, List[str]]] = None


class mapProviderCollectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderCollectionsListQuery:
        return ProviderCollectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_listing_id=data.get('provider_listing_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderCollectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
