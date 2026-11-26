from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayVirtualModelsListOutput, DashboardInstanceAiGatewayVirtualModelsListOutput, mapDashboardInstanceAiGatewayVirtualModelsListQuery, DashboardInstanceAiGatewayVirtualModelsListQuery, mapDashboardInstanceAiGatewayVirtualModelsGetOutput, DashboardInstanceAiGatewayVirtualModelsGetOutput, mapDashboardInstanceAiGatewayVirtualModelsCreateOutput, DashboardInstanceAiGatewayVirtualModelsCreateOutput, mapDashboardInstanceAiGatewayVirtualModelsCreateBody, DashboardInstanceAiGatewayVirtualModelsCreateBody, mapDashboardInstanceAiGatewayVirtualModelsCreateFromTemplateOutput, DashboardInstanceAiGatewayVirtualModelsCreateFromTemplateOutput, mapDashboardInstanceAiGatewayVirtualModelsCreateFromTemplateBody, DashboardInstanceAiGatewayVirtualModelsCreateFromTemplateBody, mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutput, DashboardInstanceAiGatewayVirtualModelsTestDraftOutput, mapDashboardInstanceAiGatewayVirtualModelsTestDraftBody, DashboardInstanceAiGatewayVirtualModelsTestDraftBody, mapDashboardInstanceAiGatewayVirtualModelsUpdateOutput, DashboardInstanceAiGatewayVirtualModelsUpdateOutput, mapDashboardInstanceAiGatewayVirtualModelsUpdateBody, DashboardInstanceAiGatewayVirtualModelsUpdateBody, mapDashboardInstanceAiGatewayVirtualModelsDeleteOutput, DashboardInstanceAiGatewayVirtualModelsDeleteOutput, mapDashboardInstanceAiGatewayVirtualModelsRollbackOutput, DashboardInstanceAiGatewayVirtualModelsRollbackOutput, mapDashboardInstanceAiGatewayVirtualModelsRollbackBody, DashboardInstanceAiGatewayVirtualModelsRollbackBody, mapDashboardInstanceAiGatewayVirtualModelsTestOutput, DashboardInstanceAiGatewayVirtualModelsTestOutput, mapDashboardInstanceAiGatewayVirtualModelsTestBody, DashboardInstanceAiGatewayVirtualModelsTestBody, mapDashboardInstanceAiGatewayVirtualModelsReplayOutput, DashboardInstanceAiGatewayVirtualModelsReplayOutput, mapDashboardInstanceAiGatewayVirtualModelsReplayBody, DashboardInstanceAiGatewayVirtualModelsReplayBody

