from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapOrganizationsFlagsGetOutput, OrganizationsFlagsGetOutput

class MetorialOrganizationsFlagsEndpoint(BaseMetorialEndpoint):
    """Read feature flags for the current organization and user"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, organization_id: str) -> OrganizationsFlagsGetOutput:
        """
    Get flags
    Get feature flags for the current organization and user

    :param organization_id: str
    :return: OrganizationsFlagsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'flags']
        )
        return self._get(request).transform(mapOrganizationsFlagsGetOutput.from_dict)