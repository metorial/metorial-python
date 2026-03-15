from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester:
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
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation:
    object: str
    id: str
    type: str
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity:
    object: str
    id: str
    name: str
    description: str
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor:
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
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties:
    object: str
    id: str
    roles: List[str]
    actor: DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor
    created_at: datetime
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester:
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
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest:
    object: str
    id: str
    status: str
    requester: DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester
    identity_id: str
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides:
    object: str
    id: str
    status: str
    permissions: List[str]
    credential_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation:
    object: str
    id: str
    status: str
    delegation_level: float
    permissions: List[str]
    identity: DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity
    parties: List[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties]
    credential_overrides: List[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides]
    created_at: datetime
    denied_reason: Optional[str] = None
    attestation: Optional[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation] = None
    note: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
    request: Optional[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputItems:
    object: str
    id: str
    status: str
    requester: DashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester
    identity_id: str
    delegation: DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation
    expires_at: datetime
    created_at: datetime
    denied_reason: Optional[str] = None
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListOutput:
    items: List[DashboardInstanceIdentitiesDelegationRequestsListOutputItems]
    pagination: DashboardInstanceIdentitiesDelegationRequestsListOutputPagination


class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties(
        object=data.get('object'),
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationPartiesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequestRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        permissions=data.get('permissions', []),
        credential_id=data.get('credential_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        delegation_level=data.get('delegation_level'),
        permissions=data.get('permissions', []),
        attestation=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationAttestation.from_dict(data.get('attestation')) if data.get('attestation') else None,
        note=data.get('note'),
        metadata=data.get('metadata'),
        identity=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        delegation_config_id=data.get('delegation_config_id'),
        parties=[mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationParties.from_dict(item) for item in data.get('parties', []) if item],
        request=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationRequest.from_dict(data.get('request')) if data.get('request') else None,
        credential_overrides=[mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegationCredentialOverrides.from_dict(item) for item in data.get('credential_overrides', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputItems:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        denied_reason=data.get('denied_reason'),
        requester=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsRequester.from_dict(data.get('requester')) if data.get('requester') else None,
        identity_id=data.get('identity_id'),
        delegation=mapDashboardInstanceIdentitiesDelegationRequestsListOutputItemsDelegation.from_dict(data.get('delegation')) if data.get('delegation') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutputPagination:
        return DashboardInstanceIdentitiesDelegationRequestsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationRequestsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListOutput:
        return DashboardInstanceIdentitiesDelegationRequestsListOutput(
        items=[mapDashboardInstanceIdentitiesDelegationRequestsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceIdentitiesDelegationRequestsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIdentitiesDelegationRequestsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    actor_id: Optional[Union[str, List[str]]] = None
    identity_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceIdentitiesDelegationRequestsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationRequestsListQuery:
        return DashboardInstanceIdentitiesDelegationRequestsListQuery(
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
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationRequestsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

