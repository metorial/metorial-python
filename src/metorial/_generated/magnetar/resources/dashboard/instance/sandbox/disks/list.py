from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxDisksListOutputItemsMachine:
    id: str
    mount_path: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class DashboardInstanceSandboxDisksListOutputItemsActiveResize:
    id: str
    status: str
    target_size_bytes: float
@dataclass
class DashboardInstanceSandboxDisksListOutputItems:
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
    machine: Optional[DashboardInstanceSandboxDisksListOutputItemsMachine] = None
    active_resize: Optional[DashboardInstanceSandboxDisksListOutputItemsActiveResize] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSandboxDisksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxDisksListOutput:
    items: List[DashboardInstanceSandboxDisksListOutputItems]
    pagination: DashboardInstanceSandboxDisksListOutputPagination


class mapDashboardInstanceSandboxDisksListOutputItemsMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksListOutputItemsMachine:
        return DashboardInstanceSandboxDisksListOutputItemsMachine(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksListOutputItemsMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksListOutputItemsActiveResize:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksListOutputItemsActiveResize:
        return DashboardInstanceSandboxDisksListOutputItemsActiveResize(
        id=data.get('id'),
        status=data.get('status'),
        target_size_bytes=data.get('target_size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksListOutputItemsActiveResize, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksListOutputItems:
        return DashboardInstanceSandboxDisksListOutputItems(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        status=data.get('status'),
        region=data.get('region'),
        size_bytes=data.get('size_bytes'),
        machine=mapDashboardInstanceSandboxDisksListOutputItemsMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        active_resize=mapDashboardInstanceSandboxDisksListOutputItemsActiveResize.from_dict(data.get('active_resize')) if data.get('active_resize') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksListOutputPagination:
        return DashboardInstanceSandboxDisksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksListOutput:
        return DashboardInstanceSandboxDisksListOutput(
        items=[mapDashboardInstanceSandboxDisksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxDisksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxDisksListQuery:
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


class mapDashboardInstanceSandboxDisksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksListQuery:
        return DashboardInstanceSandboxDisksListQuery(
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
    def to_dict(value: Union[DashboardInstanceSandboxDisksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

