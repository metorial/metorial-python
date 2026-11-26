from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayModelsListOutput, DashboardInstanceAiGatewayModelsListOutput, mapDashboardInstanceAiGatewayModelsListQuery, DashboardInstanceAiGatewayModelsListQuery, mapDashboardInstanceAiGatewayModelsGetOutput, DashboardInstanceAiGatewayModelsGetOutput, mapDashboardInstanceAiGatewayModelsResolveOutput, DashboardInstanceAiGatewayModelsResolveOutput, mapDashboardInstanceAiGatewayModelsResolveBody, DashboardInstanceAiGatewayModelsResolveBody

class MetorialManagementInstanceAiGatewayModelsEndpoint(BaseMetorialEndpoint):
    """The models in the AI gateway catalog, with their capabilities and limits. The catalog is shared by all instances and kept up to date by Metorial."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, lab: Optional[str] = None, kind: Optional[str] = None, search: Optional[str] = None) -> DashboardInstanceAiGatewayModelsListOutput:
        """
    List AI gateway models
    Returns a paginated list of the models in the catalog that are not retired.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param lab: Optional[str] (optional)
    :param kind: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayModelsListOutput
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
        if lab is not None:
            query_dict["lab"] = lab
        if kind is not None:
            query_dict["kind"] = kind
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'models'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayModelsListOutput.from_dict)

    def get(self, instance_id: str, model_id: str) -> DashboardInstanceAiGatewayModelsGetOutput:
        """
    Get AI gateway model
    Retrieves a model by ID or slug. URL-encode the slash of a slug, e.g. anthropic%2Fclaude-sonnet-4.

    :param instance_id: str
    :param model_id: str
    :return: DashboardInstanceAiGatewayModelsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'models', model_id]
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayModelsGetOutput.from_dict)

    def resolve(self, instance_id: str, *, model: str) -> DashboardInstanceAiGatewayModelsResolveOutput:
        """
    Resolve AI gateway model
    Finds the catalog model a model string refers to, the same way the gateway does for requests. Accepts slugs, names providers use for a model, and provider-pinned names like openai:gpt-4o.

    :param instance_id: str
    :param model: str
    :return: DashboardInstanceAiGatewayModelsResolveOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["model"] = model

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'models', 'resolve'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayModelsResolveOutput.from_dict)