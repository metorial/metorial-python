from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSecretsListOutputItemsType:
    identifier: str
    name: str
@dataclass
class ManagementInstanceSecretsListOutputItems:
    object: str
    id: str
    status: str
    type: ManagementInstanceSecretsListOutputItemsType
    description: str
    metadata: Dict[str, Any]
    organization_id: str
    instance_id: str
    fingerprint: str
    created_at: datetime
    last_used_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSecretsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSecretsListOutput:
    items: List[ManagementInstanceSecretsListOutputItems]
    pagination: ManagementInstanceSecretsListOutputPagination


class mapManagementInstanceSecretsListOutputItemsType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSecretsListOutputItemsType:
        return ManagementInstanceSecretsListOutputItemsType(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSecretsListOutputItemsType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSecretsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSecretsListOutputItems:
        return ManagementInstanceSecretsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=mapManagementInstanceSecretsListOutputItemsType.from_dict(data.get('type')) if data.get('type') else None,
        description=data.get('description'),
        metadata=data.get('metadata'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        fingerprint=data.get('fingerprint'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSecretsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSecretsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSecretsListOutputPagination:
        return ManagementInstanceSecretsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSecretsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSecretsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSecretsListOutput:
        return ManagementInstanceSecretsListOutput(
        items=[mapManagementInstanceSecretsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSecretsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSecretsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSecretsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSecretsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSecretsListQuery:
        return ManagementInstanceSecretsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSecretsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

