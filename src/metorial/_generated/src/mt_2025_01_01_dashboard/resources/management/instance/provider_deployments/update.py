from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsUpdateOutputLockedVersion:
    object: str
    id: str
    version: str
    provider_id: str
    is_current: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    specification_id: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig:
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
class ManagementInstanceProviderDeploymentsUpdateOutput:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    locked_version: Optional[ManagementInstanceProviderDeploymentsUpdateOutputLockedVersion] = None
    default_config: Optional[ManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig] = None


class mapManagementInstanceProviderDeploymentsUpdateOutputLockedVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsUpdateOutputLockedVersion:
        return ManagementInstanceProviderDeploymentsUpdateOutputLockedVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsUpdateOutputLockedVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig:
        return ManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsUpdateOutput:
        return ManagementInstanceProviderDeploymentsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        locked_version=mapManagementInstanceProviderDeploymentsUpdateOutputLockedVersion.from_dict(data.get('locked_version')) if data.get('locked_version') else None,
        default_config=mapManagementInstanceProviderDeploymentsUpdateOutputDefaultConfig.from_dict(data.get('default_config')) if data.get('default_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsUpdateBody:
        return ManagementInstanceProviderDeploymentsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
