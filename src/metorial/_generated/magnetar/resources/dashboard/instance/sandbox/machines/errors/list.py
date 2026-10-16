from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesErrorsListOutputItems:
    object: str
    id: str
    machine_id: str
    machine_instance_id: str
    operation_id: str
    kind: str
    stage: str
    reason: str
    code: str
    message: str
    occurred_at: datetime
    event_id: Optional[str] = None
    exit_code: Optional[float] = None
    duration_ms: Optional[float] = None
    stdout: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesErrorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxMachinesErrorsListOutput:
    items: List[DashboardInstanceSandboxMachinesErrorsListOutputItems]
    pagination: DashboardInstanceSandboxMachinesErrorsListOutputPagination


class mapDashboardInstanceSandboxMachinesErrorsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesErrorsListOutputItems:
        return DashboardInstanceSandboxMachinesErrorsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        operation_id=data.get('operation_id'),
        event_id=data.get('event_id'),
        kind=data.get('kind'),
        stage=data.get('stage'),
        reason=data.get('reason'),
        code=data.get('code'),
        message=data.get('message'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms'),
        stdout=data.get('stdout'),
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesErrorsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesErrorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesErrorsListOutputPagination:
        return DashboardInstanceSandboxMachinesErrorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesErrorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesErrorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesErrorsListOutput:
        return DashboardInstanceSandboxMachinesErrorsListOutput(
        items=[mapDashboardInstanceSandboxMachinesErrorsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxMachinesErrorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesErrorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesErrorsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    machine_instance_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSandboxMachinesErrorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesErrorsListQuery:
        return DashboardInstanceSandboxMachinesErrorsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesErrorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

