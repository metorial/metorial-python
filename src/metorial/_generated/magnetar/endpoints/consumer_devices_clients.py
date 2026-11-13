from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerDevicesClientsUpdateOutput, ConsumerDevicesClientsUpdateOutput, mapConsumerDevicesClientsUpdateBody, ConsumerDevicesClientsUpdateBody

class MetorialConsumerDevicesClientsEndpoint(BaseMetorialEndpoint):
    """Enroll Metorial Desktop devices and choose which integrations and skills each AI tool on them receives."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def update(self, consumer_device_id: str, client_key: str, *, enabled: Optional[bool] = None, excluded_magic_mcp_server_ids: Optional[List[str]] = None, excluded_skill_ids: Optional[List[str]] = None) -> ConsumerDevicesClientsUpdateOutput:
        """
    Update device AI tool
    Turns an AI tool on the device on or off, and chooses which integrations and skills it does not receive. The device applies the change at its next sync.

    :param consumer_device_id: str
    :param client_key: str
    :param enabled: Optional[bool] (optional)
    :param excluded_magic_mcp_server_ids: Optional[List[str]] (optional)
    :param excluded_skill_ids: Optional[List[str]] (optional)
    :return: ConsumerDevicesClientsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if enabled is not None:
            body_dict["enabled"] = enabled
        if excluded_magic_mcp_server_ids is not None:
            body_dict["excluded_magic_mcp_server_ids"] = excluded_magic_mcp_server_ids
        if excluded_skill_ids is not None:
            body_dict["excluded_skill_ids"] = excluded_skill_ids

        request = MetorialRequest(
            path=['consumer', 'devices', consumer_device_id, 'clients', client_key],
            body=body_dict
        )
        return self._patch(request).transform(mapConsumerDevicesClientsUpdateOutput.from_dict)