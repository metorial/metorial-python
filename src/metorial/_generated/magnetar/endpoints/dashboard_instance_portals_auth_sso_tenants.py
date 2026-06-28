from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAuthSsoTenantsListOutput, DashboardInstancePortalsAuthSsoTenantsListOutput, mapDashboardInstancePortalsAuthSsoTenantsListQuery, DashboardInstancePortalsAuthSsoTenantsListQuery, mapDashboardInstancePortalsAuthSsoTenantsCreateOutput, DashboardInstancePortalsAuthSsoTenantsCreateOutput, mapDashboardInstancePortalsAuthSsoTenantsCreateBody, DashboardInstancePortalsAuthSsoTenantsCreateBody, mapDashboardInstancePortalsAuthSsoTenantsSetupOutput, DashboardInstancePortalsAuthSsoTenantsSetupOutput

class MetorialDashboardInstancePortalsAuthSsoTenantsEndpoint(BaseMetorialEndpoint):
    """Manage the Ares-backed authentication configuration for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstancePortalsAuthSsoTenantsListOutput:
        """
    List portal auth SSO tenants
    Returns the SSO tenants configured for a portal Ares app.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstancePortalsAuthSsoTenantsListOutput
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
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'auth', 'sso-tenants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsAuthSsoTenantsListOutput.from_dict)

    def create(self, instance_id: str, portal_id: str, *, name: str) -> DashboardInstancePortalsAuthSsoTenantsCreateOutput:
        """
    Create portal auth SSO tenant
    Creates an SSO tenant for the portal Ares app.

    :param instance_id: str
    :param portal_id: str
    :param name: str
    :return: DashboardInstancePortalsAuthSsoTenantsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'auth', 'sso-tenants'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsAuthSsoTenantsCreateOutput.from_dict)

    def setup(self, instance_id: str, portal_id: str, sso_tenant_id: str) -> DashboardInstancePortalsAuthSsoTenantsSetupOutput:
        """
    Create portal auth SSO tenant setup
    Creates an Ares setup URL for finishing portal SSO tenant configuration.

    :param instance_id: str
    :param portal_id: str
    :param sso_tenant_id: str
    :return: DashboardInstancePortalsAuthSsoTenantsSetupOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'auth', 'sso-tenants', sso_tenant_id, 'setup']
        )
        return self._post(request).transform(mapDashboardInstancePortalsAuthSsoTenantsSetupOutput.from_dict)