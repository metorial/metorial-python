from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceScmAccountsPreviewOutput, DashboardInstanceScmAccountsPreviewOutput, mapDashboardInstanceScmAccountsPreviewBody, DashboardInstanceScmAccountsPreviewBody

class MetorialDashboardInstanceScmAccountsEndpoint(BaseMetorialEndpoint):
    """Preview SCM accounts from an installation."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def preview(self, instance_id: str, *, installation_id: str) -> DashboardInstanceScmAccountsPreviewOutput:
        """
    Preview SCM accounts
    Lists available accounts from an SCM installation.

    :param instance_id: str
    :param installation_id: str
    :return: DashboardInstanceScmAccountsPreviewOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["installation_id"] = installation_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'scm', 'accounts', 'preview'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceScmAccountsPreviewOutput.from_dict)
