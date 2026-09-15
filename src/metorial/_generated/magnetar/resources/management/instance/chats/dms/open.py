from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatsDmsOpenOutputContextAuthor:
    id: str
    name: str
@dataclass
class ManagementInstanceChatsDmsOpenOutputContextAssignee:
    id: str
    name: str
@dataclass
class ManagementInstanceChatsDmsOpenOutputContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[ManagementInstanceChatsDmsOpenOutputContextAuthor] = None
    assignee: Optional[ManagementInstanceChatsDmsOpenOutputContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class ManagementInstanceChatsDmsOpenOutput:
    object: str
    id: str
    chat_id: str
    type: str
    provider_type: str
    provider_channel_id: str
    created_at: datetime
    updated_at: datetime
    workspace_id: Optional[str] = None
    name: Optional[str] = None
    topic: Optional[str] = None
    subject: Optional[str] = None
    member_count: Optional[float] = None
    permalink: Optional[str] = None
    context: Optional[ManagementInstanceChatsDmsOpenOutputContext] = None
    last_interaction_at: Optional[datetime] = None


class mapManagementInstanceChatsDmsOpenOutputContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsDmsOpenOutputContextAuthor:
        return ManagementInstanceChatsDmsOpenOutputContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsDmsOpenOutputContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsDmsOpenOutputContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsDmsOpenOutputContextAssignee:
        return ManagementInstanceChatsDmsOpenOutputContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsDmsOpenOutputContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsDmsOpenOutputContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsDmsOpenOutputContext:
        return ManagementInstanceChatsDmsOpenOutputContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapManagementInstanceChatsDmsOpenOutputContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapManagementInstanceChatsDmsOpenOutputContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsDmsOpenOutputContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsDmsOpenOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsDmsOpenOutput:
        return ManagementInstanceChatsDmsOpenOutput(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        workspace_id=data.get('workspace_id'),
        type=data.get('type'),
        provider_type=data.get('provider_type'),
        provider_channel_id=data.get('provider_channel_id'),
        name=data.get('name'),
        topic=data.get('topic'),
        subject=data.get('subject'),
        member_count=data.get('member_count'),
        permalink=data.get('permalink'),
        context=mapManagementInstanceChatsDmsOpenOutputContext.from_dict(data.get('context')) if data.get('context') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsDmsOpenOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

ManagementInstanceChatsDmsOpenBody = Dict[str, Any]


class mapManagementInstanceChatsDmsOpenBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsDmsOpenBody:
        data

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsDmsOpenBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

