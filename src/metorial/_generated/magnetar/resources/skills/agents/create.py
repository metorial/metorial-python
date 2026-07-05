from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsAgentsCreateOutput:
    object: str
    id: str
    skill_id: str
    name: str
    slug: str
    status: str
    store_id: str
    document_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    store_item_id: Optional[str] = None
    path: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapSkillsAgentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAgentsCreateOutput:
        return SkillsAgentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        status=data.get('status'),
        store_id=data.get('store_id'),
        store_item_id=data.get('store_item_id'),
        path=data.get('path'),
        document_id=data.get('document_id'),
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsAgentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsAgentsCreateBody:
    name: str
    description: Optional[str] = None
    content: Optional[str] = None


class mapSkillsAgentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsAgentsCreateBody:
        return SkillsAgentsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[SkillsAgentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

