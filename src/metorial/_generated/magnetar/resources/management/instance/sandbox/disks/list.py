from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxDisksListOutputItemsMachine:
    id: str
    mount_path: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class ManagementInstanceSandboxDisksListOutputItemsActiveResize:
    id: str
    status: str
    target_size_bytes: float
@dataclass
class ManagementInstanceSandboxDisksListOutputItems:
    object: str
    metadata: Dict[str, Any]
    id: str
    type: str
    status: str
    region: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    size_bytes: Optional[float] = None
    machine: Optional[ManagementInstanceSandboxDisksListOutputItemsMachine] = None
    active_resize: Optional[ManagementInstanceSandboxDisksListOutputItemsActiveResize] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSandboxDisksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSandboxDisksListOutput:
    items: List[ManagementInstanceSandboxDisksListOutputItems]
    pagination: ManagementInstanceSandboxDisksListOutputPagination


class mapManagementInstanceSandboxDisksListOutputItemsMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksListOutputItemsMachine:
        return ManagementInstanceSandboxDisksListOutputItemsMachine(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksListOutputItemsMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksListOutputItemsActiveResize:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksListOutputItemsActiveResize:
        return ManagementInstanceSandboxDisksListOutputItemsActiveResize(
        id=data.get('id'),
        status=data.get('status'),
        target_size_bytes=data.get('target_size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksListOutputItemsActiveResize, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksListOutputItems:
        return ManagementInstanceSandboxDisksListOutputItems(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        status=data.get('status'),
        region=data.get('region'),
        size_bytes=data.get('size_bytes'),
        machine=mapManagementInstanceSandboxDisksListOutputItemsMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        active_resize=mapManagementInstanceSandboxDisksListOutputItemsActiveResize.from_dict(data.get('active_resize')) if data.get('active_resize') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksListOutputPagination:
        return ManagementInstanceSandboxDisksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksListOutput:
        return ManagementInstanceSandboxDisksListOutput(
        items=[mapManagementInstanceSandboxDisksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSandboxDisksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxDisksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    machine_id: Optional[Union[str, List[str]]] = None
    region: Optional[Union[str, List[str]]] = None
    attached: Optional[bool] = None
    search: Optional[str] = None


class mapManagementInstanceSandboxDisksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksListQuery:
        return ManagementInstanceSandboxDisksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        type=data.get('type'),
        machine_id=data.get('machine_id'),
        region=data.get('region'),
        attached=data.get('attached'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

