from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationRequestsGetOutputRequester:
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
class IdentitiesDelegationRequestsGetOutputDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class IdentitiesDelegationRequestsGetOutputDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class IdentitiesDelegationRequestsGetOutputDelegationPartiesActor:
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
class IdentitiesDelegationRequestsGetOutputDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: IdentitiesDelegationRequestsGetOutputDelegationPartiesActor
    created_at: datetime
@dataclass
class IdentitiesDelegationRequestsGetOutputDelegationRequestRequester:
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
class IdentitiesDelegationRequestsGetOutputDelegationRequest:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationRequestsGetOutputDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class IdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationRequestsGetOutputDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: IdentitiesDelegationRequestsGetOutputDelegationIdentity
    parties: List[IdentitiesDelegationRequestsGetOutputDelegationParties]
    credential_overrides: List[IdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[IdentitiesDelegationRequestsGetOutputDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[IdentitiesDelegationRequestsGetOutputDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationRequestsGetOutput:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationRequestsGetOutputRequester
    identity_id: str
    delegation: IdentitiesDelegationRequestsGetOutputDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None


class mapIdentitiesDelegationRequestsGetOutputRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputRequester:
        return IdentitiesDelegationRequestsGetOutputRequester(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationAttestation:
        return IdentitiesDelegationRequestsGetOutputDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationIdentity:
        return IdentitiesDelegationRequestsGetOutputDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationPartiesActor:
        return IdentitiesDelegationRequestsGetOutputDelegationPartiesActor(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationParties:
        return IdentitiesDelegationRequestsGetOutputDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapIdentitiesDelegationRequestsGetOutputDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationRequestRequester:
        return IdentitiesDelegationRequestsGetOutputDelegationRequestRequester(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationRequest:
        return IdentitiesDelegationRequestsGetOutputDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationRequestsGetOutputDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides:
        return IdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutputDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutputDelegation:
        return IdentitiesDelegationRequestsGetOutputDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapIdentitiesDelegationRequestsGetOutputDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapIdentitiesDelegationRequestsGetOutputDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapIdentitiesDelegationRequestsGetOutputDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapIdentitiesDelegationRequestsGetOutputDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutputDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetOutput:
        return IdentitiesDelegationRequestsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationRequestsGetOutputRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapIdentitiesDelegationRequestsGetOutputDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesDelegationRequestsGetQuery:
    allow_deleted: Optional[bool] = None


class mapIdentitiesDelegationRequestsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsGetQuery:
        return IdentitiesDelegationRequestsGetQuery(
        allow_deleted=data.get('allow_deleted')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

