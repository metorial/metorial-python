from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationFirewallAssignmentsListOutput, DashboardInstanceIntegrationFirewallAssignmentsListOutput, mapDashboardInstanceIntegrationFirewallAssignmentsListQuery, DashboardInstanceIntegrationFirewallAssignmentsListQuery, mapDashboardInstanceIntegrationFirewallAssignmentsGetOutput, DashboardInstanceIntegrationFirewallAssignmentsGetOutput, mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutput, DashboardInstanceIntegrationFirewallAssignmentsCreateOutput, mapDashboardInstanceIntegrationFirewallAssignmentsCreateBody, DashboardInstanceIntegrationFirewallAssignmentsCreateBody, mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutput, DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput

class MetorialDashboardInstanceIntegrationFirewallAssignmentsEndpoint(BaseMetorialEndpoint):
    """Manage assignments that apply firewalls to integration enclaves, providers, or the integration internet gateway."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, firewall_id: Optional[Union[str, List[str]]] = None, enclave_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, internet_gateway_id: Optional[Union[str, List[str]]] = None, target_type: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationFirewallAssignmentsListOutput:
        """
    List integration firewall assignments
    Returns a paginated list of integration firewall assignments.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param firewall_id: Optional[Union[str, List[str]]] (optional)
    :param enclave_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param internet_gateway_id: Optional[Union[str, List[str]]] (optional)
    :param target_type: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationFirewallAssignmentsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if internet_gateway_id is not None:
            query_dict["internet_gateway_id"] = internet_gateway_id
        if target_type is not None:
            query_dict["target_type"] = target_type
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-firewall-assignments'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationFirewallAssignmentsListOutput.from_dict)

    def get(self, instance_id: str, integration_firewall_assignment_id: str) -> DashboardInstanceIntegrationFirewallAssignmentsGetOutput:
        """
    Get integration firewall assignment
    Retrieves a specific integration firewall assignment by ID.

    :param instance_id: str
    :param integration_firewall_assignment_id: str
    :return: DashboardInstanceIntegrationFirewallAssignmentsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-firewall-assignments', integration_firewall_assignment_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationFirewallAssignmentsGetOutput.from_dict)

    def create(self, instance_id: str, *, firewall_id: str, target_type: str, enclave_id: Optional[str] = None, provider_id: Optional[str] = None) -> DashboardInstanceIntegrationFirewallAssignmentsCreateOutput:
        """
    Create integration firewall assignment
    Creates an assignment that applies a firewall to a target.

    :param instance_id: str
    :param firewall_id: str
    :param target_type: str
    :param enclave_id: Optional[str] (optional)
    :param provider_id: Optional[str] (optional)
    :return: DashboardInstanceIntegrationFirewallAssignmentsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["firewall_id"] = firewall_id
        body_dict["target_type"] = target_type
        if enclave_id is not None:
            body_dict["enclave_id"] = enclave_id
        if provider_id is not None:
            body_dict["provider_id"] = provider_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-firewall-assignments'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutput.from_dict)

    def delete(self, instance_id: str, integration_firewall_assignment_id: str) -> DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput:
        """
    Delete integration firewall assignment
    Deletes an integration firewall assignment.

    :param instance_id: str
    :param integration_firewall_assignment_id: str
    :return: DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-firewall-assignments', integration_firewall_assignment_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutput.from_dict)