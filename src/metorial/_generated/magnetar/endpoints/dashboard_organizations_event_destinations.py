from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsEventDestinationsListOutput, DashboardOrganizationsEventDestinationsListOutput, mapDashboardOrganizationsEventDestinationsListQuery, DashboardOrganizationsEventDestinationsListQuery, mapDashboardOrganizationsEventDestinationsGetOutput, DashboardOrganizationsEventDestinationsGetOutput, mapDashboardOrganizationsEventDestinationsCreateOutput, DashboardOrganizationsEventDestinationsCreateOutput, mapDashboardOrganizationsEventDestinationsCreateBody, DashboardOrganizationsEventDestinationsCreateBody, mapDashboardOrganizationsEventDestinationsUpdateOutput, DashboardOrganizationsEventDestinationsUpdateOutput, mapDashboardOrganizationsEventDestinationsUpdateBody, DashboardOrganizationsEventDestinationsUpdateBody, mapDashboardOrganizationsEventDestinationsArchiveOutput, DashboardOrganizationsEventDestinationsArchiveOutput, mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutput, DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput

class MetorialDashboardOrganizationsEventDestinationsEndpoint(BaseMetorialEndpoint):
    """Event destinations are where Metorial delivers system events for your organization. Webhooks are currently the only supported delivery type."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsEventDestinationsListOutput:
        """
    List event destinations
    List all event destinations configured for the organization

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsEventDestinationsListOutput
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
            path=['dashboard', 'organizations', organization_id, 'event-destinations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDestinationsListOutput.from_dict)

    def get(self, organization_id: str, event_destination_id: str) -> DashboardOrganizationsEventDestinationsGetOutput:
        """
    Get event destination
    Get a specific event destination configured for the organization

    :param organization_id: str
    :param event_destination_id: str
    :return: DashboardOrganizationsEventDestinationsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-destinations', event_destination_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDestinationsGetOutput.from_dict)

    def create(self, organization_id: str, *, name: str, type: Any, webhook: Dict[str, Any], description: Optional[str] = None) -> DashboardOrganizationsEventDestinationsCreateOutput:
        """
    Create event destination
    Create an event destination for the organization

    :param organization_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param type: Any
    :param webhook: Dict[str, Any]
    :return: DashboardOrganizationsEventDestinationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        body_dict["type"] = type
        body_dict["webhook"] = webhook

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-destinations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsEventDestinationsCreateOutput.from_dict)

    def update(self, organization_id: str, event_destination_id: str, *, name: Optional[str] = None, description: Optional[str] = None, webhook: Optional[Dict[str, Any]] = None) -> DashboardOrganizationsEventDestinationsUpdateOutput:
        """
    Update event destination
    Update an event destination configured for the organization

    :param organization_id: str
    :param event_destination_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param webhook: Optional[Dict[str, Any]] (optional)
    :return: DashboardOrganizationsEventDestinationsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if webhook is not None:
            body_dict["webhook"] = webhook

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-destinations', event_destination_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsEventDestinationsUpdateOutput.from_dict)

    def archive(self, organization_id: str, event_destination_id: str) -> DashboardOrganizationsEventDestinationsArchiveOutput:
        """
    Archive event destination
    Archives an event destination. Listeners pointed at it stop being delivered to.

    :param organization_id: str
    :param event_destination_id: str
    :return: DashboardOrganizationsEventDestinationsArchiveOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-destinations', event_destination_id, 'archive']
        )
        return self._post(request).transform(mapDashboardOrganizationsEventDestinationsArchiveOutput.from_dict)

    def rotate_webhook_secret(self, organization_id: str, event_destination_id: str) -> DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput:
        """
    Rotate event destination webhook secret
    Generates a new signing secret for this event destination's webhook, invalidating the previous one. The new secret is only returned in this response.

    :param organization_id: str
    :param event_destination_id: str
    :return: DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-destinations', event_destination_id, 'rotate-webhook-secret']
        )
        return self._post(request).transform(mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutput.from_dict)