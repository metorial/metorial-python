from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesDelegationsGetOutputAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationsGetOutputIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceIdentitiesDelegationsGetOutputPartiesActor:
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
class DashboardInstanceIdentitiesDelegationsGetOutputParties:
    object: str
    id: str
    roles: List[str]
    actor: DashboardInstanceIdentitiesDelegationsGetOutputPartiesActor
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationsGetOutputRequestRequester:
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
class DashboardInstanceIdentitiesDelegationsGetOutputRequest:
    object: str
    id: str
    status: str
    requester: DashboardInstanceIdentitiesDelegationsGetOutputRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class DashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIdentitiesDelegationsGetOutput:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: DashboardInstanceIdentitiesDelegationsGetOutputIdentity
    parties: List[DashboardInstanceIdentitiesDelegationsGetOutputParties]
    credential_overrides: List[DashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[DashboardInstanceIdentitiesDelegationsGetOutputAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[DashboardInstanceIdentitiesDelegationsGetOutputRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapDashboardInstanceIdentitiesDelegationsGetOutputAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputAttestation:
        return DashboardInstanceIdentitiesDelegationsGetOutputAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputIdentity:
        return DashboardInstanceIdentitiesDelegationsGetOutputIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutputPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputPartiesActor:
        return DashboardInstanceIdentitiesDelegationsGetOutputPartiesActor(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutputParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputParties:
        return DashboardInstanceIdentitiesDelegationsGetOutputParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapDashboardInstanceIdentitiesDelegationsGetOutputPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutputRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputRequestRequester:
        return DashboardInstanceIdentitiesDelegationsGetOutputRequestRequester(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputRequest:
        return DashboardInstanceIdentitiesDelegationsGetOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapDashboardInstanceIdentitiesDelegationsGetOutputRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides:
        return DashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationsGetOutput:
        return DashboardInstanceIdentitiesDelegationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapDashboardInstanceIdentitiesDelegationsGetOutputAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapDashboardInstanceIdentitiesDelegationsGetOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapDashboardInstanceIdentitiesDelegationsGetOutputParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapDashboardInstanceIdentitiesDelegationsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapDashboardInstanceIdentitiesDelegationsGetOutputCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

