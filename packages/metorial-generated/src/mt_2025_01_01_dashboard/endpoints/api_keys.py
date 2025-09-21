from typing import Optional, Dict, Any, List, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapApiKeysListOutput,
  ApiKeysListOutput,
  mapApiKeysListQuery,
  ApiKeysListQuery,
  mapApiKeysGetOutput,
  ApiKeysGetOutput,
  mapApiKeysCreateOutput,
  ApiKeysCreateOutput,
  mapApiKeysCreateBody,
  ApiKeysCreateBody,
  mapApiKeysUpdateOutput,
  ApiKeysUpdateOutput,
  mapApiKeysUpdateBody,
  ApiKeysUpdateBody,
  mapApiKeysRevokeOutput,
  ApiKeysRevokeOutput,
  mapApiKeysRotateOutput,
  ApiKeysRotateOutput,
  mapApiKeysRotateBody,
  ApiKeysRotateBody,
  mapApiKeysRevealOutput,
  ApiKeysRevealOutput,
)


class MetorialApiKeysEndpoint(BaseMetorialEndpoint):
  """Read and write API key information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, organizationId: str, query: ApiKeysListQuery = None
  ) -> ApiKeysListOutput:
    """
    Get user
    Get the current user information

    :param organizationId: str
    :param query: ApiKeysListQuery
    :return: ApiKeysListOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys"],
      query=mapApiKeysListQuery.to_dict(query) if query is not None else None,
    )
    return self._get(request).transform(mapApiKeysListOutput.from_dict)

  def get(self, organizationId: str, apiKeyId: str) -> ApiKeysGetOutput:
    """
    Get API key
    Get the information of a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :return: ApiKeysGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys", apiKeyId]
    )
    return self._get(request).transform(mapApiKeysGetOutput.from_dict)

  def create(self, organizationId: str) -> ApiKeysCreateOutput:
    """
    Create API key
    Create a new API key

    :param organizationId: str
    :return: ApiKeysCreateOutput
    """
    {}

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys"],
      body=body,
    )
    return self._post(request).transform(mapApiKeysCreateOutput.from_dict)

  def update(
    self,
    organizationId: str,
    apiKeyId: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    expires_at: Optional[str] = None
  ) -> ApiKeysUpdateOutput:
    """
    Update API key
    Update the information of a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :param name: str (optional)
    :param description: str (optional)
    :param expires_at: str (optional)
    :return: ApiKeysUpdateOutput
    """
    _params = {"name": name, "description": description, "expires_at": expires_at}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys", apiKeyId],
      body=body,
    )
    return self._post(request).transform(mapApiKeysUpdateOutput.from_dict)

  def revoke(self, organizationId: str, apiKeyId: str) -> ApiKeysRevokeOutput:
    """
    Revoke API key
    Revoke a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :return: ApiKeysRevokeOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys", apiKeyId]
    )
    return self._delete(request).transform(mapApiKeysRevokeOutput.from_dict)

  def rotate(
    self,
    organizationId: str,
    apiKeyId: str,
    *,
    current_expires_at: Optional[str] = None
  ) -> ApiKeysRotateOutput:
    """
    Rotate API key
    Rotate a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :param current_expires_at: str (optional)
    :return: ApiKeysRotateOutput
    """
    _params = {"current_expires_at": current_expires_at}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organizationId,
        "api-keys",
        apiKeyId,
        "rotate",
      ],
      body=body,
    )
    return self._post(request).transform(mapApiKeysRotateOutput.from_dict)

  def reveal(self, organizationId: str, apiKeyId: str) -> ApiKeysRevealOutput:
    """
    Reveal API key
    Reveal a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :return: ApiKeysRevealOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organizationId,
        "api-keys",
        apiKeyId,
        "reveal",
      ]
    )
    return self._post(request).transform(mapApiKeysRevealOutput.from_dict)
