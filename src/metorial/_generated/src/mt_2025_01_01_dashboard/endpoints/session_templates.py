from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionTemplatesListOutput, DashboardInstanceSessionTemplatesListOutput, mapDashboardInstanceSessionTemplatesListQuery, DashboardInstanceSessionTemplatesListQuery, mapDashboardInstanceSessionTemplatesGetOutput, DashboardInstanceSessionTemplatesGetOutput, mapDashboardInstanceSessionTemplatesCreateOutput, DashboardInstanceSessionTemplatesCreateOutput, mapDashboardInstanceSessionTemplatesCreateBody, DashboardInstanceSessionTemplatesCreateBody, mapDashboardInstanceSessionTemplatesUpdateOutput, DashboardInstanceSessionTemplatesUpdateOutput, mapDashboardInstanceSessionTemplatesUpdateBody, DashboardInstanceSessionTemplatesUpdateBody

class MetorialSessionTemplatesEndpoint(BaseMetorialEndpoint):
    """Session templates define reusable configurations for sessions, including which providers to include. Templates can be used to quickly create new sessions with consistent settings."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionTemplatesListOutput:
        """
    List session templates
    Returns a paginated list of session templates.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionTemplatesListOutput
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
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id

        request = MetorialRequest(
            path=['session-templates'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionTemplatesListOutput.from_dict)

    def get(self, session_template_id: str) -> DashboardInstanceSessionTemplatesGetOutput:
        """
    Get session template
    Retrieves a specific session template by ID.

    :param session_template_id: str
    :return: DashboardInstanceSessionTemplatesGetOutput
    """
        request = MetorialRequest(
            path=['session-templates', session_template_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionTemplatesGetOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, providers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceSessionTemplatesCreateOutput:
        """
    Create session template
    Creates a new session template.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param providers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceSessionTemplatesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if providers is not None:
            body_dict["providers"] = providers

        request = MetorialRequest(
            path=['session-templates'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSessionTemplatesCreateOutput.from_dict)

    def update(self, session_template_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionTemplatesUpdateOutput:
        """
    Update session template
    Updates a specific session template.

    :param session_template_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionTemplatesUpdateOutput
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
            path=['session-templates', session_template_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionTemplatesUpdateOutput.from_dict)
