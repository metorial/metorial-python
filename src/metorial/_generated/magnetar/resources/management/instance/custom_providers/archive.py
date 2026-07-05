from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersArchiveOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputDraftConfig:
    object: str
    schema: ManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputDraft:
    object: str
    config: ManagementInstanceCustomProvidersArchiveOutputDraftConfig
    container_image: Optional[ManagementInstanceCustomProvidersArchiveOutputDraftContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputScmRepo:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersArchiveOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion:
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
class ManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputProviderOauth:
    status: str
    auto_registration: ManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersArchiveOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceCustomProvidersArchiveOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[ManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion] = None
    oauth: Optional[ManagementInstanceCustomProvidersArchiveOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceCustomProvidersArchiveOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: ManagementInstanceCustomProvidersArchiveOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[ManagementInstanceCustomProvidersArchiveOutputScmRepo] = None
    provider: Optional[ManagementInstanceCustomProvidersArchiveOutputProvider] = None


class mapManagementInstanceCustomProvidersArchiveOutputDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputDraftContainerImage:
        return ManagementInstanceCustomProvidersArchiveOutputDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer:
        return ManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema:
        return ManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputDraftConfig:
        return ManagementInstanceCustomProvidersArchiveOutputDraftConfig(
        object=data.get('object'),
        schema=mapManagementInstanceCustomProvidersArchiveOutputDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputDraft:
        return ManagementInstanceCustomProvidersArchiveOutputDraft(
        object=data.get('object'),
        container_image=mapManagementInstanceCustomProvidersArchiveOutputDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapManagementInstanceCustomProvidersArchiveOutputDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapManagementInstanceCustomProvidersArchiveOutputDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputScmRepoProvider:
        return ManagementInstanceCustomProvidersArchiveOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputScmRepo:
        return ManagementInstanceCustomProvidersArchiveOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersArchiveOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputProviderPublisher:
        return ManagementInstanceCustomProvidersArchiveOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion:
        return ManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration:
        return ManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputProviderOauth:
        return ManagementInstanceCustomProvidersArchiveOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapManagementInstanceCustomProvidersArchiveOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutputProvider:
        return ManagementInstanceCustomProvidersArchiveOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapManagementInstanceCustomProvidersArchiveOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapManagementInstanceCustomProvidersArchiveOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapManagementInstanceCustomProvidersArchiveOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersArchiveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersArchiveOutput:
        return ManagementInstanceCustomProvidersArchiveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapManagementInstanceCustomProvidersArchiveOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapManagementInstanceCustomProvidersArchiveOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapManagementInstanceCustomProvidersArchiveOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersArchiveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

