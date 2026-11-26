from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationInternetGatewayGetOutput, DashboardInstanceIntegrationInternetGatewayGetOutput, mapDashboardInstanceIntegrationInternetGatewayListNetworkLogsOutput, DashboardInstanceIntegrationInternetGatewayListNetworkLogsOutput, mapDashboardInstanceIntegrationInternetGatewayListNetworkLogsQuery, DashboardInstanceIntegrationInternetGatewayListNetworkLogsQuery

class MetorialIntegrationInternetGatewayEndpoint(BaseMetorialEndpoint):
    """An integration internet gateway is the shared network exit for integration enclaves in an instance. Enclaves use it to reach the internet and be reached from it."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> DashboardInstanceIntegrationInternetGatewayGetOutput:
        """
    Get integration internet gateway
    Retrieves the instance's integration internet gateway. Public IPs are masked as `x.x.x.x` unless your plan includes IP access.


    :return: DashboardInstanceIntegrationInternetGatewayGetOutput
    """
        request = MetorialRequest(
            path=['integration-internet-gateway']
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationInternetGatewayGetOutput.from_dict)

    def list_network_logs(self, *, direction: str, enclave_id: Optional[Union[str, List[str]]] = None, hostname: Optional[Union[str, List[str]]] = None, ip: Optional[Union[str, List[str]]] = None, from_: Optional[str] = None, to: Optional[str] = None, interval_minutes: Optional[float] = None) -> DashboardInstanceIntegrationInternetGatewayListNetworkLogsOutput:
        """
    List integration internet gateway network logs
    Returns network logs for integration enclaves in the instance. Set `direction` to choose ingress or egress logs.

    :param direction: str
    :param enclave_id: Optional[Union[str, List[str]]] (optional)
    :param hostname: Optional[Union[str, List[str]]] (optional)
    :param ip: Optional[Union[str, List[str]]] (optional)
    :param from_: Optional[str] (optional)
    :param to: Optional[str] (optional)
    :param interval_minutes: Optional[float] (optional)
    :return: DashboardInstanceIntegrationInternetGatewayListNetworkLogsOutput
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
            path=['integration-internet-gateway', 'network-logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationInternetGatewayListNetworkLogsOutput.from_dict)