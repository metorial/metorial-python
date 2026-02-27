from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderCategoriesListOutputItems:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceProviderCategoriesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderCategoriesListOutput:
    items: List[DashboardInstanceProviderCategoriesListOutputItems]
    pagination: DashboardInstanceProviderCategoriesListOutputPagination


class mapDashboardInstanceProviderCategoriesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderCategoriesListOutputItems:
        return DashboardInstanceProviderCategoriesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderCategoriesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderCategoriesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderCategoriesListOutputPagination:
        return DashboardInstanceProviderCategoriesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderCategoriesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderCategoriesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderCategoriesListOutput:
        return DashboardInstanceProviderCategoriesListOutput(
        items=[mapDashboardInstanceProviderCategoriesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderCategoriesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderCategoriesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderCategoriesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_listing_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceProviderCategoriesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderCategoriesListQuery:
        return DashboardInstanceProviderCategoriesListQuery(
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
    def to_dict(value: Union[DashboardInstanceProviderCategoriesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
