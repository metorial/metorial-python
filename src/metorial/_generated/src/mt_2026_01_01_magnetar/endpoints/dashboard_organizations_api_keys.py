from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsApiKeysListOutput, DashboardOrganizationsApiKeysListOutput, mapDashboardOrganizationsApiKeysListQuery, DashboardOrganizationsApiKeysListQuery, mapDashboardOrganizationsApiKeysGetOutput, DashboardOrganizationsApiKeysGetOutput, mapDashboardOrganizationsApiKeysCreateOutput, DashboardOrganizationsApiKeysCreateOutput, mapDashboardOrganizationsApiKeysCreateBody, DashboardOrganizationsApiKeysCreateBody, mapDashboardOrganizationsApiKeysUpdateOutput, DashboardOrganizationsApiKeysUpdateOutput, mapDashboardOrganizationsApiKeysUpdateBody, DashboardOrganizationsApiKeysUpdateBody, mapDashboardOrganizationsApiKeysRevokeOutput, DashboardOrganizationsApiKeysRevokeOutput, mapDashboardOrganizationsApiKeysRotateOutput, DashboardOrganizationsApiKeysRotateOutput, mapDashboardOrganizationsApiKeysRotateBody, DashboardOrganizationsApiKeysRotateBody, mapDashboardOrganizationsApiKeysRevealOutput, DashboardOrganizationsApiKeysRevealOutput

class MetorialDashboardOrganizationsApiKeysEndpoint(BaseMetorialEndpoint):
    """Read and write API key information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Any = None, instance_id: str = None) -> DashboardOrganizationsApiKeysListOutput:
        """
    Get user
    Get the current user information

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Any (optional)
    :param instance_id: str (optional)
    :return: DashboardOrganizationsApiKeysListOutput
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
        if type is not None:
            query_dict["type"] = type
        if instance_id is not None:
            query_dict["instance_id"] = instance_id

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsApiKeysListOutput.from_dict)

    def get(self, organization_id: str, api_key_id: str) -> DashboardOrganizationsApiKeysGetOutput:
        """
    Get API key
    Get the information of a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: DashboardOrganizationsApiKeysGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsApiKeysGetOutput.from_dict)

    def create(self, organization_id: str, *, name: str, type: Any = None, instance_id: str = None, description: Optional[str] = None, expires_at: Optional[datetime] = None, ip_filters: Optional[List[str]] = None) -> DashboardOrganizationsApiKeysCreateOutput:
        """
    Create API key
    Create a new API key

    :param organization_id: str
    :param type: Any (optional)
    :param instance_id: str (optional)
    :param name: str
    :param description: Optional[str] (optional)
    :param expires_at: Optional[datetime] (optional)
    :param ip_filters: Optional[List[str]] (optional)
    :return: DashboardOrganizationsApiKeysCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if type is not None:
            body_dict["type"] = type
        if instance_id is not None:
            body_dict["instance_id"] = instance_id
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if expires_at is not None:
            body_dict["expires_at"] = expires_at
        if ip_filters is not None:
            body_dict["ip_filters"] = ip_filters

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsApiKeysCreateOutput.from_dict)

    def update(self, organization_id: str, api_key_id: str, *, name: Optional[str] = None, description: Optional[str] = None, expires_at: Optional[datetime] = None, ip_filters: Optional[List[str]] = None) -> DashboardOrganizationsApiKeysUpdateOutput:
        """
    Update API key
    Update the information of a specific API key

    :param organization_id: str
    :param api_key_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param expires_at: Optional[datetime] (optional)
    :param ip_filters: Optional[List[str]] (optional)
    :return: DashboardOrganizationsApiKeysUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if expires_at is not None:
            body_dict["expires_at"] = expires_at
        if ip_filters is not None:
            body_dict["ip_filters"] = ip_filters

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsApiKeysUpdateOutput.from_dict)

    def revoke(self, organization_id: str, api_key_id: str) -> DashboardOrganizationsApiKeysRevokeOutput:
        """
    Revoke API key
    Revoke a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: DashboardOrganizationsApiKeysRevokeOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsApiKeysRevokeOutput.from_dict)

    def rotate(self, organization_id: str, api_key_id: str, *, current_expires_at: Optional[datetime] = None) -> DashboardOrganizationsApiKeysRotateOutput:
        """
    Rotate API key
    Rotate a specific API key

    :param organization_id: str
    :param api_key_id: str
    :param current_expires_at: Optional[datetime] (optional)
    :return: DashboardOrganizationsApiKeysRotateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if current_expires_at is not None:
            body_dict["current_expires_at"] = current_expires_at

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id, 'rotate'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsApiKeysRotateOutput.from_dict)

    def reveal(self, organization_id: str, api_key_id: str) -> DashboardOrganizationsApiKeysRevealOutput:
        """
    Reveal API key
    Reveal a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: DashboardOrganizationsApiKeysRevealOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id, 'reveal']
        )
        return self._post(request).transform(mapDashboardOrganizationsApiKeysRevealOutput.from_dict)