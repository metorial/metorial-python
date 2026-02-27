from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ToolCallsCreateOutputToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsCreateOutputToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsCreateOutputToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ToolCallsCreateOutputTool:
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
    input_schema: Optional[ToolCallsCreateOutputToolInputSchema] = None
    output_schema: Optional[ToolCallsCreateOutputToolOutputSchema] = None
    tags: Optional[ToolCallsCreateOutputToolTags] = None
@dataclass
class ToolCallsCreateOutputError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    group_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
@dataclass
class ToolCallsCreateOutput:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ToolCallsCreateOutputTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[ToolCallsCreateOutputError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None


class mapToolCallsCreateOutputToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputToolInputSchema:
        return ToolCallsCreateOutputToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputToolOutputSchema:
        return ToolCallsCreateOutputToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputToolTags:
        return ToolCallsCreateOutputToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputTool:
        return ToolCallsCreateOutputTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapToolCallsCreateOutputToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapToolCallsCreateOutputToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapToolCallsCreateOutputToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputError:
        return ToolCallsCreateOutputError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutput:
        return ToolCallsCreateOutput(
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
        tool=mapToolCallsCreateOutputTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapToolCallsCreateOutputError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ToolCallsCreateBody:
    tool_id: str
    input: Dict[str, Any]
    session_id: str
    metadata: Optional[Dict[str, Any]] = None


class mapToolCallsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateBody:
        return ToolCallsCreateBody(
        tool_id=data.get('tool_id'),
        input=data.get('input'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
