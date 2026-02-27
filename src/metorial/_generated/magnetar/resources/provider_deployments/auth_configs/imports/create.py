from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsAuthConfigsImportsCreateOutput:
    object: str
    id: str
    note: str
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = None
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None


class mapProviderDeploymentsAuthConfigsImportsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsCreateOutput:
        return ProviderDeploymentsAuthConfigsImportsCreateOutput(
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
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsAuthConfigsImportsCreateBody:
    note: str
    value: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None
    provider_auth_method_id: Optional[str] = None


class mapProviderDeploymentsAuthConfigsImportsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsCreateBody:
        return ProviderDeploymentsAuthConfigsImportsCreateBody(
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_auth_method_id=data.get('providerAuthMethodId'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
