from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthCliDevicesListOutput, DashboardOrganizationsOauthCliDevicesListOutput, mapDashboardOrganizationsOauthCliDevicesListQuery, DashboardOrganizationsOauthCliDevicesListQuery, mapDashboardOrganizationsOauthCliDevicesGetOutput, DashboardOrganizationsOauthCliDevicesGetOutput

class MetorialManagementOrganizationOauthCliDevicesEndpoint(BaseMetorialEndpoint):
    """Inspect CLI devices for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsOauthCliDevicesListOutput:
        """
    List organization CLI devices
    Returns a paginated list of CLI devices for the organization.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsOauthCliDevicesListOutput
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
            path=['organization', 'oauth', 'cli-devices'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthCliDevicesListOutput.from_dict)

    def get(self, cli_device_id: str) -> DashboardOrganizationsOauthCliDevicesGetOutput:
        """
    Get organization CLI device
    Retrieves a specific CLI device for the organization.

    :param cli_device_id: str
    :return: DashboardOrganizationsOauthCliDevicesGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'cli-devices', cli_device_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthCliDevicesGetOutput.from_dict)