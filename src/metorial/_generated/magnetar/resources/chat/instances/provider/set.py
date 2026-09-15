from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatInstancesProviderSetOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ChatInstancesProviderSetOutputDeployment:
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
class ChatInstancesProviderSetOutputConfig:
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
class ChatInstancesProviderSetOutputAuthConfig:
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
class ChatInstancesProviderSetOutputIdentity:
    id: str
    user_id: str
    name: str
    username: str
    provider_type: str
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ChatInstancesProviderSetOutput:
    object: str
    id: str
    status: str
    chat_instance_id: str
    chat_connection_provider_id: str
    provider: ChatInstancesProviderSetOutputProvider
    name: str
    created_at: datetime
    updated_at: datetime
    deployment: Optional[ChatInstancesProviderSetOutputDeployment] = None
    config: Optional[ChatInstancesProviderSetOutputConfig] = None
    auth_config: Optional[ChatInstancesProviderSetOutputAuthConfig] = None
    description: Optional[str] = None
    identity: Optional[ChatInstancesProviderSetOutputIdentity] = None


class mapChatInstancesProviderSetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetOutputProvider:
        return ChatInstancesProviderSetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderSetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderSetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetOutputDeployment:
        return ChatInstancesProviderSetOutputDeployment(
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
    def to_dict(value: Union[ChatInstancesProviderSetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderSetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetOutputConfig:
        return ChatInstancesProviderSetOutputConfig(
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
    def to_dict(value: Union[ChatInstancesProviderSetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderSetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetOutputAuthConfig:
        return ChatInstancesProviderSetOutputAuthConfig(
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
    def to_dict(value: Union[ChatInstancesProviderSetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderSetOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetOutputIdentity:
        return ChatInstancesProviderSetOutputIdentity(
        id=data.get('id'),
        user_id=data.get('user_id'),
        name=data.get('name'),
        username=data.get('username'),
        provider_type=data.get('provider_type'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderSetOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesProviderSetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetOutput:
        return ChatInstancesProviderSetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        chat_instance_id=data.get('chat_instance_id'),
        chat_connection_provider_id=data.get('chat_connection_provider_id'),
        provider=mapChatInstancesProviderSetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapChatInstancesProviderSetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapChatInstancesProviderSetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapChatInstancesProviderSetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        name=data.get('name'),
        description=data.get('description'),
        identity=mapChatInstancesProviderSetOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderSetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatInstancesProviderSetBody:
    provider_id: str
    provider_deployment_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None


class mapChatInstancesProviderSetBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesProviderSetBody:
        return ChatInstancesProviderSetBody(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id')
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesProviderSetBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

