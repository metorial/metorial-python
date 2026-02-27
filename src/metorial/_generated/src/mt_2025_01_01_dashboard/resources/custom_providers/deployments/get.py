from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersDeploymentsGetOutputCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsGetOutputImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersDeploymentsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsGetOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsGetOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsGetOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersDeploymentsGetOutputScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersDeploymentsGetOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersDeploymentsGetOutputScmPush:
    object: str
    id: str
    actor: CustomProvidersDeploymentsGetOutputScmPushActor
    commit: CustomProvidersDeploymentsGetOutputScmPushCommit
    repository: CustomProvidersDeploymentsGetOutputScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersDeploymentsGetOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersDeploymentsGetOutputActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersDeploymentsGetOutputCommit] = None
    immutable_bucket: Optional[CustomProvidersDeploymentsGetOutputImmutableBucket] = None
    scm_push: Optional[CustomProvidersDeploymentsGetOutputScmPush] = None


class mapCustomProvidersDeploymentsGetOutputCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputCommit:
        return CustomProvidersDeploymentsGetOutputCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository:
        return CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink:
        return CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputImmutableBucket:
        return CustomProvidersDeploymentsGetOutputImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputActor:
        return CustomProvidersDeploymentsGetOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputScmPushActor:
        return CustomProvidersDeploymentsGetOutputScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputScmPushCommit:
        return CustomProvidersDeploymentsGetOutputScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputScmPushRepositoryProvider:
        return CustomProvidersDeploymentsGetOutputScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputScmPushRepository:
        return CustomProvidersDeploymentsGetOutputScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersDeploymentsGetOutputScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutputScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutputScmPush:
        return CustomProvidersDeploymentsGetOutputScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersDeploymentsGetOutputScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersDeploymentsGetOutputScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersDeploymentsGetOutputScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutputScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetOutput:
        return CustomProvidersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersDeploymentsGetOutputCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapCustomProvidersDeploymentsGetOutputImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersDeploymentsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersDeploymentsGetOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
