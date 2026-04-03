from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpServersProviderGetOutputDeployment:
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
class ManagementInstanceMagicMcpServersProviderGetOutputConfig:
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
class ManagementInstanceMagicMcpServersProviderGetOutputAuthConfig:
    object: str
    id: str
@dataclass
class ManagementInstanceMagicMcpServersProviderGetOutput:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    magic_mcp_server_id: str
    deployment: ManagementInstanceMagicMcpServersProviderGetOutputDeployment
    config: ManagementInstanceMagicMcpServersProviderGetOutputConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[ManagementInstanceMagicMcpServersProviderGetOutputAuthConfig] = None


class mapManagementInstanceMagicMcpServersProviderGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProviderGetOutputDeployment:
        return ManagementInstanceMagicMcpServersProviderGetOutputDeployment(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProviderGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProviderGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProviderGetOutputConfig:
        return ManagementInstanceMagicMcpServersProviderGetOutputConfig(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProviderGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProviderGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProviderGetOutputAuthConfig:
        return ManagementInstanceMagicMcpServersProviderGetOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProviderGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProviderGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProviderGetOutput:
        return ManagementInstanceMagicMcpServersProviderGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        deployment=mapManagementInstanceMagicMcpServersProviderGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceMagicMcpServersProviderGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceMagicMcpServersProviderGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProviderGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

