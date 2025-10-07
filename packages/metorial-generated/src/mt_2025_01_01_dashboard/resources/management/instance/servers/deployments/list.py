from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider:
    id: str
    name: str
    url: str
    image_url: str
@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsOauthConnection:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    provider: ManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    template_id: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsConfig:
    object: str
    id: str
    status: str
    secret_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsListOutputItemsServerImplementation:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    server_variant: ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant
    server: ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    get_launch_params: Optional[str] = None
@dataclass
class ManagementInstanceServersDeploymentsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    result: Dict[str, Any]
    metadata: Dict[str, Any]
    secret_id: str
    server: ManagementInstanceServersDeploymentsListOutputItemsServer
    config: ManagementInstanceServersDeploymentsListOutputItemsConfig
    server_implementation: ManagementInstanceServersDeploymentsListOutputItemsServerImplementation
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    oauth_connection: Optional[ManagementInstanceServersDeploymentsListOutputItemsOauthConnection] = None
@dataclass
class ManagementInstanceServersDeploymentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceServersDeploymentsListOutput:
    items: List[ManagementInstanceServersDeploymentsListOutputItems]
    pagination: ManagementInstanceServersDeploymentsListOutputPagination


class mapManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider:
        return ManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider(
        id=data.get('id'),
        name=data.get('name'),
        url=data.get('url'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItemsOauthConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsOauthConnection:
        return ManagementInstanceServersDeploymentsListOutputItemsOauthConnection(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapManagementInstanceServersDeploymentsListOutputItemsOauthConnectionProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        scopes=data.get('scopes', []),
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsOauthConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItemsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsServer:
        return ManagementInstanceServersDeploymentsListOutputItemsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsConfig:
        return ManagementInstanceServersDeploymentsListOutputItemsConfig(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_id=data.get('secret_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant:
        return ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer:
        return ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItemsServerImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItemsServerImplementation:
        return ManagementInstanceServersDeploymentsListOutputItemsServerImplementation(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        get_launch_params=data.get('get_launch_params'),
        server_variant=mapManagementInstanceServersDeploymentsListOutputItemsServerImplementationServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server=mapManagementInstanceServersDeploymentsListOutputItemsServerImplementationServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItemsServerImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputItems:
        return ManagementInstanceServersDeploymentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        oauth_connection=mapManagementInstanceServersDeploymentsListOutputItemsOauthConnection.from_dict(data.get('oauth_connection')) if data.get('oauth_connection') else None,
        result=data.get('result'),
        metadata=data.get('metadata'),
        secret_id=data.get('secret_id'),
        server=mapManagementInstanceServersDeploymentsListOutputItemsServer.from_dict(data.get('server')) if data.get('server') else None,
        config=mapManagementInstanceServersDeploymentsListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        server_implementation=mapManagementInstanceServersDeploymentsListOutputItemsServerImplementation.from_dict(data.get('server_implementation')) if data.get('server_implementation') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutputPagination:
        return ManagementInstanceServersDeploymentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersDeploymentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListOutput:
        return ManagementInstanceServersDeploymentsListOutput(
        items=[mapManagementInstanceServersDeploymentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceServersDeploymentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServersDeploymentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    server_id: Optional[Union[str, List[str]]] = None
    server_variant_id: Optional[Union[str, List[str]]] = None
    server_implementation_id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceServersDeploymentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersDeploymentsListQuery:
        return ManagementInstanceServersDeploymentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id'),
        server_implementation_id=data.get('server_implementation_id'),
        session_id=data.get('session_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersDeploymentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

