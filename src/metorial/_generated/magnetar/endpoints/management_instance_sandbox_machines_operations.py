from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesOperationsListOutput, DashboardInstanceSandboxMachinesOperationsListOutput, mapDashboardInstanceSandboxMachinesOperationsListQuery, DashboardInstanceSandboxMachinesOperationsListQuery, mapDashboardInstanceSandboxMachinesOperationsGetOutput, DashboardInstanceSandboxMachinesOperationsGetOutput

class MetorialManagementInstanceSandboxMachinesOperationsEndpoint(BaseMetorialEndpoint):
    """Operations record each start, pause, hibernate, restart, terminate, update, or upgrade a machine went through."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, machine_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, machine_instance_id: Optional[Union[str, List[str]]] = None, kind: Optional[Union[str, List[str]]] = None, trigger: Optional[Union[str, List[str]]] = None, outcome: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxMachinesOperationsListOutput:
        """
    List machine operations
    Returns a paginated list of the operations of a machine.

    :param instance_id: str
    :param machine_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param machine_instance_id: Optional[Union[str, List[str]]] (optional)
    :param kind: Optional[Union[str, List[str]]] (optional)
    :param trigger: Optional[Union[str, List[str]]] (optional)
    :param outcome: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxMachinesOperationsListOutput
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
        if machine_instance_id is not None:
            query_dict["machine_instance_id"] = machine_instance_id
        if kind is not None:
            query_dict["kind"] = kind
        if trigger is not None:
            query_dict["trigger"] = trigger
        if outcome is not None:
            query_dict["outcome"] = outcome

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'operations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesOperationsListOutput.from_dict)

    def get(self, instance_id: str, machine_id: str, operation_id: str) -> DashboardInstanceSandboxMachinesOperationsGetOutput:
        """
    Get machine operation
    Retrieves an operation of a machine.

    :param instance_id: str
    :param machine_id: str
    :param operation_id: str
    :return: DashboardInstanceSandboxMachinesOperationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'operations', operation_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesOperationsGetOutput.from_dict)