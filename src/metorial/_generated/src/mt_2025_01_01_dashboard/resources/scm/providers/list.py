from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmProvidersListOutputItems:
    object: str
    id: str
    type: str
    name: str
    is_default: bool
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    api_url: Optional[str] = None
    web_url: Optional[str] = None
@dataclass
class ScmProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ScmProvidersListOutput:
    items: List[ScmProvidersListOutputItems]
    pagination: ScmProvidersListOutputPagination


class mapScmProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersListOutputItems:
        return ScmProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        api_url=data.get('api_url'),
        web_url=data.get('web_url'),
        is_default=data.get('is_default'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersListOutputPagination:
        return ScmProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersListOutput:
        return ScmProvidersListOutput(
        items=[mapScmProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapScmProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapScmProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersListQuery:
        return ScmProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

