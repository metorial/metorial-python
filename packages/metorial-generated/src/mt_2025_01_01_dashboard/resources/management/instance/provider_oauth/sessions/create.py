from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider:
    id: str
    name: str
    url: str
    image_url: str
@dataclass
class ManagementInstanceProviderOauthSessionsCreateOutputConnection:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider: ManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    template_id: Optional[str] = None
@dataclass
class ManagementInstanceProviderOauthSessionsCreateOutput:
    object: str
    id: str
    status: str
    url: str
    connection: ManagementInstanceProviderOauthSessionsCreateOutputConnection
    metadata: Dict[str, Any]
    instance_id: str
    created_at: datetime
    updated_at: datetime
    redirect_uri: Optional[str] = None
    completed_at: Optional[datetime] = None


class mapManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider:
        return ManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider(
        id=data.get('id'),
        name=data.get('name'),
        url=data.get('url'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthSessionsCreateOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthSessionsCreateOutputConnection:
        return ManagementInstanceProviderOauthSessionsCreateOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapManagementInstanceProviderOauthSessionsCreateOutputConnectionProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        scopes=data.get('scopes', []),
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthSessionsCreateOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthSessionsCreateOutput:
        return ManagementInstanceProviderOauthSessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        url=data.get('url'),
        connection=mapManagementInstanceProviderOauthSessionsCreateOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        metadata=data.get('metadata'),
        redirect_uri=data.get('redirect_uri'),
        instance_id=data.get('instance_id'),
        completed_at=datetime.fromisoformat(data.get('completed_at')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderOauthSessionsCreateBody:
    metadata: Optional[Dict[str, Any]] = None
    redirect_uri: Optional[str] = None
    server_deployment_id: Optional[str] = None
    connection_id: Optional[str] = None


class mapManagementInstanceProviderOauthSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthSessionsCreateBody:
        return ManagementInstanceProviderOauthSessionsCreateBody(
        metadata=data.get('metadata'),
        redirect_uri=data.get('redirect_uri'),
        server_deployment_id=data.get('server_deployment_id'),
        connection_id=data.get('connection_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

