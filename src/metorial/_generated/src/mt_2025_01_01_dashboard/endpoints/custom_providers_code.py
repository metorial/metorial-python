from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput, DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput

class MetorialCustomProvidersCodeEndpoint(BaseMetorialEndpoint):
    """Manage custom provider code editor access."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get_code_editor_token(self, custom_provider_id: str) -> DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
        """
    Get code editor token
    Get a token to access the code editor for a custom provider.

    :param custom_provider_id: str
    :return: DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'code-editor-token']
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput.from_dict)
