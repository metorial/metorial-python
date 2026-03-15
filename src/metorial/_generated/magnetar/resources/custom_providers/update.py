from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersUpdateOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersUpdateOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class CustomProvidersUpdateOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersUpdateOutputDraftConfig:
    object: str
    schema: CustomProvidersUpdateOutputDraftConfigSchema
    transformer: str
@dataclass
class CustomProvidersUpdateOutputDraft:
    object: str
    config: CustomProvidersUpdateOutputDraftConfig
    container_image: Optional[CustomProvidersUpdateOutputDraftContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersUpdateOutputDraftRemoteMcpServer] = None
@dataclass
class CustomProvidersUpdateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersUpdateOutputScmRepo:
    object: str
    id: str
    provider: CustomProvidersUpdateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersUpdateOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersUpdateOutputProviderCurrentVersion:
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
class CustomProvidersUpdateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersUpdateOutputProviderOauth:
    status: str
    auto_registration: CustomProvidersUpdateOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class CustomProvidersUpdateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersUpdateOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[CustomProvidersUpdateOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersUpdateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersUpdateOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: CustomProvidersUpdateOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersUpdateOutputScmRepo] = None
    provider: Optional[CustomProvidersUpdateOutputProvider] = None


class mapCustomProvidersUpdateOutputDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftContainerImage:
        return CustomProvidersUpdateOutputDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftRemoteMcpServer:
        return CustomProvidersUpdateOutputDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftConfigSchema:
        return CustomProvidersUpdateOutputDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftConfig:
        return CustomProvidersUpdateOutputDraftConfig(
        object=data.get('object'),
        schema=mapCustomProvidersUpdateOutputDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraft:
        return CustomProvidersUpdateOutputDraft(
        object=data.get('object'),
        container_image=mapCustomProvidersUpdateOutputDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapCustomProvidersUpdateOutputDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapCustomProvidersUpdateOutputDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputScmRepoProvider:
        return CustomProvidersUpdateOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputScmRepo:
        return CustomProvidersUpdateOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersUpdateOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderPublisher:
        return CustomProvidersUpdateOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderCurrentVersion:
        return CustomProvidersUpdateOutputProviderCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderOauthAutoRegistration:
        return CustomProvidersUpdateOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderOauth:
        return CustomProvidersUpdateOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapCustomProvidersUpdateOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProvider:
        return CustomProvidersUpdateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapCustomProvidersUpdateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapCustomProvidersUpdateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapCustomProvidersUpdateOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutput:
        return CustomProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapCustomProvidersUpdateOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapCustomProvidersUpdateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapCustomProvidersUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    readme: Optional[str] = None


class mapCustomProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateBody:
        return CustomProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

