from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesUpdateOutputOwnerActor:
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
class ManagementInstanceIdentitiesUpdateOutputOwner:
    type: str
    actor: ManagementInstanceIdentitiesUpdateOutputOwnerActor
@dataclass
class ManagementInstanceIdentitiesUpdateOutputCredentials:
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
class ManagementInstanceIdentitiesUpdateOutput:
    object: str
    id: str
    status: str
    owner: ManagementInstanceIdentitiesUpdateOutputOwner
    credentials: List[ManagementInstanceIdentitiesUpdateOutputCredentials]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None


class mapManagementInstanceIdentitiesUpdateOutputOwnerActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesUpdateOutputOwnerActor:
        return ManagementInstanceIdentitiesUpdateOutputOwnerActor(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesUpdateOutputOwnerActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesUpdateOutputOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesUpdateOutputOwner:
        return ManagementInstanceIdentitiesUpdateOutputOwner(
        type=data.get('type'),
        actor=mapManagementInstanceIdentitiesUpdateOutputOwnerActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesUpdateOutputOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesUpdateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesUpdateOutputCredentials:
        return ManagementInstanceIdentitiesUpdateOutputCredentials(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesUpdateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesUpdateOutput:
        return ManagementInstanceIdentitiesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        owner=mapManagementInstanceIdentitiesUpdateOutputOwner.from_dict(data.get('owner')) if data.get('owner') else None,
        credentials=[mapManagementInstanceIdentitiesUpdateOutputCredentials.from_dict(item) for item in data.get('credentials', []) if item],
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIdentitiesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceIdentitiesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesUpdateBody:
        return ManagementInstanceIdentitiesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

