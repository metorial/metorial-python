from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateOutput:
    object: str
    id: str
    note: str
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = None
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsImportsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateBody:
    note: str
    value: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None
    provider_auth_method_id: Optional[str] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsImportsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateBody:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateBody(
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_auth_method_id=data.get('providerAuthMethodId'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
