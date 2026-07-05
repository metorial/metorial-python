from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersArchiveOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersArchiveOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class CustomProvidersArchiveOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersArchiveOutputDraftConfig:
    object: str
    schema: CustomProvidersArchiveOutputDraftConfigSchema
    transformer: str
@dataclass
class CustomProvidersArchiveOutputDraft:
    object: str
    config: CustomProvidersArchiveOutputDraftConfig
    container_image: Optional[CustomProvidersArchiveOutputDraftContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersArchiveOutputDraftRemoteMcpServer] = None
@dataclass
class CustomProvidersArchiveOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersArchiveOutputScmRepo:
    object: str
    id: str
    provider: CustomProvidersArchiveOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersArchiveOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersArchiveOutputProviderCurrentVersion:
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
class CustomProvidersArchiveOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersArchiveOutputProviderOauth:
    status: str
    auto_registration: CustomProvidersArchiveOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class CustomProvidersArchiveOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersArchiveOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[CustomProvidersArchiveOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersArchiveOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersArchiveOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: CustomProvidersArchiveOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersArchiveOutputScmRepo] = None
    provider: Optional[CustomProvidersArchiveOutputProvider] = None


class mapCustomProvidersArchiveOutputDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputDraftContainerImage:
        return CustomProvidersArchiveOutputDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputDraftRemoteMcpServer:
        return CustomProvidersArchiveOutputDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputDraftConfigSchema:
        return CustomProvidersArchiveOutputDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputDraftConfig:
        return CustomProvidersArchiveOutputDraftConfig(
        object=data.get('object'),
        schema=mapCustomProvidersArchiveOutputDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputDraft:
        return CustomProvidersArchiveOutputDraft(
        object=data.get('object'),
        container_image=mapCustomProvidersArchiveOutputDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapCustomProvidersArchiveOutputDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapCustomProvidersArchiveOutputDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputScmRepoProvider:
        return CustomProvidersArchiveOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputScmRepo:
        return CustomProvidersArchiveOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersArchiveOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputProviderPublisher:
        return CustomProvidersArchiveOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputProviderCurrentVersion:
        return CustomProvidersArchiveOutputProviderCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersArchiveOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputProviderOauthAutoRegistration:
        return CustomProvidersArchiveOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputProviderOauth:
        return CustomProvidersArchiveOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapCustomProvidersArchiveOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutputProvider:
        return CustomProvidersArchiveOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapCustomProvidersArchiveOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapCustomProvidersArchiveOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapCustomProvidersArchiveOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersArchiveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersArchiveOutput:
        return CustomProvidersArchiveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapCustomProvidersArchiveOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapCustomProvidersArchiveOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapCustomProvidersArchiveOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersArchiveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

