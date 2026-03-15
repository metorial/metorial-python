from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationsCreateOutputAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class IdentitiesDelegationsCreateOutputIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class IdentitiesDelegationsCreateOutputPartiesActor:
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
class IdentitiesDelegationsCreateOutputParties:
    object: str
    id: str
    roles: List[str]
    actor: IdentitiesDelegationsCreateOutputPartiesActor
    created_at: datetime
@dataclass
class IdentitiesDelegationsCreateOutputRequestRequester:
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
class IdentitiesDelegationsCreateOutputRequest:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationsCreateOutputRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class IdentitiesDelegationsCreateOutputCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationsCreateOutput:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: IdentitiesDelegationsCreateOutputIdentity
    parties: List[IdentitiesDelegationsCreateOutputParties]
    credential_overrides: List[IdentitiesDelegationsCreateOutputCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[IdentitiesDelegationsCreateOutputAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[IdentitiesDelegationsCreateOutputRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapIdentitiesDelegationsCreateOutputAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputAttestation:
        return IdentitiesDelegationsCreateOutputAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputIdentity:
        return IdentitiesDelegationsCreateOutputIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutputPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputPartiesActor:
        return IdentitiesDelegationsCreateOutputPartiesActor(
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
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutputParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputParties:
        return IdentitiesDelegationsCreateOutputParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapIdentitiesDelegationsCreateOutputPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutputRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputRequestRequester:
        return IdentitiesDelegationsCreateOutputRequestRequester(
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
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputRequest:
        return IdentitiesDelegationsCreateOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationsCreateOutputRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutputCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutputCredentialOverrides:
        return IdentitiesDelegationsCreateOutputCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateOutputCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateOutput:
        return IdentitiesDelegationsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapIdentitiesDelegationsCreateOutputAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapIdentitiesDelegationsCreateOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapIdentitiesDelegationsCreateOutputParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapIdentitiesDelegationsCreateOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapIdentitiesDelegationsCreateOutputCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesDelegationsCreateBodyCredentialOverrides:
    credential_id: str
    permissions: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationsCreateBody:
    identity_id: str
    delegatee_actor_id: str
    delegator_actor_id: Optional[str] = None
    permissions: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    delegation_config_id: Optional[str] = None
    credential_overrides: Optional[List[IdentitiesDelegationsCreateBodyCredentialOverrides]] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapIdentitiesDelegationsCreateBodyCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateBodyCredentialOverrides:
        return IdentitiesDelegationsCreateBodyCredentialOverrides(
        credential_id=data.get('credential_id'),
        permissions=data.get('permissions', []),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateBodyCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsCreateBody:
        return IdentitiesDelegationsCreateBody(
        identity_id=data.get('identity_id'),
        delegator_actor_id=data.get('delegator_actor_id'),
        delegatee_actor_id=data.get('delegatee_actor_id'),
        permissions=data.get('permissions', []),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        delegation_config_id=data.get('delegation_config_id'),
        credential_overrides=[mapIdentitiesDelegationsCreateBodyCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        note=data.get('note'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

