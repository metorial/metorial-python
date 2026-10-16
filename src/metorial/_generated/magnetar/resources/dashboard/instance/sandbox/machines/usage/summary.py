from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup:
    machine_instance_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals:
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
class DashboardInstanceSandboxMachinesUsageSummaryOutputGroups:
    group: DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup
    other: bool
    totals: DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals
@dataclass
class DashboardInstanceSandboxMachinesUsageSummaryOutput:
    object: str
    machine_id: str
    from_: datetime
    to: datetime
    resolution: str
    group_by: List[str]
    groups: List[DashboardInstanceSandboxMachinesUsageSummaryOutputGroups]


class mapDashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup:
        return DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup(
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals:
        return DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals(
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
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUsageSummaryOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUsageSummaryOutputGroups:
        return DashboardInstanceSandboxMachinesUsageSummaryOutputGroups(
        group=mapDashboardInstanceSandboxMachinesUsageSummaryOutputGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        other=data.get('other'),
        totals=mapDashboardInstanceSandboxMachinesUsageSummaryOutputGroupsTotals.from_dict(data.get('totals')) if data.get('totals') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUsageSummaryOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUsageSummaryOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUsageSummaryOutput:
        return DashboardInstanceSandboxMachinesUsageSummaryOutput(
        object=data.get('object'),
        machine_id=data.get('machine_id'),
        from_=datetime.fromisoformat(data.get('from').replace('Z', '+00:00')) if data.get('from') else None,
        to=datetime.fromisoformat(data.get('to').replace('Z', '+00:00')) if data.get('to') else None,
        resolution=data.get('resolution'),
        group_by=data.get('group_by', []),
        groups=[mapDashboardInstanceSandboxMachinesUsageSummaryOutputGroups.from_dict(item) for item in data.get('groups', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUsageSummaryOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesUsageSummaryQuery:
    from_: datetime
    to: datetime
    machine_instance_id: Optional[Union[str, List[str]]] = None
    group_by: Optional[str] = None
    max_series: Optional[float] = None


class mapDashboardInstanceSandboxMachinesUsageSummaryQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUsageSummaryQuery:
        return DashboardInstanceSandboxMachinesUsageSummaryQuery(
        from_=datetime.fromisoformat(data.get('from').replace('Z', '+00:00')) if data.get('from') else None,
        to=datetime.fromisoformat(data.get('to').replace('Z', '+00:00')) if data.get('to') else None,
        machine_instance_id=data.get('machine_instance_id'),
        group_by=data.get('group_by'),
        max_series=data.get('max_series')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUsageSummaryQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

