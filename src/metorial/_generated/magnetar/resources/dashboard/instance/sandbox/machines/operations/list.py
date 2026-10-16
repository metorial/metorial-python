from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesOperationsListOutputItemsFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations:
    id: str
    kind: str
    machine_instance_id: str
@dataclass
class DashboardInstanceSandboxMachinesOperationsListOutputItems:
    object: str
    id: str
    machine_id: str
    kind: str
    trigger: str
    outcome: str
    instance_operations: List[DashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations]
    requested_at: datetime
    failure: Optional[DashboardInstanceSandboxMachinesOperationsListOutputItemsFailure] = None
    from_machine_instance_id: Optional[str] = None
    superseded_by_id: Optional[str] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSandboxMachinesOperationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxMachinesOperationsListOutput:
    items: List[DashboardInstanceSandboxMachinesOperationsListOutputItems]
    pagination: DashboardInstanceSandboxMachinesOperationsListOutputPagination


class mapDashboardInstanceSandboxMachinesOperationsListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsListOutputItemsFailure:
        return DashboardInstanceSandboxMachinesOperationsListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations:
        return DashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations(
        id=data.get('id'),
        kind=data.get('kind'),
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesOperationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsListOutputItems:
        return DashboardInstanceSandboxMachinesOperationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        outcome=data.get('outcome'),
        failure=mapDashboardInstanceSandboxMachinesOperationsListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        from_machine_instance_id=data.get('from_machine_instance_id'),
        superseded_by_id=data.get('superseded_by_id'),
        instance_operations=[mapDashboardInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations.from_dict(item) for item in data.get('instance_operations', []) if item],
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesOperationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsListOutputPagination:
        return DashboardInstanceSandboxMachinesOperationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesOperationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsListOutput:
        return DashboardInstanceSandboxMachinesOperationsListOutput(
        items=[mapDashboardInstanceSandboxMachinesOperationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxMachinesOperationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesOperationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    machine_instance_id: Optional[Union[str, List[str]]] = None
    kind: Optional[Union[str, List[str]]] = None
    trigger: Optional[Union[str, List[str]]] = None
    outcome: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSandboxMachinesOperationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsListQuery:
        return DashboardInstanceSandboxMachinesOperationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        machine_instance_id=data.get('machine_instance_id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        outcome=data.get('outcome')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

