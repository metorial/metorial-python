from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersListOutputItemsDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsDraftConfig:
    object: str
    schema: DashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsDraft:
    object: str
    config: DashboardInstanceCustomProvidersListOutputItemsDraftConfig
    container_image: Optional[DashboardInstanceCustomProvidersListOutputItemsDraftContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsScmRepo:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersListOutputItemsScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion:
    object: str
    id: str
    version: str
    provider_id: str
    is_current: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    specification_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsProviderOauth:
    status: str
    auto_registration: DashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersListOutputItemsProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceCustomProvidersListOutputItemsProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[DashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion] = None
    oauth: Optional[DashboardInstanceCustomProvidersListOutputItemsProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceCustomProvidersListOutputItems:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: DashboardInstanceCustomProvidersListOutputItemsDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[DashboardInstanceCustomProvidersListOutputItemsScmRepo] = None
    provider: Optional[DashboardInstanceCustomProvidersListOutputItemsProvider] = None
@dataclass
class DashboardInstanceCustomProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCustomProvidersListOutput:
    items: List[DashboardInstanceCustomProvidersListOutputItems]
    pagination: DashboardInstanceCustomProvidersListOutputPagination


class mapDashboardInstanceCustomProvidersListOutputItemsDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsDraftContainerImage:
        return DashboardInstanceCustomProvidersListOutputItemsDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer:
        return DashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema:
        return DashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsDraftConfig:
        return DashboardInstanceCustomProvidersListOutputItemsDraftConfig(
        object=data.get('object'),
        schema=mapDashboardInstanceCustomProvidersListOutputItemsDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsDraft:
        return DashboardInstanceCustomProvidersListOutputItemsDraft(
        object=data.get('object'),
        container_image=mapDashboardInstanceCustomProvidersListOutputItemsDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapDashboardInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapDashboardInstanceCustomProvidersListOutputItemsDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsScmRepoProvider:
        return DashboardInstanceCustomProvidersListOutputItemsScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsScmRepo:
        return DashboardInstanceCustomProvidersListOutputItemsScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersListOutputItemsScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsProviderPublisher:
        return DashboardInstanceCustomProvidersListOutputItemsProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion:
        return DashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration:
        return DashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsProviderOauth:
        return DashboardInstanceCustomProvidersListOutputItemsProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapDashboardInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItemsProvider:
        return DashboardInstanceCustomProvidersListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapDashboardInstanceCustomProvidersListOutputItemsProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapDashboardInstanceCustomProvidersListOutputItemsProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapDashboardInstanceCustomProvidersListOutputItemsProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputItems:
        return DashboardInstanceCustomProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapDashboardInstanceCustomProvidersListOutputItemsDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapDashboardInstanceCustomProvidersListOutputItemsScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapDashboardInstanceCustomProvidersListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutputPagination:
        return DashboardInstanceCustomProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListOutput:
        return DashboardInstanceCustomProvidersListOutput(
        items=[mapDashboardInstanceCustomProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCustomProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    created_at: Optional[DashboardInstanceCustomProvidersListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceCustomProvidersListQueryUpdatedAt] = None


class mapDashboardInstanceCustomProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersListQuery:
        return DashboardInstanceCustomProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        type=data.get('type'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        search=data.get('search'),
        created_at=mapDashboardInstanceCustomProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceCustomProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

