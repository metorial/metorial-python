from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumersProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceConsumersProfilesListOutput:
    items: List[Dict[str, Any]]
    pagination: ManagementInstanceConsumersProfilesListOutputPagination


class mapManagementInstanceConsumersProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutputPagination:
        return ManagementInstanceConsumersProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutput:
        return ManagementInstanceConsumersProfilesListOutput(
        items=data.get('items', []),
        pagination=mapManagementInstanceConsumersProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConsumersProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceConsumersProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListQuery:
        return ManagementInstanceConsumersProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

