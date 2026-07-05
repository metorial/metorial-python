from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderTemplatesListOutputItems:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    integration_id: Optional[str] = None
@dataclass
class ProviderTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderTemplatesListOutput:
    items: List[ProviderTemplatesListOutputItems]
    pagination: ProviderTemplatesListOutputPagination


class mapProviderTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderTemplatesListOutputItems:
        return ProviderTemplatesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderTemplatesListOutputPagination:
        return ProviderTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderTemplatesListOutput:
        return ProviderTemplatesListOutput(
        items=[mapProviderTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderTemplatesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapProviderTemplatesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderTemplatesListQuery:
        return ProviderTemplatesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        search=data.get('search'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ProviderTemplatesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

