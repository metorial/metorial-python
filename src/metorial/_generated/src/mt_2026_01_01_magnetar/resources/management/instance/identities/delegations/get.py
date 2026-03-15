from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIdentitiesDelegationsGetOutputAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationsGetOutputIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsGetOutputPartiesActor:
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
class ManagementInstanceIdentitiesDelegationsGetOutputParties:
    object: str
    id: str
    roles: List[str]
    actor: ManagementInstanceIdentitiesDelegationsGetOutputPartiesActor
    created_at: datetime
@dataclass
class ManagementInstanceIdentitiesDelegationsGetOutputRequestRequester:
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
class ManagementInstanceIdentitiesDelegationsGetOutputRequest:
    object: str
    id: str
    status: str
    requester: ManagementInstanceIdentitiesDelegationsGetOutputRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIdentitiesDelegationsGetOutput:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: ManagementInstanceIdentitiesDelegationsGetOutputIdentity
    parties: List[ManagementInstanceIdentitiesDelegationsGetOutputParties]
    credential_overrides: List[ManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[ManagementInstanceIdentitiesDelegationsGetOutputAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[ManagementInstanceIdentitiesDelegationsGetOutputRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapManagementInstanceIdentitiesDelegationsGetOutputAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputAttestation:
        return ManagementInstanceIdentitiesDelegationsGetOutputAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputIdentity:
        return ManagementInstanceIdentitiesDelegationsGetOutputIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutputPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputPartiesActor:
        return ManagementInstanceIdentitiesDelegationsGetOutputPartiesActor(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutputParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputParties:
        return ManagementInstanceIdentitiesDelegationsGetOutputParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapManagementInstanceIdentitiesDelegationsGetOutputPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutputRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputRequestRequester:
        return ManagementInstanceIdentitiesDelegationsGetOutputRequestRequester(
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
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputRequest:
        return ManagementInstanceIdentitiesDelegationsGetOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapManagementInstanceIdentitiesDelegationsGetOutputRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides:
        return ManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIdentitiesDelegationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIdentitiesDelegationsGetOutput:
        return ManagementInstanceIdentitiesDelegationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapManagementInstanceIdentitiesDelegationsGetOutputAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapManagementInstanceIdentitiesDelegationsGetOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapManagementInstanceIdentitiesDelegationsGetOutputParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapManagementInstanceIdentitiesDelegationsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapManagementInstanceIdentitiesDelegationsGetOutputCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIdentitiesDelegationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

