from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerDevicesTelemetryTokenIssueOutput, ConsumerDevicesTelemetryTokenIssueOutput

class MetorialConsumerDevicesTelemetryTokenEndpoint(BaseMetorialEndpoint):
    """Enroll Metorial Desktop devices and choose which integrations and skills each AI tool on them receives."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def issue(self, consumer_device_id: str) -> ConsumerDevicesTelemetryTokenIssueOutput:
        """
    Issue device telemetry token
    Issues the ingest token the device sends agent telemetry with, bound to the consumer that enrolled this device. Every call rotates: the new token replaces the previous tokens of the device, which are revoked. The secret is only returned here. Returns 404 when this server does not collect agent telemetry, and 412 when the device is no longer signed in.

    :param consumer_device_id: str
    :return: ConsumerDevicesTelemetryTokenIssueOutput
    """
        request = MetorialRequest(
            path=['consumer', 'devices', consumer_device_id, 'telemetry-token']
        )
        return self._post(request).transform(mapConsumerDevicesTelemetryTokenIssueOutput.from_dict)