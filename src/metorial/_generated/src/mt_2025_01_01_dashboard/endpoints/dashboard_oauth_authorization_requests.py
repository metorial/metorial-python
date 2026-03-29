from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOauthAuthorizationRequestsGetOutput, DashboardOauthAuthorizationRequestsGetOutput, mapDashboardOauthAuthorizationRequestsApproveOutput, DashboardOauthAuthorizationRequestsApproveOutput, mapDashboardOauthAuthorizationRequestsApproveBody, DashboardOauthAuthorizationRequestsApproveBody, mapDashboardOauthAuthorizationRequestsRejectOutput, DashboardOauthAuthorizationRequestsRejectOutput, mapDashboardOauthAuthorizationRequestsRejectBody, DashboardOauthAuthorizationRequestsRejectBody

class MetorialDashboardOauthAuthorizationRequestsEndpoint(BaseMetorialEndpoint):
    """Read and approve oauth authorization requests"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, url_token: str) -> DashboardOauthAuthorizationRequestsGetOutput:
        """
    Get OAuth authorization request
    Get an oauth authorization request by its url token

    :param url_token: str
    :return: DashboardOauthAuthorizationRequestsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'oauth', 'authorization-requests', url_token]
        )
        return self._get(request).transform(mapDashboardOauthAuthorizationRequestsGetOutput.from_dict)

    def approve(self, url_token: str, *, organization_id: str) -> DashboardOauthAuthorizationRequestsApproveOutput:
        """
    Approve OAuth authorization request
    Approve an oauth authorization request for an organization

    :param url_token: str
    :param organization_id: str
    :return: DashboardOauthAuthorizationRequestsApproveOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["organization_id"] = organization_id

        request = MetorialRequest(
            path=['dashboard', 'oauth', 'authorization-requests', url_token, 'approve'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOauthAuthorizationRequestsApproveOutput.from_dict)

    def reject(self, url_token: str, *, organization_id: Optional[str] = None) -> DashboardOauthAuthorizationRequestsRejectOutput:
        """
    Reject OAuth authorization request
    Reject an oauth authorization request

    :param url_token: str
    :param organization_id: Optional[str] (optional)
    :return: DashboardOauthAuthorizationRequestsRejectOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if organization_id is not None:
            body_dict["organization_id"] = organization_id

        request = MetorialRequest(
            path=['dashboard', 'oauth', 'authorization-requests', url_token, 'reject'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOauthAuthorizationRequestsRejectOutput.from_dict)