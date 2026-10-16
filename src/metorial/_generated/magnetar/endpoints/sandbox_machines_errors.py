from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesErrorsListOutput, DashboardInstanceSandboxMachinesErrorsListOutput, mapDashboardInstanceSandboxMachinesErrorsListQuery, DashboardInstanceSandboxMachinesErrorsListQuery, mapDashboardInstanceSandboxMachinesErrorsGetOutput, DashboardInstanceSandboxMachinesErrorsGetOutput

class MetorialSandboxMachinesErrorsEndpoint(BaseMetorialEndpoint):
    """Errors reported from inside a machine, such as a failing lifecycle hook or setup command."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, machine_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, machine_instance_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxMachinesErrorsListOutput:
        """
    List machine errors
    Returns a paginated list of the errors reported by a machine.

    :param machine_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param machine_instance_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxMachinesErrorsListOutput
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

        request = MetorialRequest(
            path=['sandbox', 'machines', machine_id, 'errors'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesErrorsListOutput.from_dict)

    def get(self, machine_id: str, error_id: str) -> DashboardInstanceSandboxMachinesErrorsGetOutput:
        """
    Get machine error
    Retrieves an error reported by a machine.

    :param machine_id: str
    :param error_id: str
    :return: DashboardInstanceSandboxMachinesErrorsGetOutput
    """
        request = MetorialRequest(
            path=['sandbox', 'machines', machine_id, 'errors', error_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesErrorsGetOutput.from_dict)