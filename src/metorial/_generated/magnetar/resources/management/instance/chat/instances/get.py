from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatInstancesGetOutputIdentity:
    id: str
    user_id: str
    name: str
    username: str
    provider_type: str
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ManagementInstanceChatInstancesGetOutput:
    object: str
    id: str
    status: str
    chat_connection_id: str
    name: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    identity: Optional[ManagementInstanceChatInstancesGetOutputIdentity] = None


class mapManagementInstanceChatInstancesGetOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesGetOutputIdentity:
        return ManagementInstanceChatInstancesGetOutputIdentity(
        id=data.get('id'),
        user_id=data.get('user_id'),
        name=data.get('name'),
        username=data.get('username'),
        provider_type=data.get('provider_type'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatInstancesGetOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesGetOutput:
        return ManagementInstanceChatInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        chat_connection_id=data.get('chat_connection_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        identity=mapManagementInstanceChatInstancesGetOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

