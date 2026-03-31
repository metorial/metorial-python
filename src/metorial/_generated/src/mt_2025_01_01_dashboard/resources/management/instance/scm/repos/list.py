from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmReposListOutputItemsProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceScmReposListOutputItems:
    object: str
    id: str
    provider: ManagementInstanceScmReposListOutputItemsProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceScmReposListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceScmReposListOutput:
    items: List[ManagementInstanceScmReposListOutputItems]
    pagination: ManagementInstanceScmReposListOutputPagination


class mapManagementInstanceScmReposListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposListOutputItemsProvider:
        return ManagementInstanceScmReposListOutputItemsProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposListOutputItems:
        return ManagementInstanceScmReposListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceScmReposListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposListOutputPagination:
        return ManagementInstanceScmReposListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposListOutput:
        return ManagementInstanceScmReposListOutput(
        items=[mapManagementInstanceScmReposListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceScmReposListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmReposListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceScmReposListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceScmReposListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceScmReposListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceScmReposListQueryUpdatedAt] = None


class mapManagementInstanceScmReposListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposListQuery:
        return ManagementInstanceScmReposListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        created_at=mapManagementInstanceScmReposListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceScmReposListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

