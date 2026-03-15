from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ToolCallsGetOutputToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsGetOutputToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsGetOutputToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ToolCallsGetOutputTool:
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
    input_schema: Optional[ToolCallsGetOutputToolInputSchema] = None
    output_schema: Optional[ToolCallsGetOutputToolOutputSchema] = None
    tags: Optional[ToolCallsGetOutputToolTags] = None
@dataclass
class ToolCallsGetOutputError:
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
class ToolCallsGetOutput:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ToolCallsGetOutputTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[ToolCallsGetOutputError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None


class mapToolCallsGetOutputToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsGetOutputToolInputSchema:
        return ToolCallsGetOutputToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsGetOutputToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsGetOutputToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsGetOutputToolOutputSchema:
        return ToolCallsGetOutputToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsGetOutputToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsGetOutputToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsGetOutputToolTags:
        return ToolCallsGetOutputToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsGetOutputToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsGetOutputTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsGetOutputTool:
        return ToolCallsGetOutputTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapToolCallsGetOutputToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapToolCallsGetOutputToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapToolCallsGetOutputToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsGetOutputTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsGetOutputError:
        return ToolCallsGetOutputError(
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
    def to_dict(value: Union[ToolCallsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsGetOutput:
        return ToolCallsGetOutput(
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
        tool=mapToolCallsGetOutputTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapToolCallsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

