from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProvidersToolsGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProvidersToolsGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProvidersToolsGetOutputTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceProvidersToolsGetOutput:
    object: str
    id: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    constraints: List[str]
    instructions: List[str]
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[DashboardInstanceProvidersToolsGetOutputInputSchema] = None
    output_schema: Optional[DashboardInstanceProvidersToolsGetOutputOutputSchema] = None
    tags: Optional[DashboardInstanceProvidersToolsGetOutputTags] = None


class mapDashboardInstanceProvidersToolsGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersToolsGetOutputInputSchema:
        return DashboardInstanceProvidersToolsGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersToolsGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersToolsGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersToolsGetOutputOutputSchema:
        return DashboardInstanceProvidersToolsGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersToolsGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersToolsGetOutputTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersToolsGetOutputTags:
        return DashboardInstanceProvidersToolsGetOutputTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersToolsGetOutputTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersToolsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersToolsGetOutput:
        return DashboardInstanceProvidersToolsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceProvidersToolsGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProvidersToolsGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceProvidersToolsGetOutputTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersToolsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
