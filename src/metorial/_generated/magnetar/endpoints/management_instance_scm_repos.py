from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceScmReposPreviewOutput, DashboardInstanceScmReposPreviewOutput, mapDashboardInstanceScmReposPreviewBody, DashboardInstanceScmReposPreviewBody, mapDashboardInstanceScmReposCreateOutput, DashboardInstanceScmReposCreateOutput, mapDashboardInstanceScmReposCreateBody, DashboardInstanceScmReposCreateBody

class MetorialManagementInstanceScmReposEndpoint(BaseMetorialEndpoint):
    """Manage source control repositories."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def preview(self, instance_id: str, *, installation_id: str, external_account_id: Optional[str] = None) -> DashboardInstanceScmReposPreviewOutput:
        """
    Preview SCM repos
    Lists available repositories from an SCM installation.

    :param instance_id: str
    :param installation_id: str
    :param external_account_id: Optional[str] (optional)
    :return: DashboardInstanceScmReposPreviewOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["installation_id"] = installation_id
        if external_account_id is not None:
            body_dict["external_account_id"] = external_account_id

        request = MetorialRequest(
            path=['instances', instance_id, 'scm', 'repos', 'preview'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceScmReposPreviewOutput.from_dict)

    def create(self, instance_id: str, *, installation_id: str, external_repo_id: Optional[str] = None, external_account_id: Optional[str] = None, name: Optional[str] = None, is_private: Optional[bool] = None) -> DashboardInstanceScmReposCreateOutput:
        """
    Create SCM repo
    Links or creates a repository in an SCM installation.

    :param instance_id: str
    :param installation_id: str
    :param external_repo_id: Optional[str] (optional)
    :param external_account_id: Optional[str] (optional)
    :param name: Optional[str] (optional)
    :param is_private: Optional[bool] (optional)
    :return: DashboardInstanceScmReposCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["installation_id"] = installation_id
        if external_repo_id is not None:
            body_dict["external_repo_id"] = external_repo_id
        if external_account_id is not None:
            body_dict["external_account_id"] = external_account_id
        if name is not None:
            body_dict["name"] = name
        if is_private is not None:
            body_dict["is_private"] = is_private

        request = MetorialRequest(
            path=['instances', instance_id, 'scm', 'repos'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceScmReposCreateOutput.from_dict)
