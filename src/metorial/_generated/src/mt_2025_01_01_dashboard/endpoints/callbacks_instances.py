from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbacksInstancesListOutput, DashboardInstanceCallbacksInstancesListOutput, mapDashboardInstanceCallbacksInstancesListQuery, DashboardInstanceCallbacksInstancesListQuery, mapDashboardInstanceCallbacksInstancesCreateOutput, DashboardInstanceCallbacksInstancesCreateOutput, mapDashboardInstanceCallbacksInstancesCreateBody, DashboardInstanceCallbacksInstancesCreateBody, mapDashboardInstanceCallbacksInstancesDeleteOutput, DashboardInstanceCallbacksInstancesDeleteOutput

class MetorialCallbacksInstancesEndpoint(BaseMetorialEndpoint):
    """Attach or detach callback instances for a deployment/config/auth-config combination."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, callback_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbacksInstancesListOutput:
        """
    List callback instances
    Returns a paginated list of callback instances.

    :param callback_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCallbacksInstancesListOutput
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
        if status is not None:
            query_dict["status"] = status
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['callbacks', callback_id, 'instances'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksInstancesListOutput.from_dict)

    def create(self, callback_id: str, *, provider_config_id: str, provider_auth_config_id: Optional[str] = None) -> DashboardInstanceCallbacksInstancesCreateOutput:
        """
    Create callback instance
    Attaches a callback to a config and optional auth config.

    :param callback_id: str
    :param provider_config_id: str
    :param provider_auth_config_id: Optional[str] (optional)
    :return: DashboardInstanceCallbacksInstancesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            body_dict["provider_auth_config_id"] = provider_auth_config_id

        request = MetorialRequest(
            path=['callbacks', callback_id, 'instances'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCallbacksInstancesCreateOutput.from_dict)

    def delete(self, callback_id: str, callback_instance_id: str) -> DashboardInstanceCallbacksInstancesDeleteOutput:
        """
    Delete callback instance
    Detaches a callback instance.

    :param callback_id: str
    :param callback_instance_id: str
    :return: DashboardInstanceCallbacksInstancesDeleteOutput
    """
        request = MetorialRequest(
            path=['callbacks', callback_id, 'instances', callback_instance_id]
        )
        return self._delete(request).transform(mapDashboardInstanceCallbacksInstancesDeleteOutput.from_dict)