from typing import Any, Dict, List, Optional, Union
from datetime import datetime
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
    self,
    organization_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    type: Any = None,
    instance_id: str = None
  ) -> ApiKeysListOutput:
    """
    Get user
    Get the current user information

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Any (optional)
    :param instance_id: str (optional)
    :return: ApiKeysListOutput
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
    if type is not None:
      query_dict["type"] = type
    if instance_id is not None:
      query_dict["instance_id"] = instance_id

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "api-keys"], query=query_dict
    )
    return self._get(request).transform(mapApiKeysListOutput.from_dict)

  def get(self, organization_id: str, api_key_id: str) -> ApiKeysGetOutput:
    """
    Get API key
    Get the information of a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: ApiKeysGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "api-keys", api_key_id]
    )
    return self._get(request).transform(mapApiKeysGetOutput.from_dict)

  def create(
    self,
    organization_id: str,
    *,
    name: str,
    type: Any = None,
    instance_id: str = None,
    description: Optional[str] = None,
    expires_at: Optional[datetime] = None
  ) -> ApiKeysCreateOutput:
    """
    Create API key
    Create a new API key

    :param organization_id: str
    :param type: Any (optional)
    :param instance_id: str (optional)
    :param name: str
    :param description: Optional[str] (optional)
    :param expires_at: Optional[datetime] (optional)
    :return: ApiKeysCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if type is not None:
      body_dict["type"] = type
    if instance_id is not None:
      body_dict["instance_id"] = instance_id
    body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if expires_at is not None:
      body_dict["expires_at"] = expires_at

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "api-keys"], body=body_dict
    )
    return self._post(request).transform(mapApiKeysCreateOutput.from_dict)

  def update(
    self,
    organization_id: str,
    api_key_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    expires_at: Optional[datetime] = None
  ) -> ApiKeysUpdateOutput:
    """
    Update API key
    Update the information of a specific API key

    :param organization_id: str
    :param api_key_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param expires_at: Optional[datetime] (optional)
    :return: ApiKeysUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if expires_at is not None:
      body_dict["expires_at"] = expires_at

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "api-keys", api_key_id],
      body=body_dict,
    )
    return self._post(request).transform(mapApiKeysUpdateOutput.from_dict)

  def revoke(self, organization_id: str, api_key_id: str) -> ApiKeysRevokeOutput:
    """
    Revoke API key
    Revoke a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: ApiKeysRevokeOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "api-keys", api_key_id]
    )
    return self._delete(request).transform(mapApiKeysRevokeOutput.from_dict)

  def rotate(
    self,
    organization_id: str,
    api_key_id: str,
    *,
    current_expires_at: Optional[datetime] = None
  ) -> ApiKeysRotateOutput:
    """
    Rotate API key
    Rotate a specific API key

    :param organization_id: str
    :param api_key_id: str
    :param current_expires_at: Optional[datetime] (optional)
    :return: ApiKeysRotateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if current_expires_at is not None:
      body_dict["current_expires_at"] = current_expires_at

    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "api-keys",
        api_key_id,
        "rotate",
      ],
      body=body_dict,
    )
    return self._post(request).transform(mapApiKeysRotateOutput.from_dict)

  def reveal(self, organization_id: str, api_key_id: str) -> ApiKeysRevealOutput:
    """
    Reveal API key
    Reveal a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: ApiKeysRevealOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "api-keys",
        api_key_id,
        "reveal",
      ]
    )
    return self._post(request).transform(mapApiKeysRevealOutput.from_dict)
