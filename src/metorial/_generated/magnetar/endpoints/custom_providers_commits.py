from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersCommitsListOutput, DashboardInstanceCustomProvidersCommitsListOutput, mapDashboardInstanceCustomProvidersCommitsListQuery, DashboardInstanceCustomProvidersCommitsListQuery, mapDashboardInstanceCustomProvidersCommitsGetOutput, DashboardInstanceCustomProvidersCommitsGetOutput, mapDashboardInstanceCustomProvidersCommitsCreateOutput, DashboardInstanceCustomProvidersCommitsCreateOutput, mapDashboardInstanceCustomProvidersCommitsCreateBody, DashboardInstanceCustomProvidersCommitsCreateBody

class MetorialCustomProvidersCommitsEndpoint(BaseMetorialEndpoint):
    """Commits represent version promotions between environments. Merge versions from one environment to another or rollback to a previous version."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, custom_provider_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, ids: Optional[Union[str, List[str]]] = None, custom_provider_version_ids: Optional[Union[str, List[str]]] = None, custom_provider_environment_ids: Optional[Union[str, List[str]]] = None) -> DashboardInstanceCustomProvidersCommitsListOutput:
        """
    List custom provider commits
    Returns a paginated list of commits for a custom provider.

    :param custom_provider_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param ids: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_version_ids: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_environment_ids: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCustomProvidersCommitsListOutput
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
        if ids is not None:
            query_dict["ids"] = ids
        if custom_provider_version_ids is not None:
            query_dict["custom_provider_version_ids"] = custom_provider_version_ids
        if custom_provider_environment_ids is not None:
            query_dict["custom_provider_environment_ids"] = custom_provider_environment_ids

        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'commits'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersCommitsListOutput.from_dict)

    def get(self, custom_provider_id: str, custom_provider_commit_id: str) -> DashboardInstanceCustomProvidersCommitsGetOutput:
        """
    Get custom provider commit
    Retrieves a specific commit.

    :param custom_provider_id: str
    :param custom_provider_commit_id: str
    :return: DashboardInstanceCustomProvidersCommitsGetOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'commits', custom_provider_commit_id]
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersCommitsGetOutput.from_dict)

    def create(self, custom_provider_id: str, *, message: str, action: Union[Dict[str, Any], Dict[str, Any]]) -> DashboardInstanceCustomProvidersCommitsCreateOutput:
        """
    Create custom provider commit
    Creates a new commit to promote or rollback a version in an environment.

    :param custom_provider_id: str
    :param message: str
    :param action: Union[Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstanceCustomProvidersCommitsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["message"] = message
        body_dict["action"] = action

        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'commits'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCustomProvidersCommitsCreateOutput.from_dict)
