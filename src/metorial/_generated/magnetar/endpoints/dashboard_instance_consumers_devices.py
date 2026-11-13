from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceConsumersDevicesListOutput, DashboardInstanceConsumersDevicesListOutput, mapDashboardInstanceConsumersDevicesListQuery, DashboardInstanceConsumersDevicesListQuery, mapDashboardInstanceConsumersDevicesGetOutput, DashboardInstanceConsumersDevicesGetOutput, mapDashboardInstanceConsumersDevicesRevokeOutput, DashboardInstanceConsumersDevicesRevokeOutput

class MetorialDashboardInstanceConsumersDevicesEndpoint(BaseMetorialEndpoint):
    """Inspect and revoke the Metorial Desktop devices consumers have enrolled."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, consumer_profile_id: Optional[Union[str, List[str]]] = None, consumer_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceConsumersDevicesListOutput:
        """
    List consumer devices
    Returns the Metorial Desktop devices enrolled by consumers of an instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param consumer_profile_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceConsumersDevicesListOutput
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
        if consumer_profile_id is not None:
            query_dict["consumer_profile_id"] = consumer_profile_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumer-devices'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceConsumersDevicesListOutput.from_dict)

    def get(self, instance_id: str, consumer_device_id: str) -> DashboardInstanceConsumersDevicesGetOutput:
        """
    Get consumer device
    Retrieves a Metorial Desktop device enrolled by a consumer.

    :param instance_id: str
    :param consumer_device_id: str
    :return: DashboardInstanceConsumersDevicesGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumer-devices', consumer_device_id]
        )
        return self._get(request).transform(mapDashboardInstanceConsumersDevicesGetOutput.from_dict)

    def revoke(self, instance_id: str, consumer_device_id: str) -> DashboardInstanceConsumersDevicesRevokeOutput:
        """
    Revoke consumer device
    Signs the device out and revokes its integration tokens. The app removes what it installed the next time it reaches Metorial.

    :param instance_id: str
    :param consumer_device_id: str
    :return: DashboardInstanceConsumersDevicesRevokeOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumer-devices', consumer_device_id, 'revoke']
        )
        return self._post(request).transform(mapDashboardInstanceConsumersDevicesRevokeOutput.from_dict)