from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersCodeGetCodeEditorTokenOutput,
  DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput,
)


class MetorialManagementInstanceCustomServersCodeEndpoint(BaseMetorialEndpoint):
  """Manager custom server deployments"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get_code_editor_token(
    self, instanceId: str, customServerId: str
  ) -> DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput:
    """
    Get code editor token
    Get a token to access the code editor for a custom server

    :param instanceId: str
    :param customServerId: str
    :return: DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "code-editor-token",
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersCodeGetCodeEditorTokenOutput.from_dict
    )
