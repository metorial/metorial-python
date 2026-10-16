from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesInstancesListOutput, DashboardInstanceSandboxMachinesInstancesListOutput, mapDashboardInstanceSandboxMachinesInstancesListQuery, DashboardInstanceSandboxMachinesInstancesListQuery, mapDashboardInstanceSandboxMachinesInstancesGetOutput, DashboardInstanceSandboxMachinesInstancesGetOutput, mapDashboardInstanceSandboxMachinesInstancesLogsOutput, DashboardInstanceSandboxMachinesInstancesLogsOutput, mapDashboardInstanceSandboxMachinesInstancesLogsQuery, DashboardInstanceSandboxMachinesInstancesLogsQuery

class MetorialManagementInstanceSandboxMachinesInstancesEndpoint(BaseMetorialEndpoint):
    """Instances are the concrete virtual machines a sandbox machine runs on over its lifetime."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, machine_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxMachinesInstancesListOutput:
        """
    List machine instances
    Returns a paginated list of the instances of a machine.

    :param instance_id: str
    :param machine_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxMachinesInstancesListOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if limit is not None:
            query_dict["limit"] = limit
        if after is not None:
            query_dict["after"] = after
        if before is not None:
            query_dict["before"] = before
        if cursor is not None:
            query_dict["cursor"] = cursor
        if order is not None:
            query_dict["order"] = order
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'instances'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesInstancesListOutput.from_dict)

    def get(self, instance_id: str, machine_id: str, machine_instance_id: str) -> DashboardInstanceSandboxMachinesInstancesGetOutput:
        """
    Get machine instance
    Retrieves an instance of a machine.

    :param instance_id: str
    :param machine_id: str
    :param machine_instance_id: str
    :return: DashboardInstanceSandboxMachinesInstancesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'instances', machine_instance_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesInstancesGetOutput.from_dict)

    def logs(self, instance_id: str, machine_id: str, machine_instance_id: str, *, direction: Optional[str] = None, cursor: Optional[float] = None, limit: Optional[float] = None) -> DashboardInstanceSandboxMachinesInstancesLogsOutput:
        """
    Get machine instance logs
    Returns a page of the console output of an instance.

    :param instance_id: str
    :param machine_id: str
    :param machine_instance_id: str
    :param direction: Optional[str] (optional)
    :param cursor: Optional[float] (optional)
    :param limit: Optional[float] (optional)
    :return: DashboardInstanceSandboxMachinesInstancesLogsOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if direction is not None:
            query_dict["direction"] = direction
        if cursor is not None:
            query_dict["cursor"] = cursor
        if limit is not None:
            query_dict["limit"] = limit

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'instances', machine_instance_id, 'logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesInstancesLogsOutput.from_dict)