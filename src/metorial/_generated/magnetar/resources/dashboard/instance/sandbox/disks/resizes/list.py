from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxDisksResizesListOutputItemsFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxDisksResizesListOutputItems:
    object: str
    id: str
    disk_id: str
    status: str
    original_size_bytes: float
    target_size_bytes: float
    machine_ids: List[str]
    created_at: datetime
    updated_at: datetime
    failure: Optional[DashboardInstanceSandboxDisksResizesListOutputItemsFailure] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSandboxDisksResizesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxDisksResizesListOutput:
    items: List[DashboardInstanceSandboxDisksResizesListOutputItems]
    pagination: DashboardInstanceSandboxDisksResizesListOutputPagination


class mapDashboardInstanceSandboxDisksResizesListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesListOutputItemsFailure:
        return DashboardInstanceSandboxDisksResizesListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksResizesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesListOutputItems:
        return DashboardInstanceSandboxDisksResizesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        disk_id=data.get('disk_id'),
        status=data.get('status'),
        original_size_bytes=data.get('original_size_bytes'),
        target_size_bytes=data.get('target_size_bytes'),
        machine_ids=data.get('machine_ids', []),
        failure=mapDashboardInstanceSandboxDisksResizesListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksResizesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesListOutputPagination:
        return DashboardInstanceSandboxDisksResizesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksResizesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesListOutput:
        return DashboardInstanceSandboxDisksResizesListOutput(
        items=[mapDashboardInstanceSandboxDisksResizesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxDisksResizesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxDisksResizesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSandboxDisksResizesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesListQuery:
        return DashboardInstanceSandboxDisksResizesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

