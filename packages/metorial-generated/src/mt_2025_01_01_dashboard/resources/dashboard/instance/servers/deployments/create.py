from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
    id: str
    name: str
    url: str
    image_url: str
@dataclass
class DashboardInstanceServersDeploymentsCreateOutputOauthConnection:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider: DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    template_id: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsCreateOutputConfig:
    object: str
    id: str
    status: str
    secret_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsCreateOutputServerImplementation:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    server_variant: DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant
    server: DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    get_launch_params: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    result: Dict[str, Any]
    metadata: Dict[str, Any]
    secret_id: str
    server: DashboardInstanceServersDeploymentsCreateOutputServer
    config: DashboardInstanceServersDeploymentsCreateOutputConfig
    server_implementation: DashboardInstanceServersDeploymentsCreateOutputServerImplementation
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    oauth_connection: Optional[DashboardInstanceServersDeploymentsCreateOutputOauthConnection] = None


class mapDashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider:
        return DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider(
        id=data.get('id'),
        name=data.get('name'),
        url=data.get('url'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutputOauthConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputOauthConnection:
        return DashboardInstanceServersDeploymentsCreateOutputOauthConnection(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapDashboardInstanceServersDeploymentsCreateOutputOauthConnectionProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        scopes=data.get('scopes', []),
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputOauthConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputServer:
        return DashboardInstanceServersDeploymentsCreateOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputConfig:
        return DashboardInstanceServersDeploymentsCreateOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_id=data.get('secret_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant:
        return DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer:
        return DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputServerImplementationServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutputServerImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutputServerImplementation:
        return DashboardInstanceServersDeploymentsCreateOutputServerImplementation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        get_launch_params=data.get('get_launch_params'),
        server_variant=mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server=mapDashboardInstanceServersDeploymentsCreateOutputServerImplementationServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutputServerImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateOutput:
        return DashboardInstanceServersDeploymentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        oauth_connection=mapDashboardInstanceServersDeploymentsCreateOutputOauthConnection.from_dict(data.get('oauth_connection')) if data.get('oauth_connection') else None,
        result=data.get('result'),
        metadata=data.get('metadata'),
        secret_id=data.get('secret_id'),
        server=mapDashboardInstanceServersDeploymentsCreateOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        config=mapDashboardInstanceServersDeploymentsCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        server_implementation=mapDashboardInstanceServersDeploymentsCreateOutputServerImplementation.from_dict(data.get('server_implementation')) if data.get('server_implementation') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceServersDeploymentsCreateBodyOauthConfig:
    client_id: str
    client_secret: str
@dataclass
class DashboardInstanceServersDeploymentsCreateBody:
    config: Dict[str, Any]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    oauth_config: Optional[DashboardInstanceServersDeploymentsCreateBodyOauthConfig] = None
    server_implementation: Optional[Dict[str, Any]] = None
    server_implementation_id: Optional[str] = None
    server_variant_id: Optional[str] = None
    server_id: Optional[str] = None


class mapDashboardInstanceServersDeploymentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsCreateBody:
        return DashboardInstanceServersDeploymentsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        config=data.get('config'),
        oauth_config=mapDashboardInstanceServersDeploymentsCreateBodyOauthConfig.from_dict(data.get('oauth_config')) if data.get('oauth_config') else None,
        server_implementation=data.get('server_implementation'),
        server_implementation_id=data.get('server_implementation_id'),
        server_variant_id=data.get('server_variant_id'),
        server_id=data.get('server_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

