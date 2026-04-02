from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConsumersProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceConsumersProfilesListOutput:
    items: List[Dict[str, Any]]
    pagination: DashboardInstanceConsumersProfilesListOutputPagination


class mapDashboardInstanceConsumersProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutputPagination:
        return DashboardInstanceConsumersProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumersProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutput:
        return DashboardInstanceConsumersProfilesListOutput(
        items=data.get('items', []),
        pagination=mapDashboardInstanceConsumersProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceConsumersProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceConsumersProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListQuery:
        return DashboardInstanceConsumersProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

