from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsUpdateOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsUpdateOutputLockedVersion:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderDeploymentsUpdateOutputDefaultConfig:
    id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsUpdateOutput:
    object: str
    id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider: Optional[ProviderDeploymentsUpdateOutputProvider] = None
    locked_version: Optional[ProviderDeploymentsUpdateOutputLockedVersion] = None
    default_config: Optional[ProviderDeploymentsUpdateOutputDefaultConfig] = None


class mapProviderDeploymentsUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsUpdateOutputProvider:
        return ProviderDeploymentsUpdateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsUpdateOutputLockedVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsUpdateOutputLockedVersion:
        return ProviderDeploymentsUpdateOutputLockedVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsUpdateOutputLockedVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsUpdateOutputDefaultConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsUpdateOutputDefaultConfig:
        return ProviderDeploymentsUpdateOutputDefaultConfig(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsUpdateOutputDefaultConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsUpdateOutput:
        return ProviderDeploymentsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider=mapProviderDeploymentsUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        locked_version=mapProviderDeploymentsUpdateOutputLockedVersion.from_dict(data.get('locked_version')) if data.get('locked_version') else None,
        default_config=mapProviderDeploymentsUpdateOutputDefaultConfig.from_dict(data.get('default_config')) if data.get('default_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProviderDeploymentsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsUpdateBody:
        return ProviderDeploymentsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
