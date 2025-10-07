from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider:
    id: str
    name: str
    url: str
    image_url: str
@dataclass
class ManagementInstanceServersDeploymentsGetOutputOauthConnection:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider: ManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    template_id: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsGetOutputConfig:
    object: str
    id: str
    status: str
    secret_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceServersDeploymentsGetOutputServerImplementationServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsGetOutputServerImplementation:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    server_variant: ManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant
    server: ManagementInstanceServersDeploymentsGetOutputServerImplementationServer
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    get_launch_params: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsGetOutput:
    object: str
    id: str
    status: str
    name: str
    result: Dict[str, Any]
    metadata: Dict[str, Any]
    secret_id: str
    server: ManagementInstanceServersDeploymentsGetOutputServer
    config: ManagementInstanceServersDeploymentsGetOutputConfig
    server_implementation: ManagementInstanceServersDeploymentsGetOutputServerImplementation
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    oauth_connection: Optional[ManagementInstanceServersDeploymentsGetOutputOauthConnection] = None


class mapManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider:
        return ManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider(
        id=data.get('id'),
        name=data.get('name'),
        url=data.get('url'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutputOauthConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputOauthConnection:
        return ManagementInstanceServersDeploymentsGetOutputOauthConnection(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapManagementInstanceServersDeploymentsGetOutputOauthConnectionProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        scopes=data.get('scopes', []),
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputOauthConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputServer:
        return ManagementInstanceServersDeploymentsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputConfig:
        return ManagementInstanceServersDeploymentsGetOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_id=data.get('secret_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant:
        return ManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutputServerImplementationServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputServerImplementationServer:
        return ManagementInstanceServersDeploymentsGetOutputServerImplementationServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputServerImplementationServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutputServerImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutputServerImplementation:
        return ManagementInstanceServersDeploymentsGetOutputServerImplementation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        get_launch_params=data.get('get_launch_params'),
        server_variant=mapManagementInstanceServersDeploymentsGetOutputServerImplementationServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server=mapManagementInstanceServersDeploymentsGetOutputServerImplementationServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutputServerImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsGetOutput:
        return ManagementInstanceServersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        oauth_connection=mapManagementInstanceServersDeploymentsGetOutputOauthConnection.from_dict(data.get('oauth_connection')) if data.get('oauth_connection') else None,
        result=data.get('result'),
        metadata=data.get('metadata'),
        secret_id=data.get('secret_id'),
        server=mapManagementInstanceServersDeploymentsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        config=mapManagementInstanceServersDeploymentsGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        server_implementation=mapManagementInstanceServersDeploymentsGetOutputServerImplementation.from_dict(data.get('server_implementation')) if data.get('server_implementation') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

