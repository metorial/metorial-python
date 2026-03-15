from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationsListOutputItemsAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class IdentitiesDelegationsListOutputItemsIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class IdentitiesDelegationsListOutputItemsPartiesActor:
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
class IdentitiesDelegationsListOutputItemsParties:
    object: str
    id: str
    roles: List[str]
    actor: IdentitiesDelegationsListOutputItemsPartiesActor
    created_at: datetime
@dataclass
class IdentitiesDelegationsListOutputItemsRequestRequester:
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
class IdentitiesDelegationsListOutputItemsRequest:
    object: str
    id: str
    status: str
    requester: IdentitiesDelegationsListOutputItemsRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class IdentitiesDelegationsListOutputItemsCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationsListOutputItems:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: IdentitiesDelegationsListOutputItemsIdentity
    parties: List[IdentitiesDelegationsListOutputItemsParties]
    credential_overrides: List[IdentitiesDelegationsListOutputItemsCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[IdentitiesDelegationsListOutputItemsAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[IdentitiesDelegationsListOutputItemsRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class IdentitiesDelegationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IdentitiesDelegationsListOutput:
    items: List[IdentitiesDelegationsListOutputItems]
    pagination: IdentitiesDelegationsListOutputPagination


class mapIdentitiesDelegationsListOutputItemsAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsAttestation:
        return IdentitiesDelegationsListOutputItemsAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItemsIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsIdentity:
        return IdentitiesDelegationsListOutputItemsIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItemsPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsPartiesActor:
        return IdentitiesDelegationsListOutputItemsPartiesActor(
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
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItemsParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsParties:
        return IdentitiesDelegationsListOutputItemsParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapIdentitiesDelegationsListOutputItemsPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItemsRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsRequestRequester:
        return IdentitiesDelegationsListOutputItemsRequestRequester(
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
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsRequest:
        return IdentitiesDelegationsListOutputItemsRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapIdentitiesDelegationsListOutputItemsRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItemsCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItemsCredentialOverrides:
        return IdentitiesDelegationsListOutputItemsCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputItemsCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputItems:
        return IdentitiesDelegationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapIdentitiesDelegationsListOutputItemsAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapIdentitiesDelegationsListOutputItemsIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapIdentitiesDelegationsListOutputItemsParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapIdentitiesDelegationsListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapIdentitiesDelegationsListOutputItemsCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutputPagination:
        return IdentitiesDelegationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListOutput:
        return IdentitiesDelegationsListOutput(
        items=[mapIdentitiesDelegationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIdentitiesDelegationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesDelegationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    permissions: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    owner_actor_id: Optional[Union[str, List[str]]] = None
    delegator_actor_id: Optional[Union[str, List[str]]] = None
    delegatee_actor_id: Optional[Union[str, List[str]]] = None
    identity_id: Optional[Union[str, List[str]]] = None


class mapIdentitiesDelegationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationsListQuery:
        return IdentitiesDelegationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        permissions=data.get('permissions'),
        id=data.get('id'),
        owner_actor_id=data.get('owner_actor_id'),
        delegator_actor_id=data.get('delegator_actor_id'),
        delegatee_actor_id=data.get('delegatee_actor_id'),
        identity_id=data.get('identity_id')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

