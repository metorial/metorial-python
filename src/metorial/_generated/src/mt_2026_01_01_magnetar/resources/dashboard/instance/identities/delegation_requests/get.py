from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutputRequester:
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
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor:
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
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester:
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
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest:
    object: str
    id: str
    status: str
    requester: DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity
    parties: List[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties]
    credential_overrides: List[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetOutput:
    object: str
    id: str
    status: str
    requester: DashboardInstanceIdentitiesDelegationRequestsGetOutputRequester
    identity_id: str
    delegation: DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None


class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputRequester:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputRequester(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetOutput:
        return DashboardInstanceIdentitiesDelegationRequestsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapDashboardInstanceIdentitiesDelegationRequestsGetOutputDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIdentitiesDelegationRequestsGetQuery:
    allow_deleted: Optional[bool] = None


class mapDashboardInstanceIdentitiesDelegationRequestsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsGetQuery:
        return DashboardInstanceIdentitiesDelegationRequestsGetQuery(
        allow_deleted=data.get('allow_deleted')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

