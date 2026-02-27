from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput, DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput

class MetorialDashboardInstanceCustomProvidersCodeEndpoint(BaseMetorialEndpoint):
    """Manage custom provider code editor access."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get_code_editor_token(self, instance_id: str, custom_provider_id: str) -> DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
        """
    Get code editor token
    Get a token to access the code editor for a custom provider.

    :param instance_id: str
    :param custom_provider_id: str
    :return: DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'custom-providers', custom_provider_id, 'code-editor-token']
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput.from_dict)
