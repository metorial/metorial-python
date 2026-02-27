from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    object: str
    id: str
    type: str
    provider_id: str
    provider_auth_method_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput:
    object: str
    id: str
    type: str
    status: str
    provider_id: str
    provider_auth_method_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None
    expires_at: Optional[datetime] = None
    auth_config: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        redirect_url=data.get('redirect_url'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None,
        auth_config=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBody:
    provider_auth_method_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_auth_credentials_id: Optional[str] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBody:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_auth_method_id=data.get('providerAuthMethodId'),
        provider_auth_credentials_id=data.get('providerAuthCredentialsId'),
        redirect_url=data.get('redirectUrl')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
