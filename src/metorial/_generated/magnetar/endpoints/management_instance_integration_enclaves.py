from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationEnclavesListOutput, DashboardInstanceIntegrationEnclavesListOutput, mapDashboardInstanceIntegrationEnclavesListQuery, DashboardInstanceIntegrationEnclavesListQuery, mapDashboardInstanceIntegrationEnclavesGetOutput, DashboardInstanceIntegrationEnclavesGetOutput

class MetorialManagementInstanceIntegrationEnclavesEndpoint(BaseMetorialEndpoint):
    """Read integration enclave records for provider deployments in an instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, slug: Optional[Union[str, List[str]]] = None, internet_gateway_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, firewall_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationEnclavesListOutput:
        """
    List integration enclaves
    Returns a paginated list of integration enclaves.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param slug: Optional[Union[str, List[str]]] (optional)
    :param internet_gateway_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param firewall_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationEnclavesListOutput
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
        if slug is not None:
            query_dict["slug"] = slug
        if internet_gateway_id is not None:
            query_dict["internet_gateway_id"] = internet_gateway_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if firewall_id is not None:
            query_dict["firewall_id"] = firewall_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['instances', instance_id, 'integration-enclaves'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationEnclavesListOutput.from_dict)

    def get(self, instance_id: str, integration_enclave_id: str) -> DashboardInstanceIntegrationEnclavesGetOutput:
        """
    Get integration enclave
    Retrieves a specific integration enclave by ID.

    :param instance_id: str
    :param integration_enclave_id: str
    :return: DashboardInstanceIntegrationEnclavesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'integration-enclaves', integration_enclave_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationEnclavesGetOutput.from_dict)