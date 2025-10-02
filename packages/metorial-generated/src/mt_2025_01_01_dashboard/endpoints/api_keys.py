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

  def create(self, organizationId: str, body: ApiKeysCreateBody) -> ApiKeysCreateOutput:
    """
    Create API key
    Create a new API key

    :param organizationId: str
    :param body: ApiKeysCreateBody
    :return: ApiKeysCreateOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys"],
      body=mapApiKeysCreateBody.to_dict(body),
    )
    return self._post(request).transform(mapApiKeysCreateOutput.from_dict)

  def update(
    self, organizationId: str, apiKeyId: str, body: ApiKeysUpdateBody
  ) -> ApiKeysUpdateOutput:
    """
    Update API key
    Update the information of a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :param body: ApiKeysUpdateBody
    :return: ApiKeysUpdateOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "api-keys", apiKeyId],
      body=mapApiKeysUpdateBody.to_dict(body),
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
    self, organizationId: str, apiKeyId: str, body: ApiKeysRotateBody
  ) -> ApiKeysRotateOutput:
    """
    Rotate API key
    Rotate a specific API key

    :param organizationId: str
    :param apiKeyId: str
    :param body: ApiKeysRotateBody
    :return: ApiKeysRotateOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organizationId,
        "api-keys",
        apiKeyId,
        "rotate",
      ],
      body=mapApiKeysRotateBody.to_dict(body),
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
