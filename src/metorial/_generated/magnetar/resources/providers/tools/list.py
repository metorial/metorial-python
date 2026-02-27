from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersToolsListOutputItems:
    object: str
    id: str
    name: str
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
    output_schema: Optional[Dict[str, Any]] = None
@dataclass
class ProvidersToolsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersToolsListOutput:
    items: List[ProvidersToolsListOutputItems]
    pagination: ProvidersToolsListOutputPagination


class mapProvidersToolsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsListOutputItems:
        return ProvidersToolsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        title=data.get('title'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        output_schema=data.get('output_schema'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersToolsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsListOutputPagination:
        return ProvidersToolsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersToolsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsListOutput:
        return ProvidersToolsListOutput(
        items=[mapProvidersToolsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersToolsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersToolsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_version_id: Optional[str] = None


class mapProvidersToolsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsListQuery:
        return ProvidersToolsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
