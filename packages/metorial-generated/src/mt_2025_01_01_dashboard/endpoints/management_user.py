from typing import Optional, Dict, Any, List, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapManagementUserGetOutput,
  ManagementUserGetOutput,
  mapManagementUserUpdateOutput,
  ManagementUserUpdateOutput,
  mapManagementUserUpdateBody,
  ManagementUserUpdateBody,
  mapManagementUserDeleteOutput,
  ManagementUserDeleteOutput,
  mapManagementUserDeleteBody,
  ManagementUserDeleteBody,
)


class MetorialManagementUserEndpoint(BaseMetorialEndpoint):
  """Read and write user information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(self) -> ManagementUserGetOutput:
    """
    Get user
    Get the current user information


    :return: ManagementUserGetOutput
    """
    request = MetorialRequest(path=["user"])
    return self._get(request).transform(mapManagementUserGetOutput.from_dict)

  def update(
    self, *, name: Optional[str] = None, email: Optional[str] = None
  ) -> ManagementUserUpdateOutput:
    """
    Update user
    Update the current user information

    :param name: str (optional)
    :param email: str (optional)
    :return: ManagementUserUpdateOutput
    """
    _params = {"name": name, "email": email}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["user"],
      body=body,
    )
    return self._post(request).transform(mapManagementUserUpdateOutput.from_dict)

  def delete(
    self, *, name: Optional[str] = None, email: Optional[str] = None
  ) -> ManagementUserDeleteOutput:
    """
    Update user
    Update the current user information

    :param name: str (optional)
    :param email: str (optional)
    :return: ManagementUserDeleteOutput
    """
    _params = {"name": name, "email": email}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["user"],
      body=body,
    )
    return self._post(request).transform(mapManagementUserDeleteOutput.from_dict)
