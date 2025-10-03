from typing import Any, Dict, List, Optional, Union
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

    :param name: Optional[str] (optional)
    :param email: Optional[str] (optional)
    :return: ManagementUserUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if email is not None:
      body_dict["email"] = email

    request = MetorialRequest(path=["user"], body=body_dict)
    return self._post(request).transform(mapManagementUserUpdateOutput.from_dict)

  def delete(
    self, *, name: Optional[str] = None, email: Optional[str] = None
  ) -> ManagementUserDeleteOutput:
    """
    Update user
    Update the current user information

    :param name: Optional[str] (optional)
    :param email: Optional[str] (optional)
    :return: ManagementUserDeleteOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if email is not None:
      body_dict["email"] = email

    request = MetorialRequest(path=["user"], body=body_dict)
    return self._post(request).transform(mapManagementUserDeleteOutput.from_dict)
