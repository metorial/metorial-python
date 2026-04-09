from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumersListOutput:
    items: List[Dict[str, Any]]
    pagination: ConsumersListOutputPagination


class mapConsumersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersListOutputPagination:
        return ConsumersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersListOutput:
        return ConsumersListOutput(
        items=data.get('items', []),
        pagination=mapConsumersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    id: Optional[str] = None


class mapConsumersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersListQuery:
        return ConsumersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

