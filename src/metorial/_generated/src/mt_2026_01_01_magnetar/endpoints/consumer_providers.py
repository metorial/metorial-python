from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerProvidersListOutput, ConsumerProvidersListOutput, mapConsumerProvidersListQuery, ConsumerProvidersListQuery, mapConsumerProvidersGetOutput, ConsumerProvidersGetOutput, mapConsumerProvidersRequestAccessOutput, ConsumerProvidersRequestAccessOutput, mapConsumerProvidersRequestAccessBody, ConsumerProvidersRequestAccessBody, mapConsumerProvidersSetupOutput, ConsumerProvidersSetupOutput, mapConsumerProvidersSetupBody, ConsumerProvidersSetupBody, mapConsumerProvidersGetSetupOutput, ConsumerProvidersGetSetupOutput, mapConsumerProvidersDeployOutput, ConsumerProvidersDeployOutput, mapConsumerProvidersDeployBody, ConsumerProvidersDeployBody

class MetorialConsumerProvidersEndpoint(BaseMetorialEndpoint):
    """Browse and configure portal providers from the consumer side."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, provider_group_id: Optional[str] = None) -> ConsumerProvidersListOutput:
        """
    List consumer providers
    Returns the unified portal catalog with consumer availability.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param provider_group_id: Optional[str] (optional)
    :return: ConsumerProvidersListOutput
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
        if search is not None:
            query_dict["search"] = search
        if provider_group_id is not None:
            query_dict["provider_group_id"] = provider_group_id

        request = MetorialRequest(
            path=['consumer', 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerProvidersListOutput.from_dict)

    def get(self, catalog_item_id: str) -> ConsumerProvidersGetOutput:
        """
    Get consumer provider
    Returns one portal catalog item with any available setup capability data.

    :param catalog_item_id: str
    :return: ConsumerProvidersGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'providers', catalog_item_id]
        )
        return self._get(request).transform(mapConsumerProvidersGetOutput.from_dict)

    def request_access(self, catalog_item_id: str, *, message: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> ConsumerProvidersRequestAccessOutput:
        """
    Request consumer provider access
    Creates an access request for a portal catalog item.

    :param catalog_item_id: str
    :param message: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: ConsumerProvidersRequestAccessOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if message is not None:
            body_dict["message"] = message
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['consumer', 'providers', catalog_item_id, 'request-access'],
            body=body_dict
        )
        return self._post(request).transform(mapConsumerProvidersRequestAccessOutput.from_dict)

    def setup(self, catalog_item_id: str, *, provider_auth_method_id: Optional[str] = None) -> ConsumerProvidersSetupOutput:
        """
    Start consumer provider setup
    Starts an integration setup flow for a portal provider template.

    :param catalog_item_id: str
    :param provider_auth_method_id: Optional[str] (optional)
    :return: ConsumerProvidersSetupOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if provider_auth_method_id is not None:
            body_dict["provider_auth_method_id"] = provider_auth_method_id

        request = MetorialRequest(
            path=['consumer', 'providers', catalog_item_id, 'setup'],
            body=body_dict
        )
        return self._post(request).transform(mapConsumerProvidersSetupOutput.from_dict)

    def get_setup(self, catalog_item_id: str, provider_setup_session_id: str) -> ConsumerProvidersGetSetupOutput:
        """
    Get consumer provider setup
    Reads the status of an integration setup flow for a portal provider template.

    :param catalog_item_id: str
    :param provider_setup_session_id: str
    :return: ConsumerProvidersGetSetupOutput
    """
        request = MetorialRequest(
            path=['consumer', 'providers', catalog_item_id, 'setup', provider_setup_session_id]
        )
        return self._get(request).transform(mapConsumerProvidersGetSetupOutput.from_dict)

    def deploy(self, catalog_item_id: str, *, integration_setup_session_id: str, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> ConsumerProvidersDeployOutput:
        """
    Deploy consumer provider
    Creates an owned Magic MCP server from a portal provider template.

    :param catalog_item_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param integration_setup_session_id: str
    :return: ConsumerProvidersDeployOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["integration_setup_session_id"] = integration_setup_session_id

        request = MetorialRequest(
            path=['consumer', 'providers', catalog_item_id, 'deploy'],
            body=body_dict
        )
        return self._post(request).transform(mapConsumerProvidersDeployOutput.from_dict)