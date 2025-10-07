from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
    id: str
    name: str
    url: str
    image_url: str
@dataclass
class ManagementInstanceServersDeploymentsCreateOutputOauthConnection:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider: ManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    template_id: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsCreateOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsCreateOutputConfig:
    object: str
    id: str
    status: str
    secret_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceServersDeploymentsCreateOutputServerImplementationServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsCreateOutputServerImplementation:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    server_variant: ManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant
    server: ManagementInstanceServersDeploymentsCreateOutputServerImplementationServer
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    get_launch_params: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    result: Dict[str, Any]
    metadata: Dict[str, Any]
    secret_id: str
    server: ManagementInstanceServersDeploymentsCreateOutputServer
    config: ManagementInstanceServersDeploymentsCreateOutputConfig
    server_implementation: ManagementInstanceServersDeploymentsCreateOutputServerImplementation
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    oauth_connection: Optional[ManagementInstanceServersDeploymentsCreateOutputOauthConnection] = None


class mapManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
        return ManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider(
        id=data.get('id'),
        name=data.get('name'),
        url=data.get('url'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutputOauthConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputOauthConnection:
        return ManagementInstanceServersDeploymentsCreateOutputOauthConnection(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapManagementInstanceServersDeploymentsCreateOutputOauthConnectionProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        scopes=data.get('scopes', []),
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputOauthConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputServer:
        return ManagementInstanceServersDeploymentsCreateOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputConfig:
        return ManagementInstanceServersDeploymentsCreateOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_id=data.get('secret_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
        return ManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutputServerImplementationServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputServerImplementationServer:
        return ManagementInstanceServersDeploymentsCreateOutputServerImplementationServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputServerImplementationServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutputServerImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutputServerImplementation:
        return ManagementInstanceServersDeploymentsCreateOutputServerImplementation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        get_launch_params=data.get('get_launch_params'),
        server_variant=mapManagementInstanceServersDeploymentsCreateOutputServerImplementationServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server=mapManagementInstanceServersDeploymentsCreateOutputServerImplementationServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutputServerImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateOutput:
        return ManagementInstanceServersDeploymentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        oauth_connection=mapManagementInstanceServersDeploymentsCreateOutputOauthConnection.from_dict(data.get('oauth_connection')) if data.get('oauth_connection') else None,
        result=data.get('result'),
        metadata=data.get('metadata'),
        secret_id=data.get('secret_id'),
        server=mapManagementInstanceServersDeploymentsCreateOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        config=mapManagementInstanceServersDeploymentsCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        server_implementation=mapManagementInstanceServersDeploymentsCreateOutputServerImplementation.from_dict(data.get('server_implementation')) if data.get('server_implementation') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServersDeploymentsCreateBodyOauthConfig:
    client_id: str
    client_secret: str
@dataclass
class ManagementInstanceServersDeploymentsCreateBody:
    config: Dict[str, Any]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    oauth_config: Optional[ManagementInstanceServersDeploymentsCreateBodyOauthConfig] = None
    server_implementation: Optional[Dict[str, Any]] = None
    server_implementation_id: Optional[str] = None
    server_variant_id: Optional[str] = None
    server_id: Optional[str] = None


class mapManagementInstanceServersDeploymentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsCreateBody:
        return ManagementInstanceServersDeploymentsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        config=data.get('config'),
        oauth_config=mapManagementInstanceServersDeploymentsCreateBodyOauthConfig.from_dict(data.get('oauth_config')) if data.get('oauth_config') else None,
        server_implementation=data.get('server_implementation'),
        server_implementation_id=data.get('server_implementation_id'),
        server_variant_id=data.get('server_variant_id'),
        server_id=data.get('server_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

