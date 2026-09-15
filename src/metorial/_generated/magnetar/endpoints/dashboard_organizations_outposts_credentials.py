from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOutpostsCredentialsCreateOutput, DashboardOrganizationsOutpostsCredentialsCreateOutput, mapDashboardOrganizationsOutpostsCredentialsCreateBody, DashboardOrganizationsOutpostsCredentialsCreateBody, mapDashboardOrganizationsOutpostsCredentialsListOutput, DashboardOrganizationsOutpostsCredentialsListOutput, mapDashboardOrganizationsOutpostsCredentialsListQuery, DashboardOrganizationsOutpostsCredentialsListQuery, mapDashboardOrganizationsOutpostsCredentialsGetOutput, DashboardOrganizationsOutpostsCredentialsGetOutput, mapDashboardOrganizationsOutpostsCredentialsDisableOutput, DashboardOrganizationsOutpostsCredentialsDisableOutput, mapDashboardOrganizationsOutpostsCredentialsDeleteOutput, DashboardOrganizationsOutpostsCredentialsDeleteOutput

class MetorialDashboardOrganizationsOutpostsCredentialsEndpoint(BaseMetorialEndpoint):
    """Read and write outposts, their access grants, and credentials"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, organization_id: str, outpost_id: str, *, name: str, expires_at: Optional[datetime] = None) -> DashboardOrganizationsOutpostsCredentialsCreateOutput:
        """
    Create outpost credential
    Create a new enrollment credential for an outpost owned by this organization

    :param organization_id: str
    :param outpost_id: str
    :param name: str
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardOrganizationsOutpostsCredentialsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if expires_at is not None:
            body_dict["expires_at"] = expires_at

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'credentials'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsCredentialsCreateOutput.from_dict)

    def list(self, organization_id: str, outpost_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsOutpostsCredentialsListOutput:
        """
    List outpost credentials
    List the credentials for an outpost owned by this organization

    :param organization_id: str
    :param outpost_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsOutpostsCredentialsListOutput
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
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'credentials'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOutpostsCredentialsListOutput.from_dict)

    def get(self, organization_id: str, outpost_id: str, credential_id: str) -> DashboardOrganizationsOutpostsCredentialsGetOutput:
        """
    Get outpost credential
    Get a credential for an outpost owned by this organization

    :param organization_id: str
    :param outpost_id: str
    :param credential_id: str
    :return: DashboardOrganizationsOutpostsCredentialsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'credentials', credential_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsOutpostsCredentialsGetOutput.from_dict)

    def disable(self, organization_id: str, outpost_id: str, credential_id: str) -> DashboardOrganizationsOutpostsCredentialsDisableOutput:
        """
    Disable outpost credential
    Disable a credential for an outpost owned by this organization. A credential must be disabled before it can be deleted.

    :param organization_id: str
    :param outpost_id: str
    :param credential_id: str
    :return: DashboardOrganizationsOutpostsCredentialsDisableOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'credentials', credential_id, 'disable']
        )
        return self._post(request).transform(mapDashboardOrganizationsOutpostsCredentialsDisableOutput.from_dict)

    def delete(self, organization_id: str, outpost_id: str, credential_id: str) -> DashboardOrganizationsOutpostsCredentialsDeleteOutput:
        """
    Delete outpost credential
    Delete a disabled credential for an outpost owned by this organization

    :param organization_id: str
    :param outpost_id: str
    :param credential_id: str
    :return: DashboardOrganizationsOutpostsCredentialsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'outposts', outpost_id, 'credentials', credential_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsOutpostsCredentialsDeleteOutput.from_dict)