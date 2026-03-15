from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesCredentialsListOutputItems:
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
class IdentitiesCredentialsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IdentitiesCredentialsListOutput:
    items: List[IdentitiesCredentialsListOutputItems]
    pagination: IdentitiesCredentialsListOutputPagination


class mapIdentitiesCredentialsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCredentialsListOutputItems:
        return IdentitiesCredentialsListOutputItems(
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
    def to_dict(value: Union[IdentitiesCredentialsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesCredentialsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCredentialsListOutputPagination:
        return IdentitiesCredentialsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCredentialsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesCredentialsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCredentialsListOutput:
        return IdentitiesCredentialsListOutput(
        items=[mapIdentitiesCredentialsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIdentitiesCredentialsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCredentialsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesCredentialsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    agent_id: Optional[Union[str, List[str]]] = None
    actor_id: Optional[Union[str, List[str]]] = None
    identity_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None


class mapIdentitiesCredentialsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesCredentialsListQuery:
        return IdentitiesCredentialsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        agent_id=data.get('agent_id'),
        actor_id=data.get('actor_id'),
        identity_id=data.get('identity_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesCredentialsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

