from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersGroupsListOutputItems:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ConsumerProvidersGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerProvidersGroupsListOutput:
    items: List[ConsumerProvidersGroupsListOutputItems]
    pagination: ConsumerProvidersGroupsListOutputPagination


class mapConsumerProvidersGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGroupsListOutputItems:
        return ConsumerProvidersGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGroupsListOutputPagination:
        return ConsumerProvidersGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGroupsListOutput:
        return ConsumerProvidersGroupsListOutput(
        items=[mapConsumerProvidersGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerProvidersGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerProvidersGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapConsumerProvidersGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGroupsListQuery:
        return ConsumerProvidersGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

