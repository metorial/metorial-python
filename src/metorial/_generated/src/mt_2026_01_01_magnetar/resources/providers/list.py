from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersListOutputItemsPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProvidersListOutputItemsCurrentVersion:
    object: str
    id: str
    version: str
    provider_id: str
    is_current: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    specification_id: Optional[str] = None
@dataclass
class ProvidersListOutputItemsOauthAutoRegistration:
    status: str
@dataclass
class ProvidersListOutputItemsOauth:
    status: str
    auto_registration: ProvidersListOutputItemsOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ProvidersListOutputItems:
    object: str
    id: str
    access: str
    status: str
    publisher: ProvidersListOutputItemsPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[ProvidersListOutputItemsCurrentVersion] = None
    oauth: Optional[ProvidersListOutputItemsOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersListOutput:
    items: List[ProvidersListOutputItems]
    pagination: ProvidersListOutputPagination


class mapProvidersListOutputItemsPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputItemsPublisher:
        return ProvidersListOutputItemsPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputItemsPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutputItemsCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputItemsCurrentVersion:
        return ProvidersListOutputItemsCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputItemsCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutputItemsOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputItemsOauthAutoRegistration:
        return ProvidersListOutputItemsOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputItemsOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutputItemsOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputItemsOauth:
        return ProvidersListOutputItemsOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapProvidersListOutputItemsOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputItemsOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputItems:
        return ProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapProvidersListOutputItemsPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapProvidersListOutputItemsCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapProvidersListOutputItemsOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputPagination:
        return ProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutput:
        return ProvidersListOutput(
        items=[mapProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None


class mapProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListQuery:
        return ProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

