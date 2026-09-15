from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatInstancesProviderGetOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ChatInstancesProviderGetOutputDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ChatInstancesProviderGetOutputConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ChatInstancesProviderGetOutputAuthConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ChatInstancesProviderGetOutputIdentity:
    id: str
    user_id: str
    name: str
    username: str
    provider_type: str
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ChatInstancesProviderGetOutput:
    object: str
    id: str
    status: str
    chat_instance_id: str
    chat_connection_provider_id: str
    provider: ChatInstancesProviderGetOutputProvider
    name: str
    created_at: datetime
    updated_at: datetime
    deployment: Optional[ChatInstancesProviderGetOutputDeployment] = None
    config: Optional[ChatInstancesProviderGetOutputConfig] = None
    auth_config: Optional[ChatInstancesProviderGetOutputAuthConfig] = None
    description: Optional[str] = None
    identity: Optional[ChatInstancesProviderGetOutputIdentity] = None


class mapChatInstancesProviderGetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderGetOutputProvider:
        return ChatInstancesProviderGetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderGetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderGetOutputDeployment:
        return ChatInstancesProviderGetOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderGetOutputConfig:
        return ChatInstancesProviderGetOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderGetOutputAuthConfig:
        return ChatInstancesProviderGetOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderGetOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderGetOutputIdentity:
        return ChatInstancesProviderGetOutputIdentity(
        id=data.get('id'),
        user_id=data.get('user_id'),
        name=data.get('name'),
        username=data.get('username'),
        provider_type=data.get('provider_type'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderGetOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderGetOutput:
        return ChatInstancesProviderGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        chat_instance_id=data.get('chat_instance_id'),
        chat_connection_provider_id=data.get('chat_connection_provider_id'),
        provider=mapChatInstancesProviderGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapChatInstancesProviderGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapChatInstancesProviderGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapChatInstancesProviderGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        name=data.get('name'),
        description=data.get('description'),
        identity=mapChatInstancesProviderGetOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

