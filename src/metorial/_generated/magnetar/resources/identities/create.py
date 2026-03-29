from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesCreateOutputOwnerActor:
    object: str
    id: str
    type: str
    status: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    agent_id: Optional[str] = None
@dataclass
class IdentitiesCreateOutputOwner:
    type: str
    actor: IdentitiesCreateOutputOwnerActor
@dataclass
class IdentitiesCreateOutputCredentials:
    object: str
    id: str
    status: str
    identity_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    deployment_id: Optional[str] = None
    config_id: Optional[str] = None
    auth_config_id: Optional[str] = None
    delegation_config_id: Optional[str] = None
@dataclass
class IdentitiesCreateOutput:
    object: str
    id: str
    status: str
    owner: IdentitiesCreateOutputOwner
    credentials: List[IdentitiesCreateOutputCredentials]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None


class mapIdentitiesCreateOutputOwnerActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCreateOutputOwnerActor:
        return IdentitiesCreateOutputOwnerActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        agent_id=data.get('agent_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCreateOutputOwnerActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesCreateOutputOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCreateOutputOwner:
        return IdentitiesCreateOutputOwner(
        type=data.get('type'),
        actor=mapIdentitiesCreateOutputOwnerActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCreateOutputOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesCreateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCreateOutputCredentials:
        return IdentitiesCreateOutputCredentials(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        identity_id=data.get('identity_id'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        config_id=data.get('config_id'),
        auth_config_id=data.get('auth_config_id'),
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCreateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCreateOutput:
        return IdentitiesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        owner=mapIdentitiesCreateOutputOwner.from_dict(data.get('owner')) if data.get('owner') else None,
        credentials=[mapIdentitiesCreateOutputCredentials.from_dict(item) for item in data.get('credentials', []) if item],
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesCreateBodyCredentials:
    deployment_id: Optional[str] = None
    config_id: Optional[str] = None
    auth_config_id: Optional[str] = None
    delegation_config_id: Optional[str] = None
@dataclass
class IdentitiesCreateBody:
    actor_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    credentials: Optional[List[IdentitiesCreateBodyCredentials]] = None


class mapIdentitiesCreateBodyCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCreateBodyCredentials:
        return IdentitiesCreateBodyCredentials(
        deployment_id=data.get('deployment_id'),
        config_id=data.get('config_id'),
        auth_config_id=data.get('auth_config_id'),
        delegation_config_id=data.get('delegation_config_id')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCreateBodyCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCreateBody:
        return IdentitiesCreateBody(
        actor_id=data.get('actor_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        credentials=[mapIdentitiesCreateBodyCredentials.from_dict(item) for item in data.get('credentials', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

