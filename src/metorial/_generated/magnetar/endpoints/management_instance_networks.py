from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceNetworksListOutput, DashboardInstanceNetworksListOutput, mapDashboardInstanceNetworksListQuery, DashboardInstanceNetworksListQuery, mapDashboardInstanceNetworksGetOutput, DashboardInstanceNetworksGetOutput, mapDashboardInstanceNetworksListNetworkLogsOutput, DashboardInstanceNetworksListNetworkLogsOutput, mapDashboardInstanceNetworksListNetworkLogsQuery, DashboardInstanceNetworksListNetworkLogsQuery

class MetorialManagementInstanceNetworksEndpoint(BaseMetorialEndpoint):
    """Read network records for an instance environment."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, firewall_id: Optional[Union[str, List[str]]] = None, enclave_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceNetworksListOutput:
        """
    List networks
    Returns a paginated list of networks.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param firewall_id: Optional[Union[str, List[str]]] (optional)
    :param enclave_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceNetworksListOutput
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
        if id is not None:
            query_dict["id"] = id
        if firewall_id is not None:
            query_dict["firewall_id"] = firewall_id
        if enclave_id is not None:
            query_dict["enclave_id"] = enclave_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'networks'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceNetworksListOutput.from_dict)

    def get(self, instance_id: str, network_id: str) -> DashboardInstanceNetworksGetOutput:
        """
    Get network
    Retrieves a specific network by ID.

    :param instance_id: str
    :param network_id: str
    :return: DashboardInstanceNetworksGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'networks', network_id]
        )
        return self._get(request).transform(mapDashboardInstanceNetworksGetOutput.from_dict)

    def list_network_logs(self, instance_id: str, *, direction: str, enclave_id: Optional[Union[str, List[str]]] = None, hostname: Optional[Union[str, List[str]]] = None, ip: Optional[Union[str, List[str]]] = None, from_: Optional[str] = None, to: Optional[str] = None, interval_minutes: Optional[float] = None) -> DashboardInstanceNetworksListNetworkLogsOutput:
        """
    List network logs
    Returns ingress or egress network logs for enclaves in the instance environment.

    :param instance_id: str
    :param direction: str
    :param enclave_id: Optional[Union[str, List[str]]] (optional)
    :param hostname: Optional[Union[str, List[str]]] (optional)
    :param ip: Optional[Union[str, List[str]]] (optional)
    :param from_: Optional[str] (optional)
    :param to: Optional[str] (optional)
    :param interval_minutes: Optional[float] (optional)
    :return: DashboardInstanceNetworksListNetworkLogsOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["direction"] = direction
        if enclave_id is not None:
            query_dict["enclave_id"] = enclave_id
        if hostname is not None:
            query_dict["hostname"] = hostname
        if ip is not None:
            query_dict["ip"] = ip
        if from_ is not None:
            query_dict["from"] = from_
        if to is not None:
            query_dict["to"] = to
        if interval_minutes is not None:
            query_dict["interval_minutes"] = interval_minutes

        request = MetorialRequest(
            path=['instances', instance_id, 'network-logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceNetworksListNetworkLogsOutput.from_dict)