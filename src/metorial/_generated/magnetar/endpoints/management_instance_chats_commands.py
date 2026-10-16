from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsCommandsRespondOutput, DashboardInstanceChatsCommandsRespondOutput, mapDashboardInstanceChatsCommandsRespondBody, DashboardInstanceChatsCommandsRespondBody

class MetorialManagementInstanceChatsCommandsEndpoint(BaseMetorialEndpoint):
    """Chat messages are the individual messages sent within a chat channel."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def respond(self, instance_id: str, chat_id: str, *, chat_event_id: str, parts: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]], alt_text: Optional[str] = None, ephemeral: Optional[bool] = None) -> DashboardInstanceChatsCommandsRespondOutput:
        """
    Respond to chat command
    Replies to a slash command from a chat.command.invoked event, using the provider's native command response.

    :param instance_id: str
    :param chat_id: str
    :param chat_event_id: str
    :param parts: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]
    :param alt_text: Optional[str] (optional)
    :param ephemeral: Optional[bool] (optional)
    :return: DashboardInstanceChatsCommandsRespondOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["chat_event_id"] = chat_event_id
        body_dict["parts"] = parts
        if alt_text is not None:
            body_dict["alt_text"] = alt_text
        if ephemeral is not None:
            body_dict["ephemeral"] = ephemeral

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'commands', 'respond'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatsCommandsRespondOutput.from_dict)