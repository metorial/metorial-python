from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersArchiveOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputDraftConfig:
    object: str
    schema: DashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputDraft:
    object: str
    config: DashboardInstanceCustomProvidersArchiveOutputDraftConfig
    container_image: Optional[DashboardInstanceCustomProvidersArchiveOutputDraftContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputScmRepo:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersArchiveOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion:
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
class DashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputProviderOauth:
    status: str
    auto_registration: DashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersArchiveOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceCustomProvidersArchiveOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[DashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion] = None
    oauth: Optional[DashboardInstanceCustomProvidersArchiveOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceCustomProvidersArchiveOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: DashboardInstanceCustomProvidersArchiveOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[DashboardInstanceCustomProvidersArchiveOutputScmRepo] = None
    provider: Optional[DashboardInstanceCustomProvidersArchiveOutputProvider] = None


class mapDashboardInstanceCustomProvidersArchiveOutputDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputDraftContainerImage:
        return DashboardInstanceCustomProvidersArchiveOutputDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer:
        return DashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema:
        return DashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputDraftConfig:
        return DashboardInstanceCustomProvidersArchiveOutputDraftConfig(
        object=data.get('object'),
        schema=mapDashboardInstanceCustomProvidersArchiveOutputDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputDraft:
        return DashboardInstanceCustomProvidersArchiveOutputDraft(
        object=data.get('object'),
        container_image=mapDashboardInstanceCustomProvidersArchiveOutputDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapDashboardInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapDashboardInstanceCustomProvidersArchiveOutputDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputScmRepoProvider:
        return DashboardInstanceCustomProvidersArchiveOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputScmRepo:
        return DashboardInstanceCustomProvidersArchiveOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersArchiveOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputProviderPublisher:
        return DashboardInstanceCustomProvidersArchiveOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion:
        return DashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration:
        return DashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputProviderOauth:
        return DashboardInstanceCustomProvidersArchiveOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapDashboardInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutputProvider:
        return DashboardInstanceCustomProvidersArchiveOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapDashboardInstanceCustomProvidersArchiveOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapDashboardInstanceCustomProvidersArchiveOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapDashboardInstanceCustomProvidersArchiveOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersArchiveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersArchiveOutput:
        return DashboardInstanceCustomProvidersArchiveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapDashboardInstanceCustomProvidersArchiveOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapDashboardInstanceCustomProvidersArchiveOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapDashboardInstanceCustomProvidersArchiveOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersArchiveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

