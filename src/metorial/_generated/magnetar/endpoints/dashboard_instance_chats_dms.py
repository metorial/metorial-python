from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsDmsOpenOutput, DashboardInstanceChatsDmsOpenOutput, mapDashboardInstanceChatsDmsOpenBody, DashboardInstanceChatsDmsOpenBody

class MetorialDashboardInstanceChatsDmsEndpoint(BaseMetorialEndpoint):
    """Open direct message channels with one or more users on a chat."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def open(self, instance_id: str, chat_id: str) -> DashboardInstanceChatsDmsOpenOutput:
        """
    Open chat DM
    Opens (or retrieves) a direct message channel with one or more users.

    :param instance_id: str
    :param chat_id: str
    :return: DashboardInstanceChatsDmsOpenOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'dms']
        )
        return self._post(request).transform(mapDashboardInstanceChatsDmsOpenOutput.from_dict)