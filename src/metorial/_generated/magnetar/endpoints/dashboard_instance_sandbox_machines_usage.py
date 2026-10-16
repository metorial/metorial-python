from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesUsageTimelineOutput, DashboardInstanceSandboxMachinesUsageTimelineOutput, mapDashboardInstanceSandboxMachinesUsageTimelineQuery, DashboardInstanceSandboxMachinesUsageTimelineQuery, mapDashboardInstanceSandboxMachinesUsageSummaryOutput, DashboardInstanceSandboxMachinesUsageSummaryOutput, mapDashboardInstanceSandboxMachinesUsageSummaryQuery, DashboardInstanceSandboxMachinesUsageSummaryQuery

class MetorialDashboardInstanceSandboxMachinesUsageEndpoint(BaseMetorialEndpoint):
    """Aggregated measured CPU, memory, network, disk I/O, and observed runtime. History is flushed approximately every minute and is not billing consumption."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def timeline(self, instance_id: str, machine_id: str, *, from_: datetime, to: datetime, machine_instance_id: Optional[Union[str, List[str]]] = None, group_by: Optional[Any] = None, max_series: Optional[float] = None, interval: Optional[str] = None) -> DashboardInstanceSandboxMachinesUsageTimelineOutput:
        """
    Get sandbox machine usage timeline
    Returns chronological usage buckets. Minute data is retained for 7 days and hourly data for 30 days. Zero samples means no observations, not necessarily a stopped machine.

    :param instance_id: str
    :param machine_id: str
    :param from_: datetime
    :param to: datetime
    :param machine_instance_id: Optional[Union[str, List[str]]] (optional)
    :param group_by: Optional[Any] (optional)
    :param max_series: Optional[float] (optional)
    :param interval: Optional[str] (optional)
    :return: DashboardInstanceSandboxMachinesUsageTimelineOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["from"] = from_
        query_dict["to"] = to
        if machine_instance_id is not None:
            query_dict["machine_instance_id"] = machine_instance_id
        if group_by is not None:
            query_dict["group_by"] = group_by
        if max_series is not None:
            query_dict["max_series"] = max_series
        if interval is not None:
            query_dict["interval"] = interval

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'usage', 'timeline'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesUsageTimelineOutput.from_dict)

    def summary(self, instance_id: str, machine_id: str, *, from_: datetime, to: datetime, machine_instance_id: Optional[Union[str, List[str]]] = None, group_by: Optional[Any] = None, max_series: Optional[float] = None) -> DashboardInstanceSandboxMachinesUsageSummaryOutput:
        """
    Get sandbox machine usage summary
    Returns totals and averages for a range. Summary bounds align independently to minute or hour source buckets. Use a timeline’s effective bounds to compare its totals with a summary.

    :param instance_id: str
    :param machine_id: str
    :param from_: datetime
    :param to: datetime
    :param machine_instance_id: Optional[Union[str, List[str]]] (optional)
    :param group_by: Optional[Any] (optional)
    :param max_series: Optional[float] (optional)
    :return: DashboardInstanceSandboxMachinesUsageSummaryOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["from"] = from_
        query_dict["to"] = to
        if machine_instance_id is not None:
            query_dict["machine_instance_id"] = machine_instance_id
        if group_by is not None:
            query_dict["group_by"] = group_by
        if max_series is not None:
            query_dict["max_series"] = max_series

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'usage', 'summary'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesUsageSummaryOutput.from_dict)