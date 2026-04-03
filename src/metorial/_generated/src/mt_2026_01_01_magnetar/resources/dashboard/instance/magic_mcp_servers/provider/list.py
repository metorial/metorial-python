from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpServersProviderListOutputItemsDeployment:
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
class DashboardInstanceMagicMcpServersProviderListOutputItemsConfig:
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
class DashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceMagicMcpServersProviderListOutputItems:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    magic_mcp_server_id: str
    deployment: DashboardInstanceMagicMcpServersProviderListOutputItemsDeployment
    config: DashboardInstanceMagicMcpServersProviderListOutputItemsConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[DashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig] = None
@dataclass
class DashboardInstanceMagicMcpServersProviderListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceMagicMcpServersProviderListOutput:
    items: List[DashboardInstanceMagicMcpServersProviderListOutputItems]
    pagination: DashboardInstanceMagicMcpServersProviderListOutputPagination


class mapDashboardInstanceMagicMcpServersProviderListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListOutputItemsDeployment:
        return DashboardInstanceMagicMcpServersProviderListOutputItemsDeployment(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListOutputItemsConfig:
        return DashboardInstanceMagicMcpServersProviderListOutputItemsConfig(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig:
        return DashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListOutputItems:
        return DashboardInstanceMagicMcpServersProviderListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        deployment=mapDashboardInstanceMagicMcpServersProviderListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceMagicMcpServersProviderListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceMagicMcpServersProviderListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListOutputPagination:
        return DashboardInstanceMagicMcpServersProviderListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListOutput:
        return DashboardInstanceMagicMcpServersProviderListOutput(
        items=[mapDashboardInstanceMagicMcpServersProviderListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceMagicMcpServersProviderListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpServersProviderListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceMagicMcpServersProviderListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceMagicMcpServersProviderListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceMagicMcpServersProviderListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceMagicMcpServersProviderListQueryUpdatedAt] = None


class mapDashboardInstanceMagicMcpServersProviderListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderListQuery:
        return DashboardInstanceMagicMcpServersProviderListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        created_at=mapDashboardInstanceMagicMcpServersProviderListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceMagicMcpServersProviderListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

