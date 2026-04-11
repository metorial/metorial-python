from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerProvidersListOutput:
    items: List[Dict[str, Any]]
    pagination: ConsumerProvidersListOutputPagination


class mapConsumerProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersListOutputPagination:
        return ConsumerProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersListOutput:
        return ConsumerProvidersListOutput(
        items=data.get('items', []),
        pagination=mapConsumerProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    provider_group_id: Optional[str] = None


class mapConsumerProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersListQuery:
        return ConsumerProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        provider_group_id=data.get('provider_group_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

