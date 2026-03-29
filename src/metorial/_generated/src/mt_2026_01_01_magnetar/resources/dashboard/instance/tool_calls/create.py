from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceToolCallsCreateOutputToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceToolCallsCreateOutputToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceToolCallsCreateOutputToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceToolCallsCreateOutputTool:
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
    input_schema: Optional[DashboardInstanceToolCallsCreateOutputToolInputSchema] = None
    output_schema: Optional[DashboardInstanceToolCallsCreateOutputToolOutputSchema] = None
    tags: Optional[DashboardInstanceToolCallsCreateOutputToolTags] = None
@dataclass
class DashboardInstanceToolCallsCreateOutputError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    status: str
    session_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
    group_id: Optional[str] = None
@dataclass
class DashboardInstanceToolCallsCreateOutput:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: DashboardInstanceToolCallsCreateOutputTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[DashboardInstanceToolCallsCreateOutputError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None


class mapDashboardInstanceToolCallsCreateOutputToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateOutputToolInputSchema:
        return DashboardInstanceToolCallsCreateOutputToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateOutputToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsCreateOutputToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateOutputToolOutputSchema:
        return DashboardInstanceToolCallsCreateOutputToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateOutputToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsCreateOutputToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateOutputToolTags:
        return DashboardInstanceToolCallsCreateOutputToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateOutputToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsCreateOutputTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateOutputTool:
        return DashboardInstanceToolCallsCreateOutputTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceToolCallsCreateOutputToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceToolCallsCreateOutputToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceToolCallsCreateOutputToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateOutputTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsCreateOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateOutputError:
        return DashboardInstanceToolCallsCreateOutputError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateOutput:
        return DashboardInstanceToolCallsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        tool_key=data.get('tool_key'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        transport=data.get('transport'),
        session_id=data.get('session_id'),
        message_id=data.get('message_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        tool=mapDashboardInstanceToolCallsCreateOutputTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapDashboardInstanceToolCallsCreateOutputError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceToolCallsCreateBody:
    tool_id: str
    input: Dict[str, Any]
    session_id: str
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceToolCallsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsCreateBody:
        return DashboardInstanceToolCallsCreateBody(
        tool_id=data.get('tool_id'),
        input=data.get('input'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

