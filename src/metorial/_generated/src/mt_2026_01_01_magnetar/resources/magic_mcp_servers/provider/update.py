from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpServersProviderUpdateOutputDeployment:
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
class MagicMcpServersProviderUpdateOutputConfig:
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
class MagicMcpServersProviderUpdateOutputAuthConfig:
    object: str
    id: str
@dataclass
class MagicMcpServersProviderUpdateOutput:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    magic_mcp_server_id: str
    deployment: MagicMcpServersProviderUpdateOutputDeployment
    config: MagicMcpServersProviderUpdateOutputConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[MagicMcpServersProviderUpdateOutputAuthConfig] = None


class mapMagicMcpServersProviderUpdateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersProviderUpdateOutputDeployment:
        return MagicMcpServersProviderUpdateOutputDeployment(
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
    def to_dict(value: Union[MagicMcpServersProviderUpdateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersProviderUpdateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersProviderUpdateOutputConfig:
        return MagicMcpServersProviderUpdateOutputConfig(
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
    def to_dict(value: Union[MagicMcpServersProviderUpdateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersProviderUpdateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersProviderUpdateOutputAuthConfig:
        return MagicMcpServersProviderUpdateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersProviderUpdateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersProviderUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersProviderUpdateOutput:
        return MagicMcpServersProviderUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        deployment=mapMagicMcpServersProviderUpdateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapMagicMcpServersProviderUpdateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapMagicMcpServersProviderUpdateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersProviderUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpServersProviderUpdateBody:
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None


class mapMagicMcpServersProviderUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersProviderUpdateBody:
        return MagicMcpServersProviderUpdateBody(
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersProviderUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

