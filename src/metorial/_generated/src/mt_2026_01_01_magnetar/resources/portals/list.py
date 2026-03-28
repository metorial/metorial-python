from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class PortalsListOutputItemsUrls:
    type: str
    url: str
@dataclass
class PortalsListOutputItemsBrand:
    image: str
    name: str
@dataclass
class PortalsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: PortalsListOutputItemsAuth
    urls: List[PortalsListOutputItemsUrls]
    brand: PortalsListOutputItemsBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsListOutput:
    items: List[PortalsListOutputItems]
    pagination: PortalsListOutputPagination


class mapPortalsListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsAuth:
        return PortalsListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItemsUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsUrls:
        return PortalsListOutputItemsUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItemsBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItemsBrand:
        return PortalsListOutputItemsBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItemsBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputItems:
        return PortalsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapPortalsListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsListOutputItemsUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapPortalsListOutputItemsBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutputPagination:
        return PortalsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListOutput:
        return PortalsListOutput(
        items=[mapPortalsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapPortalsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapPortalsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListQuery:
        return PortalsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

