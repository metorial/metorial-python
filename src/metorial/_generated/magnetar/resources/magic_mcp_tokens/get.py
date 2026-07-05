from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpTokensGetOutputServer:
    object: str
    id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpTokensGetOutputEndpoint:
    object: str
    id: str
    status: str
    slug: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpTokensGetOutputGroups:
    object: str
    id: str
    status: str
    slug: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpTokensGetOutput:
    object: str
    id: str
    status: str
    secret: str
    groups: List[MagicMcpTokensGetOutputGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    server: Optional[MagicMcpTokensGetOutputServer] = None
    endpoint: Optional[MagicMcpTokensGetOutputEndpoint] = None


class mapMagicMcpTokensGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensGetOutputServer:
        return MagicMcpTokensGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensGetOutputEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensGetOutputEndpoint:
        return MagicMcpTokensGetOutputEndpoint(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensGetOutputEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensGetOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensGetOutputGroups:
        return MagicMcpTokensGetOutputGroups(
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
    def to_dict(value: Union[MagicMcpTokensGetOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensGetOutput:
        return MagicMcpTokensGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        server=mapMagicMcpTokensGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        endpoint=mapMagicMcpTokensGetOutputEndpoint.from_dict(data.get('endpoint')) if data.get('endpoint') else None,
        groups=[mapMagicMcpTokensGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

