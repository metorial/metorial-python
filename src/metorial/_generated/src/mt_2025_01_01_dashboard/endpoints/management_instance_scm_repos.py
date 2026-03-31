from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceScmReposListOutput, DashboardInstanceScmReposListOutput, mapDashboardInstanceScmReposListQuery, DashboardInstanceScmReposListQuery, mapDashboardInstanceScmReposGetOutput, DashboardInstanceScmReposGetOutput, mapDashboardInstanceScmReposPreviewOutput, DashboardInstanceScmReposPreviewOutput, mapDashboardInstanceScmReposPreviewBody, DashboardInstanceScmReposPreviewBody, mapDashboardInstanceScmReposCreateOutput, DashboardInstanceScmReposCreateOutput, mapDashboardInstanceScmReposCreateBody, DashboardInstanceScmReposCreateBody

class MetorialManagementInstanceScmReposEndpoint(BaseMetorialEndpoint):
    """Manage source control repositories."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceScmReposListOutput:
        """
    List SCM repos
    Returns a paginated list of SCM repositories.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceScmReposListOutput
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
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'scm', 'repos'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceScmReposListOutput.from_dict)

    def get(self, instance_id: str, scm_repository_id: str) -> DashboardInstanceScmReposGetOutput:
        """
    Get SCM repo
    Retrieves a specific SCM repository by ID.

    :param instance_id: str
    :param scm_repository_id: str
    :return: DashboardInstanceScmReposGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'scm', 'repos', scm_repository_id]
        )
        return self._get(request).transform(mapDashboardInstanceScmReposGetOutput.from_dict)

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

    def create(self, instance_id: str, *, installation_id: str, external_repo_id: str = None, external_account_id: str = None, name: str = None, is_private: Optional[bool] = None) -> DashboardInstanceScmReposCreateOutput:
        """
    Create SCM repo
    Links or creates a repository in an SCM installation.

    :param instance_id: str
    :param installation_id: str
    :param external_repo_id: str (optional)
    :param external_account_id: str (optional)
    :param name: str (optional)
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