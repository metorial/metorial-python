from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsWebhookEventsListOutput, DashboardOrganizationsWebhookEventsListOutput

class MetorialDashboardOrganizationsWebhookEventsEndpoint(BaseMetorialEndpoint):
    """Events are the record of everything Metorial delivers to your event destinations — normal resource events, callback occurrences, chat connection events, and manual pings."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str) -> DashboardOrganizationsWebhookEventsListOutput:
        """
    List webhook events
    List all event types that event destination listeners can subscribe to

    :param organization_id: str
    :return: DashboardOrganizationsWebhookEventsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'webhook-events']
        )
        return self._get(request).transform(mapDashboardOrganizationsWebhookEventsListOutput.from_dict)