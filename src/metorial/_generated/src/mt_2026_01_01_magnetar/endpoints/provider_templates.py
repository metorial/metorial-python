from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderTemplatesListOutput, DashboardInstanceProviderTemplatesListOutput, mapDashboardInstanceProviderTemplatesListQuery, DashboardInstanceProviderTemplatesListQuery, mapDashboardInstanceProviderTemplatesGetOutput, DashboardInstanceProviderTemplatesGetOutput, mapDashboardInstanceProviderTemplatesCreateOutput, DashboardInstanceProviderTemplatesCreateOutput, mapDashboardInstanceProviderTemplatesCreateBody, DashboardInstanceProviderTemplatesCreateBody, mapDashboardInstanceProviderTemplatesUpdateOutput, DashboardInstanceProviderTemplatesUpdateOutput, mapDashboardInstanceProviderTemplatesUpdateBody, DashboardInstanceProviderTemplatesUpdateBody, mapDashboardInstanceProviderTemplatesDeleteOutput, DashboardInstanceProviderTemplatesDeleteOutput

class MetorialProviderTemplatesEndpoint(BaseMetorialEndpoint):
    """Provider templates are reusable, consumer-facing wrappers around provider deployments."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderTemplatesListOutput:
        """
    List provider templates
    Returns a paginated list of provider templates.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProviderTemplatesListOutput
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
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['provider-templates'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderTemplatesListOutput.from_dict)

    def get(self, provider_template_id: str) -> DashboardInstanceProviderTemplatesGetOutput:
        """
    Get provider template
    Retrieves a specific provider template.

    :param provider_template_id: str
    :return: DashboardInstanceProviderTemplatesGetOutput
    """
        request = MetorialRequest(
            path=['provider-templates', provider_template_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderTemplatesGetOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_deployment_id: str = None, provider_deployment: Dict[str, Any] = None) -> DashboardInstanceProviderTemplatesCreateOutput:
        """
    Create provider template
    Creates a new provider template from an existing provider deployment or creates a minimal backing deployment first.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_deployment_id: str (optional)
    :param provider_deployment: Dict[str, Any] (optional)
    :return: DashboardInstanceProviderTemplatesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_deployment is not None:
            body_dict["provider_deployment"] = provider_deployment

        request = MetorialRequest(
            path=['provider-templates'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderTemplatesCreateOutput.from_dict)

    def update(self, provider_template_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderTemplatesUpdateOutput:
        """
    Update provider template
    Updates an existing provider template.

    :param provider_template_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderTemplatesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['provider-templates', provider_template_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderTemplatesUpdateOutput.from_dict)

    def delete(self, provider_template_id: str) -> DashboardInstanceProviderTemplatesDeleteOutput:
        """
    Archive provider template
    Archives an existing provider template.

    :param provider_template_id: str
    :return: DashboardInstanceProviderTemplatesDeleteOutput
    """
        request = MetorialRequest(
            path=['provider-templates', provider_template_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderTemplatesDeleteOutput.from_dict)