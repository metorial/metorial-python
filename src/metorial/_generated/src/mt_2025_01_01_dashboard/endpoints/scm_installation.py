from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceScmInstallationListOutput, DashboardInstanceScmInstallationListOutput, mapDashboardInstanceScmInstallationListQuery, DashboardInstanceScmInstallationListQuery, mapDashboardInstanceScmInstallationCreateOutput, DashboardInstanceScmInstallationCreateOutput, mapDashboardInstanceScmInstallationCreateBody, DashboardInstanceScmInstallationCreateBody

class MetorialScmInstallationEndpoint(BaseMetorialEndpoint):
    """Manage source control management installations (e.g. GitHub App installations)."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceScmInstallationListOutput:
        """
    List SCM installations
    Returns a paginated list of SCM installations.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceScmInstallationListOutput
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
            path=['scm', 'installations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceScmInstallationListOutput.from_dict)

    def create(self, *, provider: Optional[str] = None, redirect_url: Optional[str] = None) -> DashboardInstanceScmInstallationCreateOutput:
        """
    Create SCM installation
    Initiates an SCM installation setup (e.g. GitHub App authorization).

    :param provider: Optional[str] (optional)
    :param redirect_url: Optional[str] (optional)
    :return: DashboardInstanceScmInstallationCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if provider is not None:
            body_dict["provider"] = provider
        if redirect_url is not None:
            body_dict["redirect_url"] = redirect_url

        request = MetorialRequest(
            path=['scm', 'installations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceScmInstallationCreateOutput.from_dict)
