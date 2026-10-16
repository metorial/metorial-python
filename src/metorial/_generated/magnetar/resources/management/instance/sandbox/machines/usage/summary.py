from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup:
    machine_instance_id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals:
    samples: float
    runtime_seconds: float
    cpu_core_seconds: float
    average_cores_used: float
    cpu_percent: float
    peak_cores_used: float
    memory_byte_seconds: float
    average_memory_used_bytes: float
    peak_memory_used_bytes: float
    allocated_memory_byte_seconds: float
    average_memory_allocated_bytes: float
    network_rx_bytes: float
    network_tx_bytes: float
    disk_read_bytes: float
    disk_write_bytes: float
@dataclass
class ManagementInstanceSandboxMachinesUsageSummaryOutputGroups:
    group: ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup
    other: bool
    totals: ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals
@dataclass
class ManagementInstanceSandboxMachinesUsageSummaryOutput:
    object: str
    machine_id: str
    from_: datetime
    to: datetime
    resolution: str
    group_by: List[str]
    groups: List[ManagementInstanceSandboxMachinesUsageSummaryOutputGroups]


class mapManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup:
        return ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup(
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals:
        return ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals(
        samples=data.get('samples'),
        runtime_seconds=data.get('runtime_seconds'),
        cpu_core_seconds=data.get('cpu_core_seconds'),
        average_cores_used=data.get('average_cores_used'),
        cpu_percent=data.get('cpu_percent'),
        peak_cores_used=data.get('peak_cores_used'),
        memory_byte_seconds=data.get('memory_byte_seconds'),
        average_memory_used_bytes=data.get('average_memory_used_bytes'),
        peak_memory_used_bytes=data.get('peak_memory_used_bytes'),
        allocated_memory_byte_seconds=data.get('allocated_memory_byte_seconds'),
        average_memory_allocated_bytes=data.get('average_memory_allocated_bytes'),
        network_rx_bytes=data.get('network_rx_bytes'),
        network_tx_bytes=data.get('network_tx_bytes'),
        disk_read_bytes=data.get('disk_read_bytes'),
        disk_write_bytes=data.get('disk_write_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUsageSummaryOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUsageSummaryOutputGroups:
        return ManagementInstanceSandboxMachinesUsageSummaryOutputGroups(
        group=mapManagementInstanceSandboxMachinesUsageSummaryOutputGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        other=data.get('other'),
        totals=mapManagementInstanceSandboxMachinesUsageSummaryOutputGroupsTotals.from_dict(data.get('totals')) if data.get('totals') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUsageSummaryOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUsageSummaryOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUsageSummaryOutput:
        return ManagementInstanceSandboxMachinesUsageSummaryOutput(
        object=data.get('object'),
        machine_id=data.get('machine_id'),
        from_=datetime.fromisoformat(data.get('from').replace('Z', '+00:00')) if data.get('from') else None,
        to=datetime.fromisoformat(data.get('to').replace('Z', '+00:00')) if data.get('to') else None,
        resolution=data.get('resolution'),
        group_by=data.get('group_by', []),
        groups=[mapManagementInstanceSandboxMachinesUsageSummaryOutputGroups.from_dict(item) for item in data.get('groups', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUsageSummaryOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesUsageSummaryQuery:
    from_: datetime
    to: datetime
    machine_instance_id: Optional[Union[str, List[str]]] = None
    group_by: Optional[str] = None
    max_series: Optional[float] = None


class mapManagementInstanceSandboxMachinesUsageSummaryQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUsageSummaryQuery:
        return ManagementInstanceSandboxMachinesUsageSummaryQuery(
        from_=datetime.fromisoformat(data.get('from').replace('Z', '+00:00')) if data.get('from') else None,
        to=datetime.fromisoformat(data.get('to').replace('Z', '+00:00')) if data.get('to') else None,
        machine_instance_id=data.get('machine_instance_id'),
        group_by=data.get('group_by'),
        max_series=data.get('max_series')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUsageSummaryQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

