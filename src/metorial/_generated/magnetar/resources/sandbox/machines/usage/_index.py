from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesUsageOutputItems:
    object: str
    id: str
    machine_instance_id: str
    timestamp: datetime
    cpu_percent: float
    cores_used: float
    cores_available: float
    memory_used_bytes: float
    memory_total_bytes: float
    network_rx_bytes: float
    network_tx_bytes: float
    disk_read_bytes: float
    disk_write_bytes: float
@dataclass
class SandboxMachinesUsageOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxMachinesUsageOutput:
    items: List[SandboxMachinesUsageOutputItems]
    pagination: SandboxMachinesUsageOutputPagination


class mapSandboxMachinesUsageOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUsageOutputItems:
        return SandboxMachinesUsageOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_instance_id=data.get('machine_instance_id'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        cpu_percent=data.get('cpu_percent'),
        cores_used=data.get('cores_used'),
        cores_available=data.get('cores_available'),
        memory_used_bytes=data.get('memory_used_bytes'),
        memory_total_bytes=data.get('memory_total_bytes'),
        network_rx_bytes=data.get('network_rx_bytes'),
        network_tx_bytes=data.get('network_tx_bytes'),
        disk_read_bytes=data.get('disk_read_bytes'),
        disk_write_bytes=data.get('disk_write_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUsageOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUsageOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUsageOutputPagination:
        return SandboxMachinesUsageOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUsageOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUsageOutput:
        return SandboxMachinesUsageOutput(
        items=[mapSandboxMachinesUsageOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxMachinesUsageOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesUsageQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    machine_instance_id: Optional[Union[str, List[str]]] = None


class mapSandboxMachinesUsageQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUsageQuery:
        return SandboxMachinesUsageQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUsageQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

