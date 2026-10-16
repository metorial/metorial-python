from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesOperationsListOutputItemsFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations:
    id: str
    kind: str
    machine_instance_id: str
@dataclass
class ManagementInstanceSandboxMachinesOperationsListOutputItems:
    object: str
    id: str
    machine_id: str
    kind: str
    trigger: str
    outcome: str
    instance_operations: List[ManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations]
    requested_at: datetime
    failure: Optional[ManagementInstanceSandboxMachinesOperationsListOutputItemsFailure] = None
    from_machine_instance_id: Optional[str] = None
    superseded_by_id: Optional[str] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSandboxMachinesOperationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSandboxMachinesOperationsListOutput:
    items: List[ManagementInstanceSandboxMachinesOperationsListOutputItems]
    pagination: ManagementInstanceSandboxMachinesOperationsListOutputPagination


class mapManagementInstanceSandboxMachinesOperationsListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesOperationsListOutputItemsFailure:
        return ManagementInstanceSandboxMachinesOperationsListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesOperationsListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations:
        return ManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations(
        id=data.get('id'),
        kind=data.get('kind'),
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesOperationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesOperationsListOutputItems:
        return ManagementInstanceSandboxMachinesOperationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        outcome=data.get('outcome'),
        failure=mapManagementInstanceSandboxMachinesOperationsListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        from_machine_instance_id=data.get('from_machine_instance_id'),
        superseded_by_id=data.get('superseded_by_id'),
        instance_operations=[mapManagementInstanceSandboxMachinesOperationsListOutputItemsInstanceOperations.from_dict(item) for item in data.get('instance_operations', []) if item],
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesOperationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesOperationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesOperationsListOutputPagination:
        return ManagementInstanceSandboxMachinesOperationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesOperationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesOperationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesOperationsListOutput:
        return ManagementInstanceSandboxMachinesOperationsListOutput(
        items=[mapManagementInstanceSandboxMachinesOperationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSandboxMachinesOperationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesOperationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesOperationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    machine_instance_id: Optional[Union[str, List[str]]] = None
    kind: Optional[Union[str, List[str]]] = None
    trigger: Optional[Union[str, List[str]]] = None
    outcome: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSandboxMachinesOperationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesOperationsListQuery:
        return ManagementInstanceSandboxMachinesOperationsListQuery(
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
    def to_dict(value: Union[ManagementInstanceSandboxMachinesOperationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

