from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput:
    object: str
    id: str
    type: str
    status: str
    is_default: bool
    is_managed: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scopes: Optional[List[str]] = None


class mapManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput:
        return ManagementInstanceProviderDeploymentsAuthCredentialsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        is_managed=data.get('is_managed'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        scopes=data.get('scopes', []),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
    client_id: str
    client_secret: str
    scopes: List[str]
    type: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthCredentialsCreateBody:
    provider_id: str
    config: ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig:
        return ManagementInstanceProviderDeploymentsAuthCredentialsCreateBodyConfig(
        type=data.get('type'),
        client_id=data.get('client_id'),
        client_secret=data.get('client_secret'),
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
        provider_id=data.get('provider_id'),
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

