from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester:
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
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor:
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
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester:
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
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity
    parties: List[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties]
    credential_overrides: List[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyOutput:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester
    identity_id: str
    delegation: ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None


class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsDenyOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyOutput:
        return ManagementInstanceIdentitiesDelegationRequestsDenyOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapManagementInstanceIdentitiesDelegationRequestsDenyOutputDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIdentitiesDelegationRequestsDenyQuery:
    allow_deleted: Optional[bool] = None


class mapManagementInstanceIdentitiesDelegationRequestsDenyQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsDenyQuery:
        return ManagementInstanceIdentitiesDelegationRequestsDenyQuery(
        allow_deleted=data.get('allow_deleted')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsDenyQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

