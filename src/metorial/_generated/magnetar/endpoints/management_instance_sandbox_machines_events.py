from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesEventsListOutput, DashboardInstanceSandboxMachinesEventsListOutput, mapDashboardInstanceSandboxMachinesEventsListQuery, DashboardInstanceSandboxMachinesEventsListQuery, mapDashboardInstanceSandboxMachinesEventsGetOutput, DashboardInstanceSandboxMachinesEventsGetOutput

class MetorialManagementInstanceSandboxMachinesEventsEndpoint(BaseMetorialEndpoint):
    """The timeline of everything that happened to a machine and its instances."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, machine_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, scope: Optional[str] = None, machine_instance_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, source: Optional[Union[str, List[str]]] = None, reverse: Optional[bool] = None) -> DashboardInstanceSandboxMachinesEventsListOutput:
        """
    List machine events
    Returns a paginated list of the events of a machine.

    :param instance_id: str
    :param machine_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param scope: Optional[str] (optional)
    :param machine_instance_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param source: Optional[Union[str, List[str]]] (optional)
    :param reverse: Optional[bool] (optional)
    :return: DashboardInstanceSandboxMachinesEventsListOutput
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
        if scope is not None:
            query_dict["scope"] = scope
        if machine_instance_id is not None:
            query_dict["machine_instance_id"] = machine_instance_id
        if type is not None:
            query_dict["type"] = type
        if source is not None:
            query_dict["source"] = source
        if reverse is not None:
            query_dict["reverse"] = reverse

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesEventsListOutput.from_dict)

    def get(self, instance_id: str, machine_id: str, event_id: str) -> DashboardInstanceSandboxMachinesEventsGetOutput:
        """
    Get machine event
    Retrieves an event of a machine.

    :param instance_id: str
    :param machine_id: str
    :param event_id: str
    :return: DashboardInstanceSandboxMachinesEventsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'machines', machine_id, 'events', event_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesEventsGetOutput.from_dict)