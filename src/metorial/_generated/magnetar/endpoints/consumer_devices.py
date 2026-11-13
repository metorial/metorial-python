from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerDevicesCheckInOutput, ConsumerDevicesCheckInOutput, mapConsumerDevicesCheckInBody, ConsumerDevicesCheckInBody, mapConsumerDevicesListOutput, ConsumerDevicesListOutput, mapConsumerDevicesListQuery, ConsumerDevicesListQuery, mapConsumerDevicesGetOutput, ConsumerDevicesGetOutput, mapConsumerDevicesSignOutOutput, ConsumerDevicesSignOutOutput, mapConsumerDevicesRevokeOutput, ConsumerDevicesRevokeOutput

class MetorialConsumerDevicesEndpoint(BaseMetorialEndpoint):
    """Enroll Metorial Desktop devices and choose which integrations and skills each AI tool on them receives."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def check_in(self, *, installation_id: str, name: str, os: str, arch: str, app_version: str, clients: List[Dict[str, Any]], magic_mcp_token_ids: Optional[List[str]] = None) -> ConsumerDevicesCheckInOutput:
        """
    Check in device
    Enrolls the signed-in Metorial Desktop device, or refreshes what it reports, and returns what each AI tool on it should receive.

    :param installation_id: str
    :param name: str
    :param os: str
    :param arch: str
    :param app_version: str
    :param clients: List[Dict[str, Any]]
    :param magic_mcp_token_ids: Optional[List[str]] (optional)
    :return: ConsumerDevicesCheckInOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["installation_id"] = installation_id
        body_dict["name"] = name
        body_dict["os"] = os
        body_dict["arch"] = arch
        body_dict["app_version"] = app_version
        body_dict["clients"] = clients
        if magic_mcp_token_ids is not None:
            body_dict["magic_mcp_token_ids"] = magic_mcp_token_ids

        request = MetorialRequest(
            path=['consumer', 'devices', 'check-in'],
            body=body_dict
        )
        return self._post(request).transform(mapConsumerDevicesCheckInOutput.from_dict)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> ConsumerDevicesListOutput:
        """
    List devices
    Returns the devices the authenticated consumer profile has enrolled.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: ConsumerDevicesListOutput
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
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['consumer', 'devices'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerDevicesListOutput.from_dict)

    def get(self, consumer_device_id: str) -> ConsumerDevicesGetOutput:
        """
    Get device
    Retrieves a device enrolled by the authenticated consumer profile.

    :param consumer_device_id: str
    :return: ConsumerDevicesGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'devices', consumer_device_id]
        )
        return self._get(request).transform(mapConsumerDevicesGetOutput.from_dict)

    def sign_out(self) -> ConsumerDevicesSignOutOutput:
        """
    Sign out device
    Ends the device sign-in this request was made with and revokes its integration tokens. Other devices stay signed in.


    :return: ConsumerDevicesSignOutOutput
    """
        request = MetorialRequest(
            path=['consumer', 'devices', 'sign-out']
        )
        return self._post(request).transform(mapConsumerDevicesSignOutOutput.from_dict)

    def revoke(self, consumer_device_id: str) -> ConsumerDevicesRevokeOutput:
        """
    Revoke device
    Signs the device out and revokes its integration tokens. The app removes what it installed the next time it reaches Metorial.

    :param consumer_device_id: str
    :return: ConsumerDevicesRevokeOutput
    """
        request = MetorialRequest(
            path=['consumer', 'devices', consumer_device_id, 'revoke']
        )
        return self._post(request).transform(mapConsumerDevicesRevokeOutput.from_dict)