from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxSpecsListOutput, DashboardInstanceSandboxSpecsListOutput, mapDashboardInstanceSandboxSpecsListQuery, DashboardInstanceSandboxSpecsListQuery, mapDashboardInstanceSandboxSpecsGetOutput, DashboardInstanceSandboxSpecsGetOutput

class MetorialManagementInstanceSandboxSpecsEndpoint(BaseMetorialEndpoint):
    """The CPU and memory sizes sandbox machines can be created with."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSandboxSpecsListOutput:
        """
    List sandbox specs
    Returns a paginated list of machine specs. The available field shows whether your plan allows creating machines of that size.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSandboxSpecsListOutput
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

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'specs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxSpecsListOutput.from_dict)

    def get(self, instance_id: str, spec_id: str) -> DashboardInstanceSandboxSpecsGetOutput:
        """
    Get sandbox spec
    Retrieves a machine spec by ID.

    :param instance_id: str
    :param spec_id: str
    :return: DashboardInstanceSandboxSpecsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'specs', spec_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxSpecsGetOutput.from_dict)