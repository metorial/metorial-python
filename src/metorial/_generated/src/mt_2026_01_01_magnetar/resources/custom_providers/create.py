from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersCreateOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersCreateOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class CustomProvidersCreateOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersCreateOutputDraftConfig:
    object: str
    schema: CustomProvidersCreateOutputDraftConfigSchema
    transformer: str
@dataclass
class CustomProvidersCreateOutputDraft:
    object: str
    config: CustomProvidersCreateOutputDraftConfig
    container_image: Optional[CustomProvidersCreateOutputDraftContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersCreateOutputDraftRemoteMcpServer] = None
@dataclass
class CustomProvidersCreateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCreateOutputScmRepo:
    object: str
    id: str
    provider: CustomProvidersCreateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCreateOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersCreateOutputProviderCurrentVersion:
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
class CustomProvidersCreateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersCreateOutputProviderOauth:
    status: str
    auto_registration: CustomProvidersCreateOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class CustomProvidersCreateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersCreateOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[CustomProvidersCreateOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersCreateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersCreateOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: CustomProvidersCreateOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersCreateOutputScmRepo] = None
    provider: Optional[CustomProvidersCreateOutputProvider] = None


class mapCustomProvidersCreateOutputDraftContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputDraftContainerImage:
        return CustomProvidersCreateOutputDraftContainerImage(
        object=data.get('object'),
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputDraftContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputDraftRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputDraftRemoteMcpServer:
        return CustomProvidersCreateOutputDraftRemoteMcpServer(
        object=data.get('object'),
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputDraftRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputDraftConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputDraftConfigSchema:
        return CustomProvidersCreateOutputDraftConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputDraftConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputDraftConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputDraftConfig:
        return CustomProvidersCreateOutputDraftConfig(
        object=data.get('object'),
        schema=mapCustomProvidersCreateOutputDraftConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputDraftConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputDraft:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputDraft:
        return CustomProvidersCreateOutputDraft(
        object=data.get('object'),
        container_image=mapCustomProvidersCreateOutputDraftContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapCustomProvidersCreateOutputDraftRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        config=mapCustomProvidersCreateOutputDraftConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputDraft, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputScmRepoProvider:
        return CustomProvidersCreateOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputScmRepo:
        return CustomProvidersCreateOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCreateOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputProviderPublisher:
        return CustomProvidersCreateOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputProviderCurrentVersion:
        return CustomProvidersCreateOutputProviderCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersCreateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputProviderOauthAutoRegistration:
        return CustomProvidersCreateOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputProviderOauth:
        return CustomProvidersCreateOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapCustomProvidersCreateOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutputProvider:
        return CustomProvidersCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapCustomProvidersCreateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapCustomProvidersCreateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapCustomProvidersCreateOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutput:
        return CustomProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapCustomProvidersCreateOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapCustomProvidersCreateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapCustomProvidersCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class CustomProvidersCreateBody:
    name: str
    from_: Dict[str, Any]
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[CustomProvidersCreateBodyConfig] = None


class mapCustomProvidersCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateBodyConfig:
        return CustomProvidersCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateBody:
        return CustomProvidersCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_=data.get('from'),
        config=mapCustomProvidersCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

