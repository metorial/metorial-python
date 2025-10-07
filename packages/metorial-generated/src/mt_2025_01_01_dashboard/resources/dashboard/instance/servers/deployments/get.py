from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider:
    id: str
    name: str
    url: str
    image_url: str
@dataclass
class DashboardInstanceServersDeploymentsGetOutputOauthConnection:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider: DashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    template_id: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsGetOutputConfig:
    object: str
    id: str
    status: str
    secret_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceServersDeploymentsGetOutputServerImplementationServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsGetOutputServerImplementation:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    server_variant: DashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant
    server: DashboardInstanceServersDeploymentsGetOutputServerImplementationServer
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    get_launch_params: Optional[str] = None
@dataclass
class DashboardInstanceServersDeploymentsGetOutput:
    object: str
    id: str
    status: str
    name: str
    result: Dict[str, Any]
    metadata: Dict[str, Any]
    secret_id: str
    server: DashboardInstanceServersDeploymentsGetOutputServer
    config: DashboardInstanceServersDeploymentsGetOutputConfig
    server_implementation: DashboardInstanceServersDeploymentsGetOutputServerImplementation
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    oauth_connection: Optional[DashboardInstanceServersDeploymentsGetOutputOauthConnection] = None


class mapDashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider:
        return DashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider(
        id=data.get('id'),
        name=data.get('name'),
        url=data.get('url'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutputOauthConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputOauthConnection:
        return DashboardInstanceServersDeploymentsGetOutputOauthConnection(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapDashboardInstanceServersDeploymentsGetOutputOauthConnectionProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        scopes=data.get('scopes', []),
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputOauthConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputServer:
        return DashboardInstanceServersDeploymentsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputConfig:
        return DashboardInstanceServersDeploymentsGetOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_id=data.get('secret_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant:
        return DashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutputServerImplementationServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputServerImplementationServer:
        return DashboardInstanceServersDeploymentsGetOutputServerImplementationServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputServerImplementationServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutputServerImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutputServerImplementation:
        return DashboardInstanceServersDeploymentsGetOutputServerImplementation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        get_launch_params=data.get('get_launch_params'),
        server_variant=mapDashboardInstanceServersDeploymentsGetOutputServerImplementationServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server=mapDashboardInstanceServersDeploymentsGetOutputServerImplementationServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutputServerImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersDeploymentsGetOutput:
        return DashboardInstanceServersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        oauth_connection=mapDashboardInstanceServersDeploymentsGetOutputOauthConnection.from_dict(data.get('oauth_connection')) if data.get('oauth_connection') else None,
        result=data.get('result'),
        metadata=data.get('metadata'),
        secret_id=data.get('secret_id'),
        server=mapDashboardInstanceServersDeploymentsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        config=mapDashboardInstanceServersDeploymentsGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        server_implementation=mapDashboardInstanceServersDeploymentsGetOutputServerImplementation.from_dict(data.get('server_implementation')) if data.get('server_implementation') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

