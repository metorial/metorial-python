from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpGroupsRemoveServersOutput:
    object: str
    id: str
    status: str
    slug: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpGroupsRemoveServersOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpGroupsRemoveServersOutput:
        return MagicMcpGroupsRemoveServersOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpGroupsRemoveServersOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpGroupsRemoveServersBody:
    magic_mcp_server_ids: List[str]


class mapMagicMcpGroupsRemoveServersBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpGroupsRemoveServersBody:
        return MagicMcpGroupsRemoveServersBody(
        magic_mcp_server_ids=data.get('magic_mcp_server_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpGroupsRemoveServersBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

