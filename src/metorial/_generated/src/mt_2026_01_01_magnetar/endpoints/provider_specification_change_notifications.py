from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderSpecificationChangeNotificationsListOutput, DashboardInstanceProviderSpecificationChangeNotificationsListOutput, mapDashboardInstanceProviderSpecificationChangeNotificationsListQuery, DashboardInstanceProviderSpecificationChangeNotificationsListQuery, mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutput, DashboardInstanceProviderSpecificationChangeNotificationsGetOutput

class MetorialProviderSpecificationChangeNotificationsEndpoint(BaseMetorialEndpoint):
    """Provider specification change notifications describe provider schema changes."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, target: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_version_id: Optional[Union[str, List[str]]] = None, provider_specification_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderSpecificationChangeNotificationsListOutput:
        """
    List provider specification change notifications
    Returns a paginated list of provider specification change notifications for this instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param target: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_version_id: Optional[Union[str, List[str]]] (optional)
    :param provider_specification_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderSpecificationChangeNotificationsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if target is not None:
            query_dict["target"] = target
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_version_id is not None:
            query_dict["provider_version_id"] = provider_version_id
        if provider_specification_id is not None:
            query_dict["provider_specification_id"] = provider_specification_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['provider-specification-change-notifications'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderSpecificationChangeNotificationsListOutput.from_dict)

    def get(self, notification_id: str) -> DashboardInstanceProviderSpecificationChangeNotificationsGetOutput:
        """
    Get provider specification change notification
    Retrieves a provider specification change notification by ID.

    :param notification_id: str
    :return: DashboardInstanceProviderSpecificationChangeNotificationsGetOutput
    """
        request = MetorialRequest(
            path=['provider-specification-change-notifications', notification_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutput.from_dict)