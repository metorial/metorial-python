from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderSpecificationChangeNotificationsListOutputItemsFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsListOutputItemsToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsListOutputItems:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[ProviderSpecificationChangeNotificationsListOutputItemsFromSpecification] = None
    to_specification: Optional[ProviderSpecificationChangeNotificationsListOutputItemsToSpecification] = None
    from_provider_version: Optional[ProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion] = None
    to_provider_version: Optional[ProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion] = None
@dataclass
class ProviderSpecificationChangeNotificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderSpecificationChangeNotificationsListOutput:
    items: List[ProviderSpecificationChangeNotificationsListOutputItems]
    pagination: ProviderSpecificationChangeNotificationsListOutputPagination


class mapProviderSpecificationChangeNotificationsListOutputItemsFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutputItemsFromSpecification:
        return ProviderSpecificationChangeNotificationsListOutputItemsFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutputItemsFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsListOutputItemsToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutputItemsToSpecification:
        return ProviderSpecificationChangeNotificationsListOutputItemsToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutputItemsToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion:
        return ProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion:
        return ProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutputItems:
        return ProviderSpecificationChangeNotificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapProviderSpecificationChangeNotificationsListOutputItemsFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapProviderSpecificationChangeNotificationsListOutputItemsToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutputPagination:
        return ProviderSpecificationChangeNotificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListOutput:
        return ProviderSpecificationChangeNotificationsListOutput(
        items=[mapProviderSpecificationChangeNotificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderSpecificationChangeNotificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderSpecificationChangeNotificationsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderSpecificationChangeNotificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    target: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_version_id: Optional[Union[str, List[str]]] = None
    provider_specification_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ProviderSpecificationChangeNotificationsListQueryCreatedAt] = None


class mapProviderSpecificationChangeNotificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsListQuery:
        return ProviderSpecificationChangeNotificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        target=data.get('target'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=mapProviderSpecificationChangeNotificationsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

