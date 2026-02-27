from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsAuthCredentialsCreateOutput:
    object: str
    id: str
    type: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProviderDeploymentsAuthCredentialsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthCredentialsCreateOutput:
        return ProviderDeploymentsAuthCredentialsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthCredentialsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsAuthCredentialsCreateBodyConfig:
    type: str
    client_id: str
    client_secret: str
    scopes: List[str]
@dataclass
class ProviderDeploymentsAuthCredentialsCreateBody:
    name: str
    config: ProviderDeploymentsAuthCredentialsCreateBodyConfig
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProviderDeploymentsAuthCredentialsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthCredentialsCreateBodyConfig:
        return ProviderDeploymentsAuthCredentialsCreateBodyConfig(
        type=data.get('type'),
        client_id=data.get('clientId'),
        client_secret=data.get('clientSecret'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthCredentialsCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthCredentialsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthCredentialsCreateBody:
        return ProviderDeploymentsAuthCredentialsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        config=mapProviderDeploymentsAuthCredentialsCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthCredentialsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
