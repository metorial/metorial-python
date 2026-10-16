from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesEventsListOutputItemsMachine:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesEventsListOutputItemsInstance:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesEventsListOutputItemsError:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesEventsListOutputItems:
    object: str
    id: str
    machine_id: str
    type: str
    source: str
    occurred_at: datetime
    machine_instance_id: Optional[str] = None
    generation: Optional[float] = None
    machine: Optional[DashboardInstanceSandboxMachinesEventsListOutputItemsMachine] = None
    instance: Optional[DashboardInstanceSandboxMachinesEventsListOutputItemsInstance] = None
    operation_id: Optional[str] = None
    guest_error_id: Optional[str] = None
    error: Optional[DashboardInstanceSandboxMachinesEventsListOutputItemsError] = None
@dataclass
class DashboardInstanceSandboxMachinesEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxMachinesEventsListOutput:
    items: List[DashboardInstanceSandboxMachinesEventsListOutputItems]
    pagination: DashboardInstanceSandboxMachinesEventsListOutputPagination


class mapDashboardInstanceSandboxMachinesEventsListOutputItemsMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListOutputItemsMachine:
        return DashboardInstanceSandboxMachinesEventsListOutputItemsMachine(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListOutputItemsMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsListOutputItemsInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListOutputItemsInstance:
        return DashboardInstanceSandboxMachinesEventsListOutputItemsInstance(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListOutputItemsInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListOutputItemsError:
        return DashboardInstanceSandboxMachinesEventsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListOutputItems:
        return DashboardInstanceSandboxMachinesEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        generation=data.get('generation'),
        type=data.get('type'),
        source=data.get('source'),
        machine=mapDashboardInstanceSandboxMachinesEventsListOutputItemsMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        instance=mapDashboardInstanceSandboxMachinesEventsListOutputItemsInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        operation_id=data.get('operation_id'),
        guest_error_id=data.get('guest_error_id'),
        error=mapDashboardInstanceSandboxMachinesEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListOutputPagination:
        return DashboardInstanceSandboxMachinesEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListOutput:
        return DashboardInstanceSandboxMachinesEventsListOutput(
        items=[mapDashboardInstanceSandboxMachinesEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxMachinesEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesEventsListQuery:
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


class mapDashboardInstanceSandboxMachinesEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsListQuery:
        return DashboardInstanceSandboxMachinesEventsListQuery(
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
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

