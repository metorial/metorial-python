from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsImportsListOutput, DashboardInstanceSkillsImportsListOutput, mapDashboardInstanceSkillsImportsListQuery, DashboardInstanceSkillsImportsListQuery, mapDashboardInstanceSkillsImportsGetOutput, DashboardInstanceSkillsImportsGetOutput, mapDashboardInstanceSkillsImportsCreateOutput, DashboardInstanceSkillsImportsCreateOutput, mapDashboardInstanceSkillsImportsCreateBody, DashboardInstanceSkillsImportsCreateBody

class MetorialDashboardInstanceSkillsImportsEndpoint(BaseMetorialEndpoint):
    """Import skills from public repositories or uploaded files."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSkillsImportsListOutput:
        """
    List skill imports
    Returns a paginated list of skill imports.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSkillsImportsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-imports'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsImportsListOutput.from_dict)

    def get(self, instance_id: str, skill_import_id: str) -> DashboardInstanceSkillsImportsGetOutput:
        """
    Get skill import
    Retrieves an individual skill import and its results.

    :param instance_id: str
    :param skill_import_id: str
    :return: DashboardInstanceSkillsImportsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-imports', skill_import_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsImportsGetOutput.from_dict)

    def create(self, instance_id: str, *, source: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any]]) -> DashboardInstanceSkillsImportsCreateOutput:
        """
    Create skill import
    Queues a skill import from a repository or uploaded file.

    :param instance_id: str
    :param source: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstanceSkillsImportsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["source"] = source

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-imports'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsImportsCreateOutput.from_dict)