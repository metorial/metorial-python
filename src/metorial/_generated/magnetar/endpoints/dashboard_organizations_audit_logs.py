from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsAuditLogsListOutput, DashboardOrganizationsAuditLogsListOutput, mapDashboardOrganizationsAuditLogsListQuery, DashboardOrganizationsAuditLogsListQuery, mapDashboardOrganizationsAuditLogsGetOutput, DashboardOrganizationsAuditLogsGetOutput

class MetorialDashboardOrganizationsAuditLogsEndpoint(BaseMetorialEndpoint):
    """Read organization audit logs"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsAuditLogsListOutput:
        """
    List organization audit logs
    List audit logs recorded for the organization

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsAuditLogsListOutput
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
            path=['dashboard', 'organizations', organization_id, 'audit-logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsAuditLogsListOutput.from_dict)

    def get(self, organization_id: str, audit_log_id: str) -> DashboardOrganizationsAuditLogsGetOutput:
        """
    Get organization audit log
    Get a specific audit log recorded for the organization

    :param organization_id: str
    :param audit_log_id: str
    :return: DashboardOrganizationsAuditLogsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'audit-logs', audit_log_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsAuditLogsGetOutput.from_dict)