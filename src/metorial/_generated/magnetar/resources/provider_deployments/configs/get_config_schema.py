from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsConfigsGetConfigSchemaOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsConfigsGetConfigSchemaOutput:
    object: str
    visibility: str
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    schema: Optional[ProviderDeploymentsConfigsGetConfigSchemaOutputSchema] = None


class mapProviderDeploymentsConfigsGetConfigSchemaOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsConfigsGetConfigSchemaOutputSchema:
        return ProviderDeploymentsConfigsGetConfigSchemaOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsConfigsGetConfigSchemaOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsConfigsGetConfigSchemaOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsConfigsGetConfigSchemaOutput:
        return ProviderDeploymentsConfigsGetConfigSchemaOutput(
        object=data.get('object'),
        schema=mapProviderDeploymentsConfigsGetConfigSchemaOutputSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        visibility=data.get('visibility'),
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsConfigsGetConfigSchemaOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsConfigsGetConfigSchemaQuery:
    provider_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    provider_version_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None


class mapProviderDeploymentsConfigsGetConfigSchemaQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsConfigsGetConfigSchemaQuery:
        return ProviderDeploymentsConfigsGetConfigSchemaQuery(
        provider_id=data.get('provider_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_version_id=data.get('provider_version_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsConfigsGetConfigSchemaQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

