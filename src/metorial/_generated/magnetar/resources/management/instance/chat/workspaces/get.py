from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatWorkspacesGetOutput:
    object: str
    id: str
    chat_id: str
    provider_workspace_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    domain: Optional[str] = None
    image_url: Optional[str] = None


class mapManagementInstanceChatWorkspacesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatWorkspacesGetOutput:
        return ManagementInstanceChatWorkspacesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        provider_workspace_id=data.get('provider_workspace_id'),
        name=data.get('name'),
        domain=data.get('domain'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatWorkspacesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatWorkspacesGetQuery:
    chat_instance_id: str


class mapManagementInstanceChatWorkspacesGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatWorkspacesGetQuery:
        return ManagementInstanceChatWorkspacesGetQuery(
        chat_instance_id=data.get('chat_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatWorkspacesGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