class MetorialAiGatewayVirtualModelsEndpoint(BaseMetorialEndpoint):
    """Virtual models are model names that pick a real model for every request, using rules, optional signals answered by a decision model, a default, and stickiness. Every change to the definition creates a new version."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceAiGatewayVirtualModelsListOutput:
        """
    List AI gateway virtual models
    Returns a paginated list of virtual models.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsListOutput
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
            path=['ai-gateway', 'virtual-models'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayVirtualModelsListOutput.from_dict)

    def get(self, virtual_model_id: str) -> DashboardInstanceAiGatewayVirtualModelsGetOutput:
        """
    Get AI gateway virtual model
    Retrieves a virtual model by ID or slug, with its current definition.

    :param virtual_model_id: str
    :return: DashboardInstanceAiGatewayVirtualModelsGetOutput
    """
        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', virtual_model_id]
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayVirtualModelsGetOutput.from_dict)

    def create(self, *, slug: str, name: str, definition: Dict[str, Any], description: Optional[str] = None) -> DashboardInstanceAiGatewayVirtualModelsCreateOutput:
        """
    Create AI gateway virtual model
    Creates a virtual model with its first version. Requests that use its slug as the model are routed by the definition.

    :param slug: str
    :param name: str
    :param description: Optional[str] (optional)
    :param definition: Dict[str, Any]
    :return: DashboardInstanceAiGatewayVirtualModelsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["slug"] = slug
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        body_dict["definition"] = definition

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayVirtualModelsCreateOutput.from_dict)

    def create_from_template(self, *, template: str, slug: str, name: str, parameters: Dict[str, str], description: Optional[str] = None, decision_connection_id: Optional[str] = None) -> DashboardInstanceAiGatewayVirtualModelsCreateFromTemplateOutput:
        """
    Create AI gateway virtual model from template
    Creates a virtual model from a template, filling in the models it asks for. The definition can be changed afterwards like any other.

    :param template: str
    :param slug: str
    :param name: str
    :param description: Optional[str] (optional)
    :param parameters: Dict[str, str]
    :param decision_connection_id: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsCreateFromTemplateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["template"] = template
        body_dict["slug"] = slug
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        body_dict["parameters"] = parameters
        if decision_connection_id is not None:
            body_dict["decision_connection_id"] = decision_connection_id

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', 'from-template'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayVirtualModelsCreateFromTemplateOutput.from_dict)

    def test_draft(self, *, definition: Dict[str, Any], dialect: str, request: Dict[str, Any], token_id: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutput:
        """
    Test AI gateway virtual model draft
    Routes a request through an unsaved definition and shows which rule and models it picks. Nothing is sent to a provider, but the decision model is called and billed when a rule reads signals.

    :param definition: Dict[str, Any]
    :param token_id: Optional[str] (optional)
    :param dialect: str
    :param request: Dict[str, Any]
    :param metadata: Optional[Dict[str, str]] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsTestDraftOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["definition"] = definition
        if token_id is not None:
            body_dict["token_id"] = token_id
        body_dict["dialect"] = dialect
        body_dict["request"] = request
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', 'test'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutput.from_dict)

    def update(self, virtual_model_id: str, *, name: Optional[str] = None, description: Optional[str] = None, definition: Optional[Dict[str, Any]] = None) -> DashboardInstanceAiGatewayVirtualModelsUpdateOutput:
        """
    Update AI gateway virtual model
    Updates the name, description or definition of a virtual model. A new definition becomes a new version and takes effect right away.

    :param virtual_model_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param definition: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if definition is not None:
            body_dict["definition"] = definition

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', virtual_model_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceAiGatewayVirtualModelsUpdateOutput.from_dict)

    def delete(self, virtual_model_id: str) -> DashboardInstanceAiGatewayVirtualModelsDeleteOutput:
        """
    Delete AI gateway virtual model
    Deletes a virtual model. Requests that use its slug are no longer routed by it, and the slug can be used again.

    :param virtual_model_id: str
    :return: DashboardInstanceAiGatewayVirtualModelsDeleteOutput
    """
        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', virtual_model_id]
        )
        return self._delete(request).transform(mapDashboardInstanceAiGatewayVirtualModelsDeleteOutput.from_dict)

    def rollback(self, virtual_model_id: str, *, version_id: str) -> DashboardInstanceAiGatewayVirtualModelsRollbackOutput:
        """
    Roll back AI gateway virtual model
    Makes an earlier version's definition current again, as a new version. The version history is kept.

    :param virtual_model_id: str
    :param version_id: str
    :return: DashboardInstanceAiGatewayVirtualModelsRollbackOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["version_id"] = version_id

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', virtual_model_id, 'rollback'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayVirtualModelsRollbackOutput.from_dict)

    def test(self, virtual_model_id: str, *, dialect: str, request: Dict[str, Any], definition: Optional[Dict[str, Any]] = None, token_id: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> DashboardInstanceAiGatewayVirtualModelsTestOutput:
        """
    Test AI gateway virtual model
    Routes a request through the virtual model and shows which rule and models it picks. Nothing is sent to a provider, but the decision model is called and billed when a rule reads signals.

    :param virtual_model_id: str
    :param definition: Optional[Dict[str, Any]] (optional)
    :param token_id: Optional[str] (optional)
    :param dialect: str
    :param request: Dict[str, Any]
    :param metadata: Optional[Dict[str, str]] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsTestOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if definition is not None:
            body_dict["definition"] = definition
        if token_id is not None:
            body_dict["token_id"] = token_id
        body_dict["dialect"] = dialect
        body_dict["request"] = request
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', virtual_model_id, 'test'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayVirtualModelsTestOutput.from_dict)

    def replay(self, virtual_model_id: str, *, definition: Optional[Dict[str, Any]] = None, limit: Optional[float] = None) -> DashboardInstanceAiGatewayVirtualModelsReplayOutput:
        """
    Replay AI gateway virtual model requests
    Routes the virtual model's most recent logged requests again, through the current definition or a draft, and shows which would be routed differently. Only requests whose content was logged are replayed. Logged decision model answers are reused while the signals are unchanged; otherwise the decision model is called and billed.

    :param virtual_model_id: str
    :param definition: Optional[Dict[str, Any]] (optional)
    :param limit: Optional[float] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsReplayOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if definition is not None:
            body_dict["definition"] = definition
        if limit is not None:
            body_dict["limit"] = limit

        request = MetorialRequest(
            path=['ai-gateway', 'virtual-models', virtual_model_id, 'replay'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayVirtualModelsReplayOutput.from_dict)