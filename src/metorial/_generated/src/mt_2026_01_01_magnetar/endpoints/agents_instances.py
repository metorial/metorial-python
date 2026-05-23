from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAgentsInstancesListOutput, DashboardInstanceAgentsInstancesListOutput, mapDashboardInstanceAgentsInstancesListQuery, DashboardInstanceAgentsInstancesListQuery, mapDashboardInstanceAgentsInstancesGetOutput, DashboardInstanceAgentsInstancesGetOutput

class MetorialAgentsInstancesEndpoint(BaseMetorialEndpoint):
    """Inspect agents and their linked clients and instances."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, agent_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, agent_client_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceAgentsInstancesListOutput:
        """
    List agent instances
    Returns a paginated list of instances for an agent.

    :param agent_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param agent_client_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceAgentsInstancesListOutput
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
        if id is not None:
            query_dict["id"] = id
        if agent_client_id is not None:
            query_dict["agent_client_id"] = agent_client_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['agents', agent_id, 'instances'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAgentsInstancesListOutput.from_dict)

    def get(self, agent_id: str, agent_instance_id: str) -> DashboardInstanceAgentsInstancesGetOutput:
        """
    Get agent instance
    Retrieves a specific agent instance by ID.

    :param agent_id: str
    :param agent_instance_id: str
    :return: DashboardInstanceAgentsInstancesGetOutput
    """
        request = MetorialRequest(
            path=['agents', agent_id, 'instances', agent_instance_id]
        )
        return self._get(request).transform(mapDashboardInstanceAgentsInstancesGetOutput.from_dict)