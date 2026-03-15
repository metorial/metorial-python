from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesCreateOutputOwnerActor:
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
class DashboardInstanceIdentitiesCreateOutputOwner:
    type: str
    actor: DashboardInstanceIdentitiesCreateOutputOwnerActor
@dataclass
class DashboardInstanceIdentitiesCreateOutputCredentials:
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
class DashboardInstanceIdentitiesCreateOutput:
    object: str
    id: str
    status: str
    owner: DashboardInstanceIdentitiesCreateOutputOwner
    credentials: List[DashboardInstanceIdentitiesCreateOutputCredentials]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None


class mapDashboardInstanceIdentitiesCreateOutputOwnerActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesCreateOutputOwnerActor:
        return DashboardInstanceIdentitiesCreateOutputOwnerActor(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesCreateOutputOwnerActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesCreateOutputOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesCreateOutputOwner:
        return DashboardInstanceIdentitiesCreateOutputOwner(
        type=data.get('type'),
        actor=mapDashboardInstanceIdentitiesCreateOutputOwnerActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesCreateOutputOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesCreateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesCreateOutputCredentials:
        return DashboardInstanceIdentitiesCreateOutputCredentials(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesCreateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesCreateOutput:
        return DashboardInstanceIdentitiesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        owner=mapDashboardInstanceIdentitiesCreateOutputOwner.from_dict(data.get('owner')) if data.get('owner') else None,
        credentials=[mapDashboardInstanceIdentitiesCreateOutputCredentials.from_dict(item) for item in data.get('credentials', []) if item],
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIdentitiesCreateBodyCredentials:
    deployment_id: Optional[str] = None
    config_id: Optional[str] = None
    auth_config_id: Optional[str] = None
    delegation_config_id: Optional[str] = None
@dataclass
class DashboardInstanceIdentitiesCreateBody:
    actor_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    credentials: Optional[List[DashboardInstanceIdentitiesCreateBodyCredentials]] = None


class mapDashboardInstanceIdentitiesCreateBodyCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesCreateBodyCredentials:
        return DashboardInstanceIdentitiesCreateBodyCredentials(
        deployment_id=data.get('deployment_id'),
        config_id=data.get('config_id'),
        auth_config_id=data.get('auth_config_id'),
        delegation_config_id=data.get('delegation_config_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesCreateBodyCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesCreateBody:
        return DashboardInstanceIdentitiesCreateBody(
        actor_id=data.get('actor_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        credentials=[mapDashboardInstanceIdentitiesCreateBodyCredentials.from_dict(item) for item in data.get('credentials', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

