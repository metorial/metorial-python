from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutput:
    object: str
    visibility: str
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    schema: Optional[ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema] = None


class mapManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema:
        return ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutput:
        return ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutput(
        object=data.get('object'),
        schema=mapManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutputSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        visibility=data.get('visibility'),
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaQuery:
    provider_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    provider_version_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None


class mapManagementInstanceProviderDeploymentsConfigsGetConfigSchemaQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaQuery:
        return ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaQuery(
        provider_id=data.get('provider_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_version_id=data.get('provider_version_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsConfigsGetConfigSchemaQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

