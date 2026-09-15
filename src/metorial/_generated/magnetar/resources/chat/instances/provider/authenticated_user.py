from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatInstancesProviderAuthenticatedUserOutputWorkspace:
    id: str
    provider_workspace_id: str
    name: Optional[str] = None
    domain: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ChatInstancesProviderAuthenticatedUserOutput:
    object: str
    type: str
    role: str
    provider_author_id: str
    user_name: str
    full_name: str
    is_self: bool
    id: Optional[str] = None
    chat_id: Optional[str] = None
    provider_type: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
    workspace: Optional[ChatInstancesProviderAuthenticatedUserOutputWorkspace] = None


class mapChatInstancesProviderAuthenticatedUserOutputWorkspace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderAuthenticatedUserOutputWorkspace:
        return ChatInstancesProviderAuthenticatedUserOutputWorkspace(
        id=data.get('id'),
        provider_workspace_id=data.get('provider_workspace_id'),
        name=data.get('name'),
        domain=data.get('domain'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderAuthenticatedUserOutputWorkspace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderAuthenticatedUserOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderAuthenticatedUserOutput:
        return ChatInstancesProviderAuthenticatedUserOutput(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        type=data.get('type'),
        role=data.get('role'),
        provider_type=data.get('provider_type'),
        provider_author_id=data.get('provider_author_id'),
        user_name=data.get('user_name'),
        full_name=data.get('full_name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        is_self=data.get('is_self'),
        workspace=mapChatInstancesProviderAuthenticatedUserOutputWorkspace.from_dict(data.get('workspace')) if data.get('workspace') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderAuthenticatedUserOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

