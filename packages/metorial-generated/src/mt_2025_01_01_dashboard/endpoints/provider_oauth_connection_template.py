from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapProviderOauthConnectionTemplateListOutput,
  ProviderOauthConnectionTemplateListOutput,
  mapProviderOauthConnectionTemplateListQuery,
  ProviderOauthConnectionTemplateListQuery,
  mapProviderOauthConnectionTemplateGetOutput,
  ProviderOauthConnectionTemplateGetOutput,
  mapProviderOauthConnectionTemplateEvaluateOutput,
  ProviderOauthConnectionTemplateEvaluateOutput,
  mapProviderOauthConnectionTemplateEvaluateBody,
  ProviderOauthConnectionTemplateEvaluateBody,
)


class MetorialProviderOauthConnectionTemplateEndpoint(BaseMetorialEndpoint):
  """Get OAuth connection template information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, organizationId: str, query: ProviderOauthConnectionTemplateListQuery = None
  ) -> ProviderOauthConnectionTemplateListOutput:
    """
    List oauth connection templates
    List all oauth connection templates

    :param organizationId: str
    :param query: ProviderOauthConnectionTemplateListQuery
    :return: ProviderOauthConnectionTemplateListOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organizationId,
        "provider-oauth-connection-template",
      ],
      query=mapProviderOauthConnectionTemplateListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapProviderOauthConnectionTemplateListOutput.from_dict
    )

  def get(
    self, organizationId: str, oauthTemplateId: str
  ) -> ProviderOauthConnectionTemplateGetOutput:
    """
    Get oauth connection template
    Get the information of a specific oauth connection template

    :param organizationId: str
    :param oauthTemplateId: str
    :return: ProviderOauthConnectionTemplateGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organizationId,
        "provider-oauth-connection-template",
        oauthTemplateId,
      ]
    )
    return self._get(request).transform(
      mapProviderOauthConnectionTemplateGetOutput.from_dict
    )

  def evaluate(
    self, oauthTemplateId: str, body: ProviderOauthConnectionTemplateEvaluateBody
  ) -> ProviderOauthConnectionTemplateEvaluateOutput:
    """
    Evaluate oauth connection template
    Evaluate the configuration of an oauth connection template

    :param oauthTemplateId: str
    :param body: ProviderOauthConnectionTemplateEvaluateBody
    :return: ProviderOauthConnectionTemplateEvaluateOutput
    """
    request = MetorialRequest(
      path=["provider-oauth-connection-template", oauthTemplateId, "evaluate"],
      body=mapProviderOauthConnectionTemplateEvaluateBody.to_dict(body),
    )
    return self._post(request).transform(
      mapProviderOauthConnectionTemplateEvaluateOutput.from_dict
    )
