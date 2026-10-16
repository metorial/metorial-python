from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxRegionsListOutputItemsArea:
    id: str
    name: str
@dataclass
class DashboardInstanceSandboxRegionsListOutputItems:
    object: str
    id: str
    name: str
    area: DashboardInstanceSandboxRegionsListOutputItemsArea
    is_default: bool
    availability: str
@dataclass
class DashboardInstanceSandboxRegionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxRegionsListOutput:
    items: List[DashboardInstanceSandboxRegionsListOutputItems]
    pagination: DashboardInstanceSandboxRegionsListOutputPagination


class mapDashboardInstanceSandboxRegionsListOutputItemsArea:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsListOutputItemsArea:
        return DashboardInstanceSandboxRegionsListOutputItemsArea(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsListOutputItemsArea, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxRegionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsListOutputItems:
        return DashboardInstanceSandboxRegionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        area=mapDashboardInstanceSandboxRegionsListOutputItemsArea.from_dict(data.get('area')) if data.get('area') else None,
        is_default=data.get('is_default'),
        availability=data.get('availability')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxRegionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsListOutputPagination:
        return DashboardInstanceSandboxRegionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxRegionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsListOutput:
        return DashboardInstanceSandboxRegionsListOutput(
        items=[mapDashboardInstanceSandboxRegionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxRegionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxRegionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceSandboxRegionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsListQuery:
        return DashboardInstanceSandboxRegionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

