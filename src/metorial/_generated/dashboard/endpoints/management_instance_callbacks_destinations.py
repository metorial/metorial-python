from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCallbacksDestinationsListOutput,
  DashboardInstanceCallbacksDestinationsListOutput,
  mapDashboardInstanceCallbacksDestinationsListQuery,
  DashboardInstanceCallbacksDestinationsListQuery,
  mapDashboardInstanceCallbacksDestinationsGetOutput,
  DashboardInstanceCallbacksDestinationsGetOutput,
  mapDashboardInstanceCallbacksDestinationsCreateOutput,
  DashboardInstanceCallbacksDestinationsCreateOutput,
  mapDashboardInstanceCallbacksDestinationsCreateBody,
  DashboardInstanceCallbacksDestinationsCreateBody,
  mapDashboardInstanceCallbacksDestinationsUpdateOutput,
  DashboardInstanceCallbacksDestinationsUpdateOutput,
  mapDashboardInstanceCallbacksDestinationsUpdateBody,
  DashboardInstanceCallbacksDestinationsUpdateBody,
  mapDashboardInstanceCallbacksDestinationsDeleteOutput,
  DashboardInstanceCallbacksDestinationsDeleteOutput,
)


class MetorialManagementInstanceCallbacksDestinationsEndpoint(BaseMetorialEndpoint):
  """Represents callbacks that you have uploaded to Metorial. Callbacks can be linked to various resources based on their purpose. Metorial can also automatically extract callbacks for you, for example for data exports."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    callback_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceCallbacksDestinationsListOutput:
    """
    List callback destinations
    Returns a paginated list of callback destinations for a specific callback.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCallbacksDestinationsListOutput
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
    if callback_id is not None:
      query_dict["callback_id"] = callback_id

    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-destinations"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceCallbacksDestinationsListOutput.from_dict
    )

  def get(
    self, instance_id: str, destination_id: str
  ) -> DashboardInstanceCallbacksDestinationsGetOutput:
    """
    Get callback destination by ID
    Retrieves details for a specific callback by its ID.

    :param instance_id: str
    :param destination_id: str
    :return: DashboardInstanceCallbacksDestinationsGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-destinations", destination_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceCallbacksDestinationsGetOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    *,
    name: str,
    url: str,
    callbacks: Union[Dict[str, Any], Dict[str, Any]],
    description: Optional[str] = None
  ) -> DashboardInstanceCallbacksDestinationsCreateOutput:
    """
    Create callback destination
    Creates a new callback destination for the instance.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param url: str
    :param callbacks: Union[Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstanceCallbacksDestinationsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    body_dict["url"] = url
    body_dict["callbacks"] = callbacks

    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-destinations"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardInstanceCallbacksDestinationsCreateOutput.from_dict
    )

  def update(
    self,
    instance_id: str,
    destination_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None
  ) -> DashboardInstanceCallbacksDestinationsUpdateOutput:
    """
    Update callback destination
    Updates an existing callback destination for the instance.

    :param instance_id: str
    :param destination_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: DashboardInstanceCallbacksDestinationsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description

    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-destinations", destination_id],
      body=body_dict,
    )
    return self._patch(request).transform(
      mapDashboardInstanceCallbacksDestinationsUpdateOutput.from_dict
    )

  def delete(
    self, instance_id: str, destination_id: str
  ) -> DashboardInstanceCallbacksDestinationsDeleteOutput:
    """
    Delete callback destination
    Deletes an existing callback destination for the instance.

    :param instance_id: str
    :param destination_id: str
    :return: DashboardInstanceCallbacksDestinationsDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-destinations", destination_id]
    )
    return self._delete(request).transform(
      mapDashboardInstanceCallbacksDestinationsDeleteOutput.from_dict
    )
