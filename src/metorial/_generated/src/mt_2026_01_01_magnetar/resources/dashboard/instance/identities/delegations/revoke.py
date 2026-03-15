from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesDelegationsRevokeOutputAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationsRevokeOutputIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor:
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
class DashboardInstanceIdentitiesDelegationsRevokeOutputParties:
    object: str
    id: str
    roles: List[str]
    actor: DashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester:
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
class DashboardInstanceIdentitiesDelegationsRevokeOutputRequest:
    object: str
    id: str
    status: str
    requester: DashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class DashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIdentitiesDelegationsRevokeOutput:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: DashboardInstanceIdentitiesDelegationsRevokeOutputIdentity
    parties: List[DashboardInstanceIdentitiesDelegationsRevokeOutputParties]
    credential_overrides: List[DashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[DashboardInstanceIdentitiesDelegationsRevokeOutputAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[DashboardInstanceIdentitiesDelegationsRevokeOutputRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapDashboardInstanceIdentitiesDelegationsRevokeOutputAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputAttestation:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputIdentity:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutputParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputParties:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapDashboardInstanceIdentitiesDelegationsRevokeOutputPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputRequest:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapDashboardInstanceIdentitiesDelegationsRevokeOutputRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides:
        return DashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsRevokeOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsRevokeOutput:
        return DashboardInstanceIdentitiesDelegationsRevokeOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapDashboardInstanceIdentitiesDelegationsRevokeOutputAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapDashboardInstanceIdentitiesDelegationsRevokeOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapDashboardInstanceIdentitiesDelegationsRevokeOutputParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapDashboardInstanceIdentitiesDelegationsRevokeOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapDashboardInstanceIdentitiesDelegationsRevokeOutputCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsRevokeOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

