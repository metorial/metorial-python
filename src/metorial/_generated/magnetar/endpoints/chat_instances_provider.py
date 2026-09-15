from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatInstancesProviderGetOutput, DashboardInstanceChatInstancesProviderGetOutput, mapDashboardInstanceChatInstancesProviderSetOutput, DashboardInstanceChatInstancesProviderSetOutput, mapDashboardInstanceChatInstancesProviderSetBody, DashboardInstanceChatInstancesProviderSetBody, mapDashboardInstanceChatInstancesProviderAuthenticatedUserOutput, DashboardInstanceChatInstancesProviderAuthenticatedUserOutput

class MetorialChatInstancesProviderEndpoint(BaseMetorialEndpoint):
    """Chat instances materialize a chat connection for a specific runtime configuration."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, chat_instance_id: str) -> DashboardInstanceChatInstancesProviderGetOutput:
        """
    Get chat instance provider
    Retrieves the single provider configured for a chat instance.

    :param chat_instance_id: str
    :return: DashboardInstanceChatInstancesProviderGetOutput
    """
        request = MetorialRequest(
            path=['chat', 'instances', chat_instance_id, 'provider']
        )
        return self._get(request).transform(mapDashboardInstanceChatInstancesProviderGetOutput.from_dict)

    def set(self, chat_instance_id: str, *, provider_id: str, provider_deployment_id: Optional[str] = None, provider_config_id: Optional[str] = None, provider_auth_config_id: Optional[str] = None) -> DashboardInstanceChatInstancesProviderSetOutput:
        """
    Set chat instance provider
    Creates or updates the single provider for a chat instance.

    :param chat_instance_id: str
    :param provider_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param provider_auth_config_id: Optional[str] (optional)
    :return: DashboardInstanceChatInstancesProviderSetOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            body_dict["provider_auth_config_id"] = provider_auth_config_id

        request = MetorialRequest(
            path=['chat', 'instances', chat_instance_id, 'provider'],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceChatInstancesProviderSetOutput.from_dict)

    def authenticated_user(self, chat_instance_id: str) -> DashboardInstanceChatInstancesProviderAuthenticatedUserOutput:
        """
    Get chat instance authenticated user
    Retrieves the chat provider account this chat instance is authenticated as.

    :param chat_instance_id: str
    :return: DashboardInstanceChatInstancesProviderAuthenticatedUserOutput
    """
        request = MetorialRequest(
            path=['chat', 'instances', chat_instance_id, 'provider', 'authenticated-user']
        )
        return self._get(request).transform(mapDashboardInstanceChatInstancesProviderAuthenticatedUserOutput.from_dict)