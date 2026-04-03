from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpServersUpdateOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class MagicMcpServersUpdateOutput:
    object: str
    id: str
    status: str
    source: str
    session_template_id: str
    endpoints: List[MagicMcpServersUpdateOutputEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpServersUpdateOutputEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutputEndpoints:
        return MagicMcpServersUpdateOutputEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersUpdateOutputEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutput:
        return MagicMcpServersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        session_template_id=data.get('session_template_id'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapMagicMcpServersUpdateOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpServersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    aliases: Optional[List[str]] = None
    session_template_id: Optional[str] = None


class mapMagicMcpServersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateBody:
        return MagicMcpServersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        aliases=data.get('aliases', []),
        session_template_id=data.get('session_template_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

