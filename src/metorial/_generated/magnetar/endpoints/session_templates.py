from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionTemplatesListOutput, DashboardInstanceSessionTemplatesListOutput, mapDashboardInstanceSessionTemplatesListQuery, DashboardInstanceSessionTemplatesListQuery, mapDashboardInstanceSessionTemplatesGetOutput, DashboardInstanceSessionTemplatesGetOutput, mapDashboardInstanceSessionTemplatesCreateOutput, DashboardInstanceSessionTemplatesCreateOutput, mapDashboardInstanceSessionTemplatesCreateBody, DashboardInstanceSessionTemplatesCreateBody, mapDashboardInstanceSessionTemplatesUpdateOutput, DashboardInstanceSessionTemplatesUpdateOutput, mapDashboardInstanceSessionTemplatesUpdateBody, DashboardInstanceSessionTemplatesUpdateBody

class MetorialSessionTemplatesEndpoint(BaseMetorialEndpoint):
    """Session templates define reusable configurations for sessions, including which providers to include. Templates can be used to quickly create new sessions with consistent settings."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSessionTemplatesListOutput:
        """
    List session templates
    Returns a paginated list of session templates.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
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
