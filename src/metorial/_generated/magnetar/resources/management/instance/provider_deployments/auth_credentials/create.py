from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput:
    object: str
    id: str
    type: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput:
        return ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig:
    type: str
    client_id: str
    client_secret: str
    scopes: List[str]
@dataclass
class ManagementInstanceProviderDeploymentsAuthCredentialsCreateBody:
    name: str
    config: ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig:
        return ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig(
        type=data.get('type'),
        client_id=data.get('clientId'),
        client_secret=data.get('clientSecret'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthCredentialsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthCredentialsCreateBody:
        return ManagementInstanceProviderDeploymentsAuthCredentialsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        config=mapManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthCredentialsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
