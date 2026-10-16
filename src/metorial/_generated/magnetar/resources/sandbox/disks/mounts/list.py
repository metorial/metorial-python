from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxDisksMountsListOutputItemsFailure:
    code: str
    message: str
@dataclass
class SandboxDisksMountsListOutputItems:
    object: str
    id: str
    disk_id: str
    mount_path: str
    status: str
    created_at: datetime
    machine_id: Optional[str] = None
    machine_instance_id: Optional[str] = None
    failure: Optional[SandboxDisksMountsListOutputItemsFailure] = None
    mounted_at: Optional[datetime] = None
    released_at: Optional[datetime] = None
@dataclass
class SandboxDisksMountsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxDisksMountsListOutput:
    items: List[SandboxDisksMountsListOutputItems]
    pagination: SandboxDisksMountsListOutputPagination


class mapSandboxDisksMountsListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksMountsListOutputItemsFailure:
        return SandboxDisksMountsListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksMountsListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxDisksMountsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksMountsListOutputItems:
        return SandboxDisksMountsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        disk_id=data.get('disk_id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status'),
        failure=mapSandboxDisksMountsListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        mounted_at=datetime.fromisoformat(data.get('mounted_at').replace('Z', '+00:00')) if data.get('mounted_at') else None,
        released_at=datetime.fromisoformat(data.get('released_at').replace('Z', '+00:00')) if data.get('released_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksMountsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxDisksMountsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksMountsListOutputPagination:
        return SandboxDisksMountsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksMountsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxDisksMountsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksMountsListOutput:
        return SandboxDisksMountsListOutput(
        items=[mapSandboxDisksMountsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxDisksMountsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksMountsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxDisksMountsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSandboxDisksMountsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksMountsListQuery:
        return SandboxDisksMountsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksMountsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

