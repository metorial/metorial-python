from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AgentsInstancesGetOutputAgentClient:
    object: str
    id: str
    type: str
    name: str
    created_at: datetime
    updated_at: datetime
    last_connected_at: Optional[datetime] = None
@dataclass
class AgentsInstancesGetOutput:
    object: str
    id: str
    type: str
    name: str
    agent_id: str
    created_at: datetime
    updated_at: datetime
    version: Optional[str] = None
    description: Optional[str] = None
    agent_client: Optional[AgentsInstancesGetOutputAgentClient] = None
    last_connected_at: Optional[datetime] = None


class mapAgentsInstancesGetOutputAgentClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AgentsInstancesGetOutputAgentClient:
        return AgentsInstancesGetOutputAgentClient(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_connected_at=datetime.fromisoformat(data.get('last_connected_at').replace('Z', '+00:00')) if data.get('last_connected_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AgentsInstancesGetOutputAgentClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAgentsInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AgentsInstancesGetOutput:
        return AgentsInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        version=data.get('version'),
        description=data.get('description'),
        agent_id=data.get('agent_id'),
        agent_client=mapAgentsInstancesGetOutputAgentClient.from_dict(data.get('agent_client')) if data.get('agent_client') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_connected_at=datetime.fromisoformat(data.get('last_connected_at').replace('Z', '+00:00')) if data.get('last_connected_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AgentsInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

