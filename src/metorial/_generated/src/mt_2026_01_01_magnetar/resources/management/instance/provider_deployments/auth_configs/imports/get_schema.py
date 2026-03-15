from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
    object: str
    visibility: str
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput(
        object=data.get('object'),
        schema=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutputSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        visibility=data.get('visibility'),
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery:
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        provider_auth_method_id=data.get('provider_auth_method_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

