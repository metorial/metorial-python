from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsConsumerProfilesListOutput:
    items: List[Dict[str, Any]]
    pagination: PortalsConsumerProfilesListOutputPagination


class mapPortalsConsumerProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesListOutputPagination:
        return PortalsConsumerProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesListOutput:
        return PortalsConsumerProfilesListOutput(
        items=data.get('items', []),
        pagination=mapPortalsConsumerProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsConsumerProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    consumer_group_id: Optional[str] = None


class mapPortalsConsumerProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesListQuery:
        return PortalsConsumerProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        consumer_group_id=data.get('consumer_group_id')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

