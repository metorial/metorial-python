from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpTokensCreateOutputGroups:
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
class ManagementInstanceMagicMcpTokensCreateOutput:
    object: str
    id: str
    status: str
    secret: str
    groups: List[ManagementInstanceMagicMcpTokensCreateOutputGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapManagementInstanceMagicMcpTokensCreateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensCreateOutputGroups:
        return ManagementInstanceMagicMcpTokensCreateOutputGroups(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensCreateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpTokensCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensCreateOutput:
        return ManagementInstanceMagicMcpTokensCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        groups=[mapManagementInstanceMagicMcpTokensCreateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpTokensCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    magic_mcp_group_ids: Optional[List[str]] = None


class mapManagementInstanceMagicMcpTokensCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensCreateBody:
        return ManagementInstanceMagicMcpTokensCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        magic_mcp_group_ids=data.get('magic_mcp_group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

