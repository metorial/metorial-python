from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersListOutputItemsDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsDraftConfig:
    object: str
    schema: ManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsDraft:
    object: str
    config: ManagementInstanceCustomProvidersListOutputItemsDraftConfig
    container_image: Optional[ManagementInstanceCustomProvidersListOutputItemsDraftContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsScmRepo:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersListOutputItemsScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion:
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
class ManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsProviderOauth:
    status: str
    auto_registration: ManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersListOutputItemsProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceCustomProvidersListOutputItemsProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[ManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion] = None
    oauth: Optional[ManagementInstanceCustomProvidersListOutputItemsProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceCustomProvidersListOutputItems:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: ManagementInstanceCustomProvidersListOutputItemsDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[ManagementInstanceCustomProvidersListOutputItemsScmRepo] = None
    provider: Optional[ManagementInstanceCustomProvidersListOutputItemsProvider] = None
@dataclass
class ManagementInstanceCustomProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCustomProvidersListOutput:
    items: List[ManagementInstanceCustomProvidersListOutputItems]
    pagination: ManagementInstanceCustomProvidersListOutputPagination


class mapManagementInstanceCustomProvidersListOutputItemsDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsDraftContainerImage:
        return ManagementInstanceCustomProvidersListOutputItemsDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer:
        return ManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema:
        return ManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsDraftConfig:
        return ManagementInstanceCustomProvidersListOutputItemsDraftConfig(
        object=data.get('object'),
        schema=mapManagementInstanceCustomProvidersListOutputItemsDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsDraft:
        return ManagementInstanceCustomProvidersListOutputItemsDraft(
        object=data.get('object'),
        container_image=mapManagementInstanceCustomProvidersListOutputItemsDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapManagementInstanceCustomProvidersListOutputItemsDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapManagementInstanceCustomProvidersListOutputItemsDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsScmRepoProvider:
        return ManagementInstanceCustomProvidersListOutputItemsScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsScmRepo:
        return ManagementInstanceCustomProvidersListOutputItemsScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersListOutputItemsScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsProviderPublisher:
        return ManagementInstanceCustomProvidersListOutputItemsProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion:
        return ManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration:
        return ManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsProviderOauth:
        return ManagementInstanceCustomProvidersListOutputItemsProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapManagementInstanceCustomProvidersListOutputItemsProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItemsProvider:
        return ManagementInstanceCustomProvidersListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapManagementInstanceCustomProvidersListOutputItemsProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapManagementInstanceCustomProvidersListOutputItemsProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapManagementInstanceCustomProvidersListOutputItemsProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputItems:
        return ManagementInstanceCustomProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapManagementInstanceCustomProvidersListOutputItemsDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapManagementInstanceCustomProvidersListOutputItemsScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapManagementInstanceCustomProvidersListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutputPagination:
        return ManagementInstanceCustomProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListOutput:
        return ManagementInstanceCustomProvidersListOutput(
        items=[mapManagementInstanceCustomProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCustomProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersListQuery:
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


class mapManagementInstanceCustomProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersListQuery:
        return ManagementInstanceCustomProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        type=data.get('type'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

