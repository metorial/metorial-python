from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerAgentsGetOutputAgent:
    object: str
    id: str
    type: str
    status: str
    name: str
    slug: str
    actor_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember:
    id: str
@dataclass
class ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember] = None
    consumer: Optional[ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer] = None
@dataclass
class ConsumerAgentsGetOutputMagicMcpEndpointsAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner] = None
@dataclass
class ConsumerAgentsGetOutputMagicMcpEndpoints:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: ConsumerAgentsGetOutputMagicMcpEndpointsAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ConsumerAgentsGetOutput:
    object: str
    agent: ConsumerAgentsGetOutputAgent
    magic_mcp_endpoints: List[ConsumerAgentsGetOutputMagicMcpEndpoints]


class mapConsumerAgentsGetOutputAgent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutputAgent:
        return ConsumerAgentsGetOutputAgent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutputAgent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember:
        return ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer:
        return ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner:
        return ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapConsumerAgentsGetOutputMagicMcpEndpointsAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsGetOutputMagicMcpEndpointsAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutputMagicMcpEndpointsAccess:
        return ConsumerAgentsGetOutputMagicMcpEndpointsAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapConsumerAgentsGetOutputMagicMcpEndpointsAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutputMagicMcpEndpointsAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsGetOutputMagicMcpEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutputMagicMcpEndpoints:
        return ConsumerAgentsGetOutputMagicMcpEndpoints(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        enable_skill_editing=data.get('enable_skill_editing'),
        access=mapConsumerAgentsGetOutputMagicMcpEndpointsAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutputMagicMcpEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsGetOutput:
        return ConsumerAgentsGetOutput(
        object=data.get('object'),
        agent=mapConsumerAgentsGetOutputAgent.from_dict(data.get('agent')) if data.get('agent') else None,
        magic_mcp_endpoints=[mapConsumerAgentsGetOutputMagicMcpEndpoints.from_dict(item) for item in data.get('magic_mcp_endpoints', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

