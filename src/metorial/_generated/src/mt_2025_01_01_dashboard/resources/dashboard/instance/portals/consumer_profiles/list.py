from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsConsumerProfilesListOutput:
    items: List[Dict[str, Any]]
    pagination: DashboardInstancePortalsConsumerProfilesListOutputPagination


class mapDashboardInstancePortalsConsumerProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutputPagination:
        return DashboardInstancePortalsConsumerProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutput:
        return DashboardInstancePortalsConsumerProfilesListOutput(
        items=data.get('items', []),
        pagination=mapDashboardInstancePortalsConsumerProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    id: Optional[str] = None
    consumer_group_id: Optional[str] = None


class mapDashboardInstancePortalsConsumerProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListQuery:
        return DashboardInstancePortalsConsumerProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        id=data.get('id'),
        consumer_group_id=data.get('consumer_group_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

