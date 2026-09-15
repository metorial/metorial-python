from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatInstancesProviderSetOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceChatInstancesProviderSetOutputDeployment:
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
class ManagementInstanceChatInstancesProviderSetOutputConfig:
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
class ManagementInstanceChatInstancesProviderSetOutputAuthConfig:
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
class ManagementInstanceChatInstancesProviderSetOutputIdentity:
    id: str
    user_id: str
    name: str
    username: str
    provider_type: str
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ManagementInstanceChatInstancesProviderSetOutput:
    object: str
    id: str
    status: str
    chat_instance_id: str
    chat_connection_provider_id: str
    provider: ManagementInstanceChatInstancesProviderSetOutputProvider
    name: str
    created_at: datetime
    updated_at: datetime
    deployment: Optional[ManagementInstanceChatInstancesProviderSetOutputDeployment] = None
    config: Optional[ManagementInstanceChatInstancesProviderSetOutputConfig] = None
    auth_config: Optional[ManagementInstanceChatInstancesProviderSetOutputAuthConfig] = None
    description: Optional[str] = None
    identity: Optional[ManagementInstanceChatInstancesProviderSetOutputIdentity] = None


class mapManagementInstanceChatInstancesProviderSetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetOutputProvider:
        return ManagementInstanceChatInstancesProviderSetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatInstancesProviderSetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetOutputDeployment:
        return ManagementInstanceChatInstancesProviderSetOutputDeployment(
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
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatInstancesProviderSetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetOutputConfig:
        return ManagementInstanceChatInstancesProviderSetOutputConfig(
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
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatInstancesProviderSetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetOutputAuthConfig:
        return ManagementInstanceChatInstancesProviderSetOutputAuthConfig(
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
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatInstancesProviderSetOutputIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetOutputIdentity:
        return ManagementInstanceChatInstancesProviderSetOutputIdentity(
        id=data.get('id'),
        user_id=data.get('user_id'),
        name=data.get('name'),
        username=data.get('username'),
        provider_type=data.get('provider_type'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetOutputIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatInstancesProviderSetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetOutput:
        return ManagementInstanceChatInstancesProviderSetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        chat_instance_id=data.get('chat_instance_id'),
        chat_connection_provider_id=data.get('chat_connection_provider_id'),
        provider=mapManagementInstanceChatInstancesProviderSetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapManagementInstanceChatInstancesProviderSetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceChatInstancesProviderSetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceChatInstancesProviderSetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        name=data.get('name'),
        description=data.get('description'),
        identity=mapManagementInstanceChatInstancesProviderSetOutputIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatInstancesProviderSetBody:
    provider_id: str
    provider_deployment_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None


class mapManagementInstanceChatInstancesProviderSetBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatInstancesProviderSetBody:
        return ManagementInstanceChatInstancesProviderSetBody(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatInstancesProviderSetBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

