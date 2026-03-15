from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesListOutputItemsOwnerActor:
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
class IdentitiesListOutputItemsOwner:
    type: str
    actor: IdentitiesListOutputItemsOwnerActor
@dataclass
class IdentitiesListOutputItemsCredentials:
    object: str
    id: str
    status: str
    identity_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    deployment_id: Optional[str] = None
    config_id: Optional[str] = None
    auth_config_id: Optional[str] = None
    delegation_config_id: Optional[str] = None
@dataclass
class IdentitiesListOutputItems:
    object: str
    id: str
    status: str
    owner: IdentitiesListOutputItemsOwner
    credentials: List[IdentitiesListOutputItemsCredentials]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    delegation_config_id: Optional[str] = None
@dataclass
class IdentitiesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IdentitiesListOutput:
    items: List[IdentitiesListOutputItems]
    pagination: IdentitiesListOutputPagination


class mapIdentitiesListOutputItemsOwnerActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListOutputItemsOwnerActor:
        return IdentitiesListOutputItemsOwnerActor(
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
    def to_dict(value: Union[IdentitiesListOutputItemsOwnerActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesListOutputItemsOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListOutputItemsOwner:
        return IdentitiesListOutputItemsOwner(
        type=data.get('type'),
        actor=mapIdentitiesListOutputItemsOwnerActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesListOutputItemsOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesListOutputItemsCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListOutputItemsCredentials:
        return IdentitiesListOutputItemsCredentials(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        identity_id=data.get('identity_id'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        config_id=data.get('config_id'),
        auth_config_id=data.get('auth_config_id'),
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesListOutputItemsCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListOutputItems:
        return IdentitiesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        owner=mapIdentitiesListOutputItemsOwner.from_dict(data.get('owner')) if data.get('owner') else None,
        credentials=[mapIdentitiesListOutputItemsCredentials.from_dict(item) for item in data.get('credentials', []) if item],
        delegation_config_id=data.get('delegation_config_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListOutputPagination:
        return IdentitiesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListOutput:
        return IdentitiesListOutput(
        items=[mapIdentitiesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIdentitiesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    agent_id: Optional[Union[str, List[str]]] = None
    actor_id: Optional[Union[str, List[str]]] = None


class mapIdentitiesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesListQuery:
        return IdentitiesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        agent_id=data.get('agent_id'),
        actor_id=data.get('actor_id')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

