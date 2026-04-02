from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsListOutput, DashboardInstanceProviderDeploymentsListOutput, mapDashboardInstanceProviderDeploymentsListQuery, DashboardInstanceProviderDeploymentsListQuery, mapDashboardInstanceProviderDeploymentsGetOutput, DashboardInstanceProviderDeploymentsGetOutput, mapDashboardInstanceProviderDeploymentsCreateOutput, DashboardInstanceProviderDeploymentsCreateOutput, mapDashboardInstanceProviderDeploymentsCreateBody, DashboardInstanceProviderDeploymentsCreateBody, mapDashboardInstanceProviderDeploymentsUpdateOutput, DashboardInstanceProviderDeploymentsUpdateOutput, mapDashboardInstanceProviderDeploymentsUpdateBody, DashboardInstanceProviderDeploymentsUpdateBody, mapDashboardInstanceProviderDeploymentsDeleteOutput, DashboardInstanceProviderDeploymentsDeleteOutput

class MetorialProviderDeploymentsEndpoint(BaseMetorialEndpoint):
    """A deployment is a running instance of a provider, pinned to a specific version. Deployments support custom configuration values and user authentication."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_version_id: Optional[Union[str, List[str]]] = None, actor_id: Optional[Union[str, List[str]]] = None, consumer_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, identity_credential_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsListOutput:
        """
    List provider deployments
    Returns a paginated list of provider deployments.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_version_id: Optional[Union[str, List[str]]] (optional)
    :param actor_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param identity_credential_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsListOutput
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
        if provider_version_id is not None:
            query_dict["provider_version_id"] = provider_version_id
        if actor_id is not None:
            query_dict["actor_id"] = actor_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if identity_credential_id is not None:
            query_dict["identity_credential_id"] = identity_credential_id
        if status is not None:
            query_dict["status"] = status
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['provider-deployments'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsListOutput.from_dict)

    def get(self, provider_deployment_id: str) -> DashboardInstanceProviderDeploymentsGetOutput:
        """
    Get provider deployment
    Retrieves a specific provider deployment by ID.

    :param provider_deployment_id: str
    :return: DashboardInstanceProviderDeploymentsGetOutput
    """
        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsGetOutput.from_dict)

    def create(self, *, provider_id: str, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None, locked_provider_version_id: Optional[str] = None, provider_config_id: Optional[str] = None, provider_config: Optional[Union[Dict[str, Any], Dict[str, Any]]] = None) -> DashboardInstanceProviderDeploymentsCreateOutput:
        """
    Create provider deployment
    Creates a new provider deployment.

    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :param provider_id: str
    :param locked_provider_version_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param provider_config: Optional[Union[Dict[str, Any], Dict[str, Any]]] (optional)
    :return: DashboardInstanceProviderDeploymentsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters
        body_dict["provider_id"] = provider_id
        if locked_provider_version_id is not None:
            body_dict["locked_provider_version_id"] = locked_provider_version_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if provider_config is not None:
            body_dict["provider_config"] = provider_config

        request = MetorialRequest(
            path=['provider-deployments'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsCreateOutput.from_dict)

    def update(self, provider_deployment_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceProviderDeploymentsUpdateOutput:
        """
    Update provider deployment
    Updates a specific provider deployment.

    :param provider_deployment_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceProviderDeploymentsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsUpdateOutput.from_dict)

    def delete(self, provider_deployment_id: str) -> DashboardInstanceProviderDeploymentsDeleteOutput:
        """
    Delete provider deployment
    Permanently deletes a provider deployment.

    :param provider_deployment_id: str
    :return: DashboardInstanceProviderDeploymentsDeleteOutput
    """
        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsDeleteOutput.from_dict)