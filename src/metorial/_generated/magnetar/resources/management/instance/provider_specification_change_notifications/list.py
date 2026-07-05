from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutputItems:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification] = None
    to_specification: Optional[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification] = None
    from_provider_version: Optional[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion] = None
    to_provider_version: Optional[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion] = None
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListOutput:
    items: List[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItems]
    pagination: ManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination


class mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutputItems:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItemsToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderSpecificationChangeNotificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListOutput:
        return ManagementInstanceProviderSpecificationChangeNotificationsListOutput(
        items=[mapManagementInstanceProviderSpecificationChangeNotificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderSpecificationChangeNotificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceProviderSpecificationChangeNotificationsListQuery:
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
    created_at: Optional[ManagementInstanceProviderSpecificationChangeNotificationsListQueryCreatedAt] = None


class mapManagementInstanceProviderSpecificationChangeNotificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderSpecificationChangeNotificationsListQuery:
        return ManagementInstanceProviderSpecificationChangeNotificationsListQuery(
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
        created_at=mapManagementInstanceProviderSpecificationChangeNotificationsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderSpecificationChangeNotificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

