from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpServersUpdateOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ManagementInstanceMagicMcpServersUpdateOutput:
    object: str
    id: str
    status: str
    source: str
    endpoints: List[ManagementInstanceMagicMcpServersUpdateOutputEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    session_template_id: str
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    session_id: Optional[str] = None


class mapManagementInstanceMagicMcpServersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersUpdateOutput:
        return ManagementInstanceMagicMcpServersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapManagementInstanceMagicMcpServersUpdateOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        session_template_id=data.get('session_template_id'),
        session_id=data.get('session_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpServersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    aliases: Optional[List[str]] = None
    session_template_id: Optional[str] = None


class mapManagementInstanceMagicMcpServersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersUpdateBody:
        return ManagementInstanceMagicMcpServersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        aliases=data.get('aliases', []),
        session_template_id=data.get('session_template_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

