from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardUsageTimelineOutput,
  DashboardUsageTimelineOutput,
  mapDashboardUsageTimelineQuery,
  DashboardUsageTimelineQuery,
)


class MetorialDashboardUsageEndpoint(BaseMetorialEndpoint):
  """Get usage information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def timeline(
    self,
    organization_id: str,
    *,
    entities: List[Dict[str, Any]],
    from_: datetime,
    to: datetime,
    interval: Dict[str, Any]
  ) -> DashboardUsageTimelineOutput:
    """
    Get organization
    Get the current organization information

    :param organization_id: str
    :param entities: List[Dict[str, Any]]
    :param from_: datetime
    :param to: datetime
    :param interval: Dict[str, Any]
    :return: DashboardUsageTimelineOutput
    """
    # Build query parameters from keyword arguments
    query_dict = {}
    query_dict["entities"] = entities
    query_dict["from"] = from_
    query_dict["to"] = to
    query_dict["interval"] = interval

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "usage", "timeline"],
      query=query_dict,
    )
    return self._get(request).transform(mapDashboardUsageTimelineOutput.from_dict)
