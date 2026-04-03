from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesProvidersListOutputItemsDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class SessionTemplatesProvidersListOutputItemsConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class SessionTemplatesProvidersListOutputItemsAuthConfig:
    object: str
    id: str
@dataclass
class SessionTemplatesProvidersListOutputItems:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: SessionTemplatesProvidersListOutputItemsDeployment
    config: SessionTemplatesProvidersListOutputItemsConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[SessionTemplatesProvidersListOutputItemsAuthConfig] = None
@dataclass
class SessionTemplatesProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionTemplatesProvidersListOutput:
    items: List[SessionTemplatesProvidersListOutputItems]
    pagination: SessionTemplatesProvidersListOutputPagination


class mapSessionTemplatesProvidersListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListOutputItemsDeployment:
        return SessionTemplatesProvidersListOutputItemsDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListOutputItemsConfig:
        return SessionTemplatesProvidersListOutputItemsConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListOutputItemsAuthConfig:
        return SessionTemplatesProvidersListOutputItemsAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListOutputItems:
        return SessionTemplatesProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapSessionTemplatesProvidersListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionTemplatesProvidersListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionTemplatesProvidersListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListOutputPagination:
        return SessionTemplatesProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListOutput:
        return SessionTemplatesProvidersListOutput(
        items=[mapSessionTemplatesProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionTemplatesProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionTemplatesProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionTemplatesProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionTemplatesProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_template_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SessionTemplatesProvidersListQueryCreatedAt] = None
    updated_at: Optional[SessionTemplatesProvidersListQueryUpdatedAt] = None


class mapSessionTemplatesProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersListQuery:
        return SessionTemplatesProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        session_template_id=data.get('session_template_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        created_at=mapSessionTemplatesProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSessionTemplatesProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

