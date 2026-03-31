from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmReposListOutputItemsProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ScmReposListOutputItems:
    object: str
    id: str
    provider: ScmReposListOutputItemsProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ScmReposListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ScmReposListOutput:
    items: List[ScmReposListOutputItems]
    pagination: ScmReposListOutputPagination


class mapScmReposListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposListOutputItemsProvider:
        return ScmReposListOutputItemsProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposListOutputItems:
        return ScmReposListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapScmReposListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmReposListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposListOutputPagination:
        return ScmReposListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposListOutput:
        return ScmReposListOutput(
        items=[mapScmReposListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapScmReposListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmReposListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmReposListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ScmReposListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ScmReposListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ScmReposListQueryCreatedAt] = None
    updated_at: Optional[ScmReposListQueryUpdatedAt] = None


class mapScmReposListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposListQuery:
        return ScmReposListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        created_at=mapScmReposListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapScmReposListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmReposListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

