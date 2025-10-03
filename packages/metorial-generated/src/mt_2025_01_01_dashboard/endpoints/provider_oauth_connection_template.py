from typing import Any, Dict, List, Optional, Union
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
    self,
    organization_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    profile_id: Optional[Union[List[str], str]] = None
  ) -> ProviderOauthConnectionTemplateListOutput:
    """
    List oauth connection templates
    List all oauth connection templates

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param profile_id: Optional[Union[List[str], str]] (optional)
    :return: ProviderOauthConnectionTemplateListOutput
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
    if profile_id is not None:
      query_dict["profile_id"] = profile_id

    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "provider-oauth-connection-template",
      ],
      query=query_dict,
    )
    return self._get(request).transform(
      mapProviderOauthConnectionTemplateListOutput.from_dict
    )

  def get(
    self, organization_id: str, oauth_template_id: str
  ) -> ProviderOauthConnectionTemplateGetOutput:
    """
    Get oauth connection template
    Get the information of a specific oauth connection template

    :param organization_id: str
    :param oauth_template_id: str
    :return: ProviderOauthConnectionTemplateGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "provider-oauth-connection-template",
        oauth_template_id,
      ]
    )
    return self._get(request).transform(
      mapProviderOauthConnectionTemplateGetOutput.from_dict
    )

  def evaluate(
    self, oauth_template_id: str, *, data: Dict[str, Any]
  ) -> ProviderOauthConnectionTemplateEvaluateOutput:
    """
    Evaluate oauth connection template
    Evaluate the configuration of an oauth connection template

    :param oauth_template_id: str
    :param data: Dict[str, Any]
    :return: ProviderOauthConnectionTemplateEvaluateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["data"] = data

    request = MetorialRequest(
      path=["provider-oauth-connection-template", oauth_template_id, "evaluate"],
      body=body_dict,
    )
    return self._post(request).transform(
      mapProviderOauthConnectionTemplateEvaluateOutput.from_dict
    )
