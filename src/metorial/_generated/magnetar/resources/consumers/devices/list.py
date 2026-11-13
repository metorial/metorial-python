from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersDevicesListOutputItemsClients:
    object: str
    key: str
    name: str
    detected: bool
    installable: bool
    supports_skills: bool
    enabled: bool
    excluded_magic_mcp_server_ids: List[str]
    excluded_skill_ids: List[str]
@dataclass
class ConsumersDevicesListOutputItems:
    object: str
    id: str
    status: str
    consumer_profile_id: str
    name: str
    os: str
    arch: str
    app_version: str
    clients: List[ConsumersDevicesListOutputItemsClients]
    last_seen_at: datetime
    created_at: datetime
    updated_at: datetime
    revoked_at: Optional[datetime] = None
@dataclass
class ConsumersDevicesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumersDevicesListOutput:
    items: List[ConsumersDevicesListOutputItems]
    pagination: ConsumersDevicesListOutputPagination


class mapConsumersDevicesListOutputItemsClients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesListOutputItemsClients:
        return ConsumersDevicesListOutputItemsClients(
        object=data.get('object'),
        key=data.get('key'),
        name=data.get('name'),
        detected=data.get('detected'),
        installable=data.get('installable'),
        supports_skills=data.get('supports_skills'),
        enabled=data.get('enabled'),
        excluded_magic_mcp_server_ids=data.get('excluded_magic_mcp_server_ids', []),
        excluded_skill_ids=data.get('excluded_skill_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesListOutputItemsClients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersDevicesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesListOutputItems:
        return ConsumersDevicesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        consumer_profile_id=data.get('consumer_profile_id'),
        name=data.get('name'),
        os=data.get('os'),
        arch=data.get('arch'),
        app_version=data.get('app_version'),
        clients=[mapConsumersDevicesListOutputItemsClients.from_dict(item) for item in data.get('clients', []) if item],
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersDevicesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesListOutputPagination:
        return ConsumersDevicesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersDevicesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesListOutput:
        return ConsumersDevicesListOutput(
        items=[mapConsumersDevicesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumersDevicesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumersDevicesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    consumer_profile_id: Optional[Union[str, List[str]]] = None
    consumer_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapConsumersDevicesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesListQuery:
        return ConsumersDevicesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        consumer_profile_id=data.get('consumer_profile_id'),
        consumer_id=data.get('consumer_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

