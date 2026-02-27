from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsConfigVaultsCreateOutput:
    object: str
    id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None


class mapProviderDeploymentsConfigVaultsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsConfigVaultsCreateOutput:
        return ProviderDeploymentsConfigVaultsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsConfigVaultsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsConfigVaultsCreateBody:
    name: str
    data: Dict[str, Any]
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProviderDeploymentsConfigVaultsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsConfigVaultsCreateBody:
        return ProviderDeploymentsConfigVaultsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        data=data.get('data')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsConfigVaultsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
