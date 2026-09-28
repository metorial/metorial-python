from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOutpostsAccessSetOutput, DashboardOrganizationsOutpostsAccessSetOutput, mapDashboardOrganizationsOutpostsAccessSetBody, DashboardOrganizationsOutpostsAccessSetBody, mapDashboardOrganizationsOutpostsAccessListOutput, DashboardOrganizationsOutpostsAccessListOutput, mapDashboardOrganizationsOutpostsAccessListQuery, DashboardOrganizationsOutpostsAccessListQuery

class MetorialDashboardOrganizationsOutpostsAccessEndpoint(BaseMetorialEndpoint):
    """Read and write outposts, their access grants, and credentials"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def set(self, organization_id: str, outpost_id: str, *, grants: List[Dict[str, Any]]) -> DashboardOrganizationsOutpostsAccessSetOutput:
        """
    Set outpost access
    Replace this organization's access grants on an outpost with the given list of instance/service grants

    :param organization_id: str
    :param outpost_id: str
    :param grants: List[Dict[str, Any]]
    :return: DashboardOrganizationsOutpostsAccessSetOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["grants"] = grants

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'access'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsAccessSetOutput.from_dict)

    def list(self, organization_id: str, outpost_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, instance_id: Optional[str] = None) -> DashboardOrganizationsOutpostsAccessListOutput:
        """
    List outpost access
    List the access grants on an outpost, optionally filtered by organization or instance

    :param organization_id: str
    :param outpost_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param instance_id: Optional[str] (optional)
    :return: DashboardOrganizationsOutpostsAccessListOutput
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
        if instance_id is not None:
            query_dict["instance_id"] = instance_id

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'access'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOutpostsAccessListOutput.from_dict)