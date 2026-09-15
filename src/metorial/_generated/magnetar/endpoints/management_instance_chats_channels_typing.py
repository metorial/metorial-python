from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsChannelsTypingStartOutput, DashboardInstanceChatsChannelsTypingStartOutput, mapDashboardInstanceChatsChannelsTypingStartBody, DashboardInstanceChatsChannelsTypingStartBody

class MetorialManagementInstanceChatsChannelsTypingEndpoint(BaseMetorialEndpoint):
    """Chat channels are the conversations within a chat, such as Slack channels or Microsoft Teams channels."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def start(self, instance_id: str, chat_id: str, channel_id: str, *, thread_id: Optional[str] = None, status: Optional[str] = None) -> DashboardInstanceChatsChannelsTypingStartOutput:
        """
    Start chat typing indicator
    Shows a typing indicator in a chat channel.

    :param instance_id: str
    :param chat_id: str
    :param channel_id: str
    :param thread_id: Optional[str] (optional)
    :param status: Optional[str] (optional)
    :return: DashboardInstanceChatsChannelsTypingStartOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if thread_id is not None:
            body_dict["thread_id"] = thread_id
        if status is not None:
            body_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'channels', channel_id, 'typing'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatsChannelsTypingStartOutput.from_dict)