from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOutpostsListOutput, DashboardOrganizationsOutpostsListOutput, mapDashboardOrganizationsOutpostsListQuery, DashboardOrganizationsOutpostsListQuery, mapDashboardOrganizationsOutpostsGetOutput, DashboardOrganizationsOutpostsGetOutput, mapDashboardOrganizationsOutpostsCreateOutput, DashboardOrganizationsOutpostsCreateOutput, mapDashboardOrganizationsOutpostsCreateBody, DashboardOrganizationsOutpostsCreateBody, mapDashboardOrganizationsOutpostsUpdateOutput, DashboardOrganizationsOutpostsUpdateOutput, mapDashboardOrganizationsOutpostsUpdateBody, DashboardOrganizationsOutpostsUpdateBody, mapDashboardOrganizationsOutpostsDisableOutput, DashboardOrganizationsOutpostsDisableOutput, mapDashboardOrganizationsOutpostsEnableOutput, DashboardOrganizationsOutpostsEnableOutput, mapDashboardOrganizationsOutpostsDeleteOutput, DashboardOrganizationsOutpostsDeleteOutput

class MetorialManagementOrganizationOutpostsEndpoint(BaseMetorialEndpoint):
    """Read and write outposts, their access grants, and credentials"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsOutpostsListOutput:
        """
    List outposts
    List every outpost in the organization's account family

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsOutpostsListOutput
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
            path=['organization', 'outposts'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOutpostsListOutput.from_dict)

    def get(self, outpost_id: str) -> DashboardOrganizationsOutpostsGetOutput:
        """
    Get outpost
    Get any outpost in the organization's account family

    :param outpost_id: str
    :return: DashboardOrganizationsOutpostsGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'outposts', outpost_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsOutpostsGetOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None) -> DashboardOrganizationsOutpostsCreateOutput:
        """
    Create outpost
    Create a new outpost owned by this organization

    :param name: str
    :param description: Optional[str] (optional)
    :return: DashboardOrganizationsOutpostsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['organization', 'outposts'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsCreateOutput.from_dict)

    def update(self, outpost_id: str, *, name: Optional[str] = None, description: Optional[str] = None) -> DashboardOrganizationsOutpostsUpdateOutput:
        """
    Update outpost
    Update the information of an outpost owned by this organization

    :param outpost_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: DashboardOrganizationsOutpostsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['organization', 'outposts', outpost_id],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsUpdateOutput.from_dict)

    def disable(self, outpost_id: str) -> DashboardOrganizationsOutpostsDisableOutput:
        """
    Disable outpost
    Disable an outpost owned by this organization. An outpost must be disabled before it can be deleted.

    :param outpost_id: str
    :return: DashboardOrganizationsOutpostsDisableOutput
    """
        request = MetorialRequest(
            path=['organization', 'outposts', outpost_id, 'disable']
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsDisableOutput.from_dict)

    def enable(self, outpost_id: str) -> DashboardOrganizationsOutpostsEnableOutput:
        """
    Enable outpost
    Enable a disabled outpost owned by this organization

    :param outpost_id: str
    :return: DashboardOrganizationsOutpostsEnableOutput
    """
        request = MetorialRequest(
            path=['organization', 'outposts', outpost_id, 'enable']
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsEnableOutput.from_dict)

    def delete(self, outpost_id: str) -> DashboardOrganizationsOutpostsDeleteOutput:
        """
    Delete outpost
    Delete a disabled outpost owned by this organization

    :param outpost_id: str
    :return: DashboardOrganizationsOutpostsDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'outposts', outpost_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsOutpostsDeleteOutput.from_dict)