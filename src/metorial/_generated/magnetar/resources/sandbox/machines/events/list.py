from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesEventsListOutputItemsMachine:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class SandboxMachinesEventsListOutputItemsInstance:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class SandboxMachinesEventsListOutputItemsError:
    code: str
    message: str
@dataclass
class SandboxMachinesEventsListOutputItems:
    object: str
    id: str
    machine_id: str
    type: str
    source: str
    occurred_at: datetime
    machine_instance_id: Optional[str] = None
    generation: Optional[float] = None
    machine: Optional[SandboxMachinesEventsListOutputItemsMachine] = None
    instance: Optional[SandboxMachinesEventsListOutputItemsInstance] = None
    operation_id: Optional[str] = None
    guest_error_id: Optional[str] = None
    error: Optional[SandboxMachinesEventsListOutputItemsError] = None
@dataclass
class SandboxMachinesEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxMachinesEventsListOutput:
    items: List[SandboxMachinesEventsListOutputItems]
    pagination: SandboxMachinesEventsListOutputPagination


class mapSandboxMachinesEventsListOutputItemsMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListOutputItemsMachine:
        return SandboxMachinesEventsListOutputItemsMachine(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsListOutputItemsMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsListOutputItemsInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListOutputItemsInstance:
        return SandboxMachinesEventsListOutputItemsInstance(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsListOutputItemsInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListOutputItemsError:
        return SandboxMachinesEventsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListOutputItems:
        return SandboxMachinesEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        generation=data.get('generation'),
        type=data.get('type'),
        source=data.get('source'),
        machine=mapSandboxMachinesEventsListOutputItemsMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        instance=mapSandboxMachinesEventsListOutputItemsInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        operation_id=data.get('operation_id'),
        guest_error_id=data.get('guest_error_id'),
        error=mapSandboxMachinesEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListOutputPagination:
        return SandboxMachinesEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListOutput:
        return SandboxMachinesEventsListOutput(
        items=[mapSandboxMachinesEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxMachinesEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesEventsListQuery:
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


class mapSandboxMachinesEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsListQuery:
        return SandboxMachinesEventsListQuery(
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
    def to_dict(value: Union[SandboxMachinesEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

