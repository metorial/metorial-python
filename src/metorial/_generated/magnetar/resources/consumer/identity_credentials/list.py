from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerIdentityCredentialsListOutputItems:
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
class ConsumerIdentityCredentialsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerIdentityCredentialsListOutput:
    items: List[ConsumerIdentityCredentialsListOutputItems]
    pagination: ConsumerIdentityCredentialsListOutputPagination


class mapConsumerIdentityCredentialsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerIdentityCredentialsListOutputItems:
        return ConsumerIdentityCredentialsListOutputItems(
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
    def to_dict(value: Union[ConsumerIdentityCredentialsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerIdentityCredentialsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerIdentityCredentialsListOutputPagination:
        return ConsumerIdentityCredentialsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerIdentityCredentialsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerIdentityCredentialsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerIdentityCredentialsListOutput:
        return ConsumerIdentityCredentialsListOutput(
        items=[mapConsumerIdentityCredentialsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerIdentityCredentialsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerIdentityCredentialsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerIdentityCredentialsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_id: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapConsumerIdentityCredentialsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerIdentityCredentialsListQuery:
        return ConsumerIdentityCredentialsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_id=data.get('provider_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerIdentityCredentialsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

