from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutput, DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput, mapDashboardInstancePortalsAuthSsoTenantsConnectionsListQuery, DashboardInstancePortalsAuthSsoTenantsConnectionsListQuery

class MetorialManagementInstancePortalsAuthSsoTenantsConnectionsEndpoint(BaseMetorialEndpoint):
    """Manage the Ares-backed authentication configuration for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, sso_tenant_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput:
        """
    List portal auth SSO tenant connections
    Returns SSO connections that belong to a portal SSO tenant.

    :param instance_id: str
    :param portal_id: str
    :param sso_tenant_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput
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

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'auth', 'sso-tenants', sso_tenant_id, 'connections'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutput.from_dict)