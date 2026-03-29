from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationRequestsApproveOutputRequester:
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
class IdentitiesDelegationRequestsApproveOutputDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class IdentitiesDelegationRequestsApproveOutputDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class IdentitiesDelegationRequestsApproveOutputDelegationPartiesActor:
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
class IdentitiesDelegationRequestsApproveOutputDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: IdentitiesDelegationRequestsApproveOutputDelegationPartiesActor
    created_at: datetime
@dataclass
class IdentitiesDelegationRequestsApproveOutputDelegationRequestRequester:
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
class IdentitiesDelegationRequestsApproveOutputDelegationRequest:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationRequestsApproveOutputDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class IdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationRequestsApproveOutputDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: IdentitiesDelegationRequestsApproveOutputDelegationIdentity
    parties: List[IdentitiesDelegationRequestsApproveOutputDelegationParties]
    credential_overrides: List[IdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[IdentitiesDelegationRequestsApproveOutputDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[IdentitiesDelegationRequestsApproveOutputDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationRequestsApproveOutput:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationRequestsApproveOutputRequester
    identity_id: str
    delegation: IdentitiesDelegationRequestsApproveOutputDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None


class mapIdentitiesDelegationRequestsApproveOutputRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputRequester:
        return IdentitiesDelegationRequestsApproveOutputRequester(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationAttestation:
        return IdentitiesDelegationRequestsApproveOutputDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationIdentity:
        return IdentitiesDelegationRequestsApproveOutputDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationPartiesActor:
        return IdentitiesDelegationRequestsApproveOutputDelegationPartiesActor(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationParties:
        return IdentitiesDelegationRequestsApproveOutputDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationRequestRequester:
        return IdentitiesDelegationRequestsApproveOutputDelegationRequestRequester(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationRequest:
        return IdentitiesDelegationRequestsApproveOutputDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides:
        return IdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutputDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutputDelegation:
        return IdentitiesDelegationRequestsApproveOutputDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapIdentitiesDelegationRequestsApproveOutputDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapIdentitiesDelegationRequestsApproveOutputDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapIdentitiesDelegationRequestsApproveOutputDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapIdentitiesDelegationRequestsApproveOutputDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutputDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsApproveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveOutput:
        return IdentitiesDelegationRequestsApproveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationRequestsApproveOutputRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapIdentitiesDelegationRequestsApproveOutputDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesDelegationRequestsApproveQuery:
    allow_deleted: Optional[bool] = None


class mapIdentitiesDelegationRequestsApproveQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsApproveQuery:
        return IdentitiesDelegationRequestsApproveQuery(
        allow_deleted=data.get('allow_deleted')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsApproveQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

