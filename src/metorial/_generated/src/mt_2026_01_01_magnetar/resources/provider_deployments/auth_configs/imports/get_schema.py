from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
    object: str
    visibility: str
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    schema: Optional[ProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema] = None


class mapProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema:
        return ProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
        return ProviderDeploymentsAuthConfigsImportsGetSchemaOutput(
        object=data.get('object'),
        schema=mapProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        visibility=data.get('visibility'),
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsGetSchemaOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsAuthConfigsImportsGetSchemaQuery:
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None


class mapProviderDeploymentsAuthConfigsImportsGetSchemaQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsGetSchemaQuery:
        return ProviderDeploymentsAuthConfigsImportsGetSchemaQuery(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        provider_auth_method_id=data.get('provider_auth_method_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsGetSchemaQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
