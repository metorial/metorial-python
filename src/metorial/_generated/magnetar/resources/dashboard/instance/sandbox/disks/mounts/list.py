from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxDisksMountsListOutputItemsFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxDisksMountsListOutputItems:
    object: str
    id: str
    disk_id: str
    mount_path: str
    status: str
    created_at: datetime
    machine_id: Optional[str] = None
    machine_instance_id: Optional[str] = None
    failure: Optional[DashboardInstanceSandboxDisksMountsListOutputItemsFailure] = None
    mounted_at: Optional[datetime] = None
    released_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSandboxDisksMountsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxDisksMountsListOutput:
    items: List[DashboardInstanceSandboxDisksMountsListOutputItems]
    pagination: DashboardInstanceSandboxDisksMountsListOutputPagination


class mapDashboardInstanceSandboxDisksMountsListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksMountsListOutputItemsFailure:
        return DashboardInstanceSandboxDisksMountsListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksMountsListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksMountsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksMountsListOutputItems:
        return DashboardInstanceSandboxDisksMountsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        disk_id=data.get('disk_id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status'),
        failure=mapDashboardInstanceSandboxDisksMountsListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        mounted_at=datetime.fromisoformat(data.get('mounted_at').replace('Z', '+00:00')) if data.get('mounted_at') else None,
        released_at=datetime.fromisoformat(data.get('released_at').replace('Z', '+00:00')) if data.get('released_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksMountsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksMountsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksMountsListOutputPagination:
        return DashboardInstanceSandboxDisksMountsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksMountsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksMountsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksMountsListOutput:
        return DashboardInstanceSandboxDisksMountsListOutput(
        items=[mapDashboardInstanceSandboxDisksMountsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxDisksMountsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksMountsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxDisksMountsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceSandboxDisksMountsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksMountsListQuery:
        return DashboardInstanceSandboxDisksMountsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksMountsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

