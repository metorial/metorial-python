from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsParticipantsListOutputItems:
    object: str
    id: str
    session_id: str
    created_at: datetime
    updated_at: datetime
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionsParticipantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsParticipantsListOutput:
    items: List[ManagementInstanceSessionsParticipantsListOutputItems]
    pagination: ManagementInstanceSessionsParticipantsListOutputPagination


class mapManagementInstanceSessionsParticipantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsParticipantsListOutputItems:
        return ManagementInstanceSessionsParticipantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsParticipantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsParticipantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsParticipantsListOutputPagination:
        return ManagementInstanceSessionsParticipantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsParticipantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsParticipantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsParticipantsListOutput:
        return ManagementInstanceSessionsParticipantsListOutput(
        items=[mapManagementInstanceSessionsParticipantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsParticipantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsParticipantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsParticipantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None


class mapManagementInstanceSessionsParticipantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsParticipantsListQuery:
        return ManagementInstanceSessionsParticipantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsParticipantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
