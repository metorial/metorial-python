from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMergeRequestsItemsResolveOutput, DashboardInstanceSkillsMergeRequestsItemsResolveOutput, mapDashboardInstanceSkillsMergeRequestsItemsResolveBody, DashboardInstanceSkillsMergeRequestsItemsResolveBody, mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput, DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput, mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveBody, DashboardInstanceSkillsMergeRequestsItemsBulkResolveBody

class MetorialSkillsMergeRequestsItemsEndpoint(BaseMetorialEndpoint):
    """Review, resolve, and apply changes between skills."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def resolve(self, skill_merge_request_id: str, item_id: str, *, resolution_type: str, resolution: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsMergeRequestsItemsResolveOutput:
        """
    Resolve skill merge request item
    Saves a resolution for one proposed skill change.

    :param skill_merge_request_id: str
    :param item_id: str
    :param resolution_type: str
    :param resolution: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsMergeRequestsItemsResolveOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["resolution_type"] = resolution_type
        if resolution is not None:
            body_dict["resolution"] = resolution

        request = MetorialRequest(
            path=['skill-merge-requests', skill_merge_request_id, 'items', item_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsMergeRequestsItemsResolveOutput.from_dict)

    def bulk_resolve(self, skill_merge_request_id: str, *, items: List[Dict[str, Any]]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput:
        """
    Resolve skill merge request items
    Saves resolutions for multiple proposed skill changes.

    :param skill_merge_request_id: str
    :param items: List[Dict[str, Any]]
    :return: DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["items"] = items

        request = MetorialRequest(
            path=['skill-merge-requests', skill_merge_request_id, 'items'],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput.from_dict)