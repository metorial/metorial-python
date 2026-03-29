from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester:
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
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor:
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
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester:
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
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity
    parties: List[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties]
    credential_overrides: List[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveOutput:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester
    identity_id: str
    delegation: ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None


class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationRequestsApproveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveOutput:
        return ManagementInstanceIdentitiesDelegationRequestsApproveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapManagementInstanceIdentitiesDelegationRequestsApproveOutputDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIdentitiesDelegationRequestsApproveQuery:
    allow_deleted: Optional[bool] = None


class mapManagementInstanceIdentitiesDelegationRequestsApproveQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationRequestsApproveQuery:
        return ManagementInstanceIdentitiesDelegationRequestsApproveQuery(
        allow_deleted=data.get('allow_deleted')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationRequestsApproveQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

