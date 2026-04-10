from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderTemplatesCreateOutput:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider_deployment_id: str
    tool_filters: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapProviderTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderTemplatesCreateOutput:
        return ProviderTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_deployment_id=data.get('provider_deployment_id'),
        tool_filters=data.get('tool_filters'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderTemplatesCreateBodyProviderDeployment:
    provider_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    locked_provider_version_id: Optional[str] = None
@dataclass
class ProviderTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filers: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    provider_deployment_id: Optional[str] = None
    provider_deployment: Optional[ProviderTemplatesCreateBodyProviderDeployment] = None


class mapProviderTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderTemplatesCreateBody:
        return ProviderTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filers=data.get('tool_filers'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_deployment=data.get('provider_deployment')
        )

    @staticmethod
    def to_dict(value: Union[ProviderTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

