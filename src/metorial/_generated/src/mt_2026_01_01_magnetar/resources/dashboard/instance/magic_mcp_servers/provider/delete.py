from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpServersProviderDeleteOutputDeployment:
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
class DashboardInstanceMagicMcpServersProviderDeleteOutputConfig:
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
class DashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceMagicMcpServersProviderDeleteOutput:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    magic_mcp_server_id: str
    deployment: DashboardInstanceMagicMcpServersProviderDeleteOutputDeployment
    config: DashboardInstanceMagicMcpServersProviderDeleteOutputConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[DashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig] = None


class mapDashboardInstanceMagicMcpServersProviderDeleteOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderDeleteOutputDeployment:
        return DashboardInstanceMagicMcpServersProviderDeleteOutputDeployment(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderDeleteOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderDeleteOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderDeleteOutputConfig:
        return DashboardInstanceMagicMcpServersProviderDeleteOutputConfig(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderDeleteOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig:
        return DashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersProviderDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersProviderDeleteOutput:
        return DashboardInstanceMagicMcpServersProviderDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        deployment=mapDashboardInstanceMagicMcpServersProviderDeleteOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceMagicMcpServersProviderDeleteOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceMagicMcpServersProviderDeleteOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersProviderDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

