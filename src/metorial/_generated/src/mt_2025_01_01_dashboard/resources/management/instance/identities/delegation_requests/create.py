from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester:
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
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor:
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
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester:
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
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity
    parties: List[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties]
    credential_overrides: List[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateOutput:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester
    identity_id: str
    delegation: ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None


class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateOutput:
        return ManagementInstanceIdentitiesDelegationRequestsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapManagementInstanceIdentitiesDelegationRequestsCreateOutputDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides:
    credential_id: str
    permissions: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsCreateBody:
    identity_id: str
    requester_actor_id: str
    expires_at: datetime
    delegator_actor_id: Optional[str] = None
    permissions: Optional[List[str]] = None
    delegation_config_id: Optional[str] = None
    credential_overrides: Optional[List[ManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides]] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides(
        credential_id=data.get('credential_id'),
        permissions=data.get('permissions', []),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsCreateBody:
        return ManagementInstanceIdentitiesDelegationRequestsCreateBody(
        identity_id=data.get('identity_id'),
        requester_actor_id=data.get('requester_actor_id'),
        delegator_actor_id=data.get('delegator_actor_id'),
        permissions=data.get('permissions', []),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        delegation_config_id=data.get('delegation_config_id'),
        credential_overrides=[mapManagementInstanceIdentitiesDelegationRequestsCreateBodyCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        note=data.get('note'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

