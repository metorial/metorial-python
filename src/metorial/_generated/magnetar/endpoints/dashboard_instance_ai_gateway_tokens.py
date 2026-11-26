from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayTokensListOutput, DashboardInstanceAiGatewayTokensListOutput, mapDashboardInstanceAiGatewayTokensListQuery, DashboardInstanceAiGatewayTokensListQuery, mapDashboardInstanceAiGatewayTokensGetOutput, DashboardInstanceAiGatewayTokensGetOutput, mapDashboardInstanceAiGatewayTokensCreateOutput, DashboardInstanceAiGatewayTokensCreateOutput, mapDashboardInstanceAiGatewayTokensCreateBody, DashboardInstanceAiGatewayTokensCreateBody, mapDashboardInstanceAiGatewayTokensUpdateOutput, DashboardInstanceAiGatewayTokensUpdateOutput, mapDashboardInstanceAiGatewayTokensUpdateBody, DashboardInstanceAiGatewayTokensUpdateBody, mapDashboardInstanceAiGatewayTokensRevokeOutput, DashboardInstanceAiGatewayTokensRevokeOutput

class MetorialDashboardInstanceAiGatewayTokensEndpoint(BaseMetorialEndpoint):
    """API keys for the AI gateway. Each token can be limited to certain models and given its own rate and spend limits."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, consumer_id: Optional[str] = None) -> DashboardInstanceAiGatewayTokensListOutput:
        """
    List AI gateway tokens
    Returns a paginated list of tokens, including revoked ones.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param consumer_id: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayTokensListOutput
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
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'tokens'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayTokensListOutput.from_dict)

    def get(self, instance_id: str, token_id: str) -> DashboardInstanceAiGatewayTokensGetOutput:
        """
    Get AI gateway token
    Retrieves a token by ID. The secret is never returned again.

    :param instance_id: str
    :param token_id: str
    :return: DashboardInstanceAiGatewayTokensGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'tokens', token_id]
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayTokensGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, consumer_id: Optional[str] = None, allowed_models: Optional[List[str]] = None, limits: Optional[List[Dict[str, Any]]] = None, metadata: Optional[Dict[str, str]] = None, expires_at: Optional[datetime] = None) -> DashboardInstanceAiGatewayTokensCreateOutput:
        """
    Create AI gateway token
    Creates a token. The response contains the secret, which is shown only this once.

    :param instance_id: str
    :param name: str
    :param consumer_id: Optional[str] (optional)
    :param allowed_models: Optional[List[str]] (optional)
    :param limits: Optional[List[Dict[str, Any]]] (optional)
    :param metadata: Optional[Dict[str, str]] (optional)
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardInstanceAiGatewayTokensCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if consumer_id is not None:
            body_dict["consumer_id"] = consumer_id
        if allowed_models is not None:
            body_dict["allowed_models"] = allowed_models
        if limits is not None:
            body_dict["limits"] = limits
        if metadata is not None:
            body_dict["metadata"] = metadata
        if expires_at is not None:
            body_dict["expires_at"] = expires_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'tokens'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayTokensCreateOutput.from_dict)

    def update(self, instance_id: str, token_id: str, *, name: Optional[str] = None, allowed_models: Optional[List[str]] = None, limits: Optional[List[Dict[str, Any]]] = None, metadata: Optional[Dict[str, str]] = None, expires_at: Optional[datetime] = None) -> DashboardInstanceAiGatewayTokensUpdateOutput:
        """
    Update AI gateway token
    Updates the name, allowed models, limits, metadata or expiry of a token.

    :param instance_id: str
    :param token_id: str
    :param name: Optional[str] (optional)
    :param allowed_models: Optional[List[str]] (optional)
    :param limits: Optional[List[Dict[str, Any]]] (optional)
    :param metadata: Optional[Dict[str, str]] (optional)
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardInstanceAiGatewayTokensUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if allowed_models is not None:
            body_dict["allowed_models"] = allowed_models
        if limits is not None:
            body_dict["limits"] = limits
        if metadata is not None:
            body_dict["metadata"] = metadata
        if expires_at is not None:
            body_dict["expires_at"] = expires_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'tokens', token_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceAiGatewayTokensUpdateOutput.from_dict)

    def revoke(self, instance_id: str, token_id: str) -> DashboardInstanceAiGatewayTokensRevokeOutput:
        """
    Revoke AI gateway token
    Revokes a token. Requests made with it are rejected from then on.

    :param instance_id: str
    :param token_id: str
    :return: DashboardInstanceAiGatewayTokensRevokeOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'tokens', token_id, 'revoke']
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayTokensRevokeOutput.from_dict)