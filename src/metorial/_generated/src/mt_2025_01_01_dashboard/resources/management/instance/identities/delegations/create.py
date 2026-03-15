from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesDelegationsCreateOutputAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationsCreateOutputIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor:
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
class ManagementInstanceIdentitiesDelegationsCreateOutputParties:
    object: str
    id: str
    roles: List[str]
    actor: ManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester:
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
class ManagementInstanceIdentitiesDelegationsCreateOutputRequest:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsCreateOutput:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: ManagementInstanceIdentitiesDelegationsCreateOutputIdentity
    parties: List[ManagementInstanceIdentitiesDelegationsCreateOutputParties]
    credential_overrides: List[ManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[ManagementInstanceIdentitiesDelegationsCreateOutputAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[ManagementInstanceIdentitiesDelegationsCreateOutputRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapManagementInstanceIdentitiesDelegationsCreateOutputAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputAttestation:
        return ManagementInstanceIdentitiesDelegationsCreateOutputAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputIdentity:
        return ManagementInstanceIdentitiesDelegationsCreateOutputIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor:
        return ManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutputParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputParties:
        return ManagementInstanceIdentitiesDelegationsCreateOutputParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapManagementInstanceIdentitiesDelegationsCreateOutputPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester:
        return ManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputRequest:
        return ManagementInstanceIdentitiesDelegationsCreateOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationsCreateOutputRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateOutput:
        return ManagementInstanceIdentitiesDelegationsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapManagementInstanceIdentitiesDelegationsCreateOutputAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapManagementInstanceIdentitiesDelegationsCreateOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapManagementInstanceIdentitiesDelegationsCreateOutputParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapManagementInstanceIdentitiesDelegationsCreateOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapManagementInstanceIdentitiesDelegationsCreateOutputCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides:
    credential_id: str
    permissions: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsCreateBody:
    identity_id: str
    delegatee_actor_id: str
    delegator_actor_id: Optional[str] = None
    permissions: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    delegation_config_id: Optional[str] = None
    credential_overrides: Optional[List[ManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides]] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides(
        credential_id=data.get('credential_id'),
        permissions=data.get('permissions', []),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsCreateBody:
        return ManagementInstanceIdentitiesDelegationsCreateBody(
        identity_id=data.get('identity_id'),
        delegator_actor_id=data.get('delegator_actor_id'),
        delegatee_actor_id=data.get('delegatee_actor_id'),
        permissions=data.get('permissions', []),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        delegation_config_id=data.get('delegation_config_id'),
        credential_overrides=[mapManagementInstanceIdentitiesDelegationsCreateBodyCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        note=data.get('note'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

