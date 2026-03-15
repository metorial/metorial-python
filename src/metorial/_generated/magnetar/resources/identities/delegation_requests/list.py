from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationRequestsListOutputItemsRequester:
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
class IdentitiesDelegationRequestsListOutputItemsDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class IdentitiesDelegationRequestsListOutputItemsDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class IdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor:
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
class IdentitiesDelegationRequestsListOutputItemsDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: IdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor
    created_at: datetime
@dataclass
class IdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester:
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
class IdentitiesDelegationRequestsListOutputItemsDelegationRequest:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class IdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationRequestsListOutputItemsDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: IdentitiesDelegationRequestsListOutputItemsDelegationIdentity
    parties: List[IdentitiesDelegationRequestsListOutputItemsDelegationParties]
    credential_overrides: List[IdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[IdentitiesDelegationRequestsListOutputItemsDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[IdentitiesDelegationRequestsListOutputItemsDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationRequestsListOutputItems:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationRequestsListOutputItemsRequester
    identity_id: str
    delegation: IdentitiesDelegationRequestsListOutputItemsDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class IdentitiesDelegationRequestsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IdentitiesDelegationRequestsListOutput:
    items: List[IdentitiesDelegationRequestsListOutputItems]
    pagination: IdentitiesDelegationRequestsListOutputPagination


class mapIdentitiesDelegationRequestsListOutputItemsRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsRequester:
        return IdentitiesDelegationRequestsListOutputItemsRequester(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationAttestation:
        return IdentitiesDelegationRequestsListOutputItemsDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationIdentity:
        return IdentitiesDelegationRequestsListOutputItemsDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor:
        return IdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationParties:
        return IdentitiesDelegationRequestsListOutputItemsDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester:
        return IdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester(
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
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationRequest:
        return IdentitiesDelegationRequestsListOutputItemsDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides:
        return IdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItemsDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItemsDelegation:
        return IdentitiesDelegationRequestsListOutputItemsDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapIdentitiesDelegationRequestsListOutputItemsDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapIdentitiesDelegationRequestsListOutputItemsDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapIdentitiesDelegationRequestsListOutputItemsDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapIdentitiesDelegationRequestsListOutputItemsDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItemsDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputItems:
        return IdentitiesDelegationRequestsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationRequestsListOutputItemsRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapIdentitiesDelegationRequestsListOutputItemsDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutputPagination:
        return IdentitiesDelegationRequestsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationRequestsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListOutput:
        return IdentitiesDelegationRequestsListOutput(
        items=[mapIdentitiesDelegationRequestsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIdentitiesDelegationRequestsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesDelegationRequestsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    actor_id: Optional[Union[str, List[str]]] = None
    identity_id: Optional[Union[str, List[str]]] = None


class mapIdentitiesDelegationRequestsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationRequestsListQuery:
        return IdentitiesDelegationRequestsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        actor_id=data.get('actor_id'),
        identity_id=data.get('identity_id')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationRequestsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

