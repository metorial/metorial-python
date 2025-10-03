from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersCodeGetCodeEditorTokenOutput,
  DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput,
)


class MetorialCustomServersCodeEndpoint(BaseMetorialEndpoint):
  """Manager custom server deployments"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get_code_editor_token(
    self, custom_server_id: str
  ) -> DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput:
    """
    Get code editor token
    Get a token to access the code editor for a custom server

    :param custom_server_id: str
    :return: DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput
    """
    request = MetorialRequest(
      path=["custom-servers", custom_server_id, "code-editor-token"]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersCodeGetCodeEditorTokenOutput.from_dict
    )
