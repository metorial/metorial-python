from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesEventsListOutputItemsMachine:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesEventsListOutputItemsInstance:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesEventsListOutputItemsError:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesEventsListOutputItems:
    object: str
    id: str
    machine_id: str
    type: str
    source: str
    occurred_at: datetime
    machine_instance_id: Optional[str] = None
    generation: Optional[float] = None
    machine: Optional[ManagementInstanceSandboxMachinesEventsListOutputItemsMachine] = None
    instance: Optional[ManagementInstanceSandboxMachinesEventsListOutputItemsInstance] = None
    operation_id: Optional[str] = None
    guest_error_id: Optional[str] = None
    error: Optional[ManagementInstanceSandboxMachinesEventsListOutputItemsError] = None
@dataclass
class ManagementInstanceSandboxMachinesEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSandboxMachinesEventsListOutput:
    items: List[ManagementInstanceSandboxMachinesEventsListOutputItems]
    pagination: ManagementInstanceSandboxMachinesEventsListOutputPagination


class mapManagementInstanceSandboxMachinesEventsListOutputItemsMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListOutputItemsMachine:
        return ManagementInstanceSandboxMachinesEventsListOutputItemsMachine(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListOutputItemsMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsListOutputItemsInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListOutputItemsInstance:
        return ManagementInstanceSandboxMachinesEventsListOutputItemsInstance(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListOutputItemsInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListOutputItemsError:
        return ManagementInstanceSandboxMachinesEventsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListOutputItems:
        return ManagementInstanceSandboxMachinesEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        generation=data.get('generation'),
        type=data.get('type'),
        source=data.get('source'),
        machine=mapManagementInstanceSandboxMachinesEventsListOutputItemsMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        instance=mapManagementInstanceSandboxMachinesEventsListOutputItemsInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        operation_id=data.get('operation_id'),
        guest_error_id=data.get('guest_error_id'),
        error=mapManagementInstanceSandboxMachinesEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListOutputPagination:
        return ManagementInstanceSandboxMachinesEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListOutput:
        return ManagementInstanceSandboxMachinesEventsListOutput(
        items=[mapManagementInstanceSandboxMachinesEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSandboxMachinesEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    scope: Optional[str] = None
    machine_instance_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    source: Optional[Union[str, List[str]]] = None
    reverse: Optional[bool] = None


class mapManagementInstanceSandboxMachinesEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsListQuery:
        return ManagementInstanceSandboxMachinesEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        scope=data.get('scope'),
        machine_instance_id=data.get('machine_instance_id'),
        type=data.get('type'),
        source=data.get('source'),
        reverse=data.get('reverse')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

