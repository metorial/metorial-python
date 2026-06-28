from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderTemplatesListOutput, DashboardInstanceProviderTemplatesListOutput, mapDashboardInstanceProviderTemplatesListQuery, DashboardInstanceProviderTemplatesListQuery, mapDashboardInstanceProviderTemplatesGetOutput, DashboardInstanceProviderTemplatesGetOutput, mapDashboardInstanceProviderTemplatesCreateOutput, DashboardInstanceProviderTemplatesCreateOutput, mapDashboardInstanceProviderTemplatesCreateBody, DashboardInstanceProviderTemplatesCreateBody, mapDashboardInstanceProviderTemplatesUpdateOutput, DashboardInstanceProviderTemplatesUpdateOutput, mapDashboardInstanceProviderTemplatesUpdateBody, DashboardInstanceProviderTemplatesUpdateBody, mapDashboardInstanceProviderTemplatesDeleteOutput, DashboardInstanceProviderTemplatesDeleteOutput

class MetorialProviderTemplatesEndpoint(BaseMetorialEndpoint):
    """Provider templates are reusable, consumer-facing wrappers around integrations."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderTemplatesListOutput:
        """
    List provider templates
    Returns a paginated list of provider templates.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
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
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
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

    def create(self, *, name: str, integration_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderTemplatesCreateOutput:
        """
    Create provider template
    Creates a new provider template from an existing integration.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param integration_id: str
    :return: DashboardInstanceProviderTemplatesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["integration_id"] = integration_id

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