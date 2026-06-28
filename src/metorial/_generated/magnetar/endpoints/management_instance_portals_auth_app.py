from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAuthAppGetOutput, DashboardInstancePortalsAuthAppGetOutput, mapDashboardInstancePortalsAuthAppUpdateOutput, DashboardInstancePortalsAuthAppUpdateOutput, mapDashboardInstancePortalsAuthAppUpdateBody, DashboardInstancePortalsAuthAppUpdateBody

class MetorialManagementInstancePortalsAuthAppEndpoint(BaseMetorialEndpoint):
    """Manage the Ares-backed authentication configuration for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, portal_id: str) -> DashboardInstancePortalsAuthAppGetOutput:
        """
    Get portal auth app
    Returns the Ares app configuration for a portal.

    :param instance_id: str
    :param portal_id: str
    :return: DashboardInstancePortalsAuthAppGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'auth', 'app']
        )
        return self._get(request).transform(mapDashboardInstancePortalsAuthAppGetOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, *, email_whitelist: Optional[List[str]] = None) -> DashboardInstancePortalsAuthAppUpdateOutput:
        """
    Update portal auth app
    Updates the portal auth app configuration stored on the portal surface.

    :param instance_id: str
    :param portal_id: str
    :param email_whitelist: Optional[List[str]] (optional)
    :return: DashboardInstancePortalsAuthAppUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if email_whitelist is not None:
            body_dict["email_whitelist"] = email_whitelist

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'auth', 'app'],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsAuthAppUpdateOutput.from_dict)