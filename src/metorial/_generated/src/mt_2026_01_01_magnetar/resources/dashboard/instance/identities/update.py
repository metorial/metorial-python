from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesUpdateOutputOwnerActor:
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
class DashboardInstanceIdentitiesUpdateOutputOwner:
    type: str
    actor: DashboardInstanceIdentitiesUpdateOutputOwnerActor
@dataclass
class DashboardInstanceIdentitiesUpdateOutputCredentials:
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
class DashboardInstanceIdentitiesUpdateOutput:
    object: str
    id: str
    status: str
    owner: DashboardInstanceIdentitiesUpdateOutputOwner
    credentials: List[DashboardInstanceIdentitiesUpdateOutputCredentials]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None


class mapDashboardInstanceIdentitiesUpdateOutputOwnerActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesUpdateOutputOwnerActor:
        return DashboardInstanceIdentitiesUpdateOutputOwnerActor(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesUpdateOutputOwnerActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesUpdateOutputOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesUpdateOutputOwner:
        return DashboardInstanceIdentitiesUpdateOutputOwner(
        type=data.get('type'),
        actor=mapDashboardInstanceIdentitiesUpdateOutputOwnerActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesUpdateOutputOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesUpdateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesUpdateOutputCredentials:
        return DashboardInstanceIdentitiesUpdateOutputCredentials(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesUpdateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesUpdateOutput:
        return DashboardInstanceIdentitiesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        owner=mapDashboardInstanceIdentitiesUpdateOutputOwner.from_dict(data.get('owner')) if data.get('owner') else None,
        credentials=[mapDashboardInstanceIdentitiesUpdateOutputCredentials.from_dict(item) for item in data.get('credentials', []) if item],
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIdentitiesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceIdentitiesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesUpdateBody:
        return DashboardInstanceIdentitiesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

