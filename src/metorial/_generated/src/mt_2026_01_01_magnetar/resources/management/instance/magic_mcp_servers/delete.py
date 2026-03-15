from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpServersDeleteOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ManagementInstanceMagicMcpServersDeleteOutput:
    object: str
    id: str
    status: str
    session_template_id: str
    endpoints: List[ManagementInstanceMagicMcpServersDeleteOutputEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapManagementInstanceMagicMcpServersDeleteOutputEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersDeleteOutputEndpoints:
        return ManagementInstanceMagicMcpServersDeleteOutputEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersDeleteOutputEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersDeleteOutput:
        return ManagementInstanceMagicMcpServersDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        session_template_id=data.get('session_template_id'),
        endpoints=[mapManagementInstanceMagicMcpServersDeleteOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

