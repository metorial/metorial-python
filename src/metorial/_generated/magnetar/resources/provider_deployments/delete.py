from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsDeleteOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsDeleteOutputLockedVersion:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderDeploymentsDeleteOutputDefaultConfig:
    id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsDeleteOutput:
    object: str
    id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider: Optional[ProviderDeploymentsDeleteOutputProvider] = None
    locked_version: Optional[ProviderDeploymentsDeleteOutputLockedVersion] = None
    default_config: Optional[ProviderDeploymentsDeleteOutputDefaultConfig] = None


class mapProviderDeploymentsDeleteOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsDeleteOutputProvider:
        return ProviderDeploymentsDeleteOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsDeleteOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsDeleteOutputLockedVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsDeleteOutputLockedVersion:
        return ProviderDeploymentsDeleteOutputLockedVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsDeleteOutputLockedVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsDeleteOutputDefaultConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsDeleteOutputDefaultConfig:
        return ProviderDeploymentsDeleteOutputDefaultConfig(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsDeleteOutputDefaultConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsDeleteOutput:
        return ProviderDeploymentsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider=mapProviderDeploymentsDeleteOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        locked_version=mapProviderDeploymentsDeleteOutputLockedVersion.from_dict(data.get('locked_version')) if data.get('locked_version') else None,
        default_config=mapProviderDeploymentsDeleteOutputDefaultConfig.from_dict(data.get('default_config')) if data.get('default_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
