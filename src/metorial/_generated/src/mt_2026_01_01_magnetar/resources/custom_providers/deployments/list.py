from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersDeploymentsListOutputItemsCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsListOutputItemsImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersDeploymentsListOutputItemsActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsListOutputItemsScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsListOutputItemsScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersDeploymentsListOutputItemsScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersDeploymentsListOutputItemsScmPush:
    object: str
    id: str
    actor: CustomProvidersDeploymentsListOutputItemsScmPushActor
    commit: CustomProvidersDeploymentsListOutputItemsScmPushCommit
    repository: CustomProvidersDeploymentsListOutputItemsScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersDeploymentsListOutputItems:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersDeploymentsListOutputItemsActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersDeploymentsListOutputItemsCommit] = None
    immutable_bucket: Optional[CustomProvidersDeploymentsListOutputItemsImmutableBucket] = None
    scm_push: Optional[CustomProvidersDeploymentsListOutputItemsScmPush] = None
@dataclass
class CustomProvidersDeploymentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CustomProvidersDeploymentsListOutput:
    items: List[CustomProvidersDeploymentsListOutputItems]
    pagination: CustomProvidersDeploymentsListOutputPagination


class mapCustomProvidersDeploymentsListOutputItemsCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsCommit:
        return CustomProvidersDeploymentsListOutputItemsCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository:
        return CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink:
        return CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsImmutableBucket:
        return CustomProvidersDeploymentsListOutputItemsImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersDeploymentsListOutputItemsImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsActor:
        return CustomProvidersDeploymentsListOutputItemsActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsScmPushActor:
        return CustomProvidersDeploymentsListOutputItemsScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsScmPushCommit:
        return CustomProvidersDeploymentsListOutputItemsScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider:
        return CustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsScmPushRepository:
        return CustomProvidersDeploymentsListOutputItemsScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersDeploymentsListOutputItemsScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItemsScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItemsScmPush:
        return CustomProvidersDeploymentsListOutputItemsScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersDeploymentsListOutputItemsScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersDeploymentsListOutputItemsScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersDeploymentsListOutputItemsScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItemsScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputItems:
        return CustomProvidersDeploymentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersDeploymentsListOutputItemsCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapCustomProvidersDeploymentsListOutputItemsImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersDeploymentsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersDeploymentsListOutputItemsScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutputPagination:
        return CustomProvidersDeploymentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListOutput:
        return CustomProvidersDeploymentsListOutput(
        items=[mapCustomProvidersDeploymentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCustomProvidersDeploymentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersDeploymentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersDeploymentsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersDeploymentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    custom_provider_version_id: Optional[Union[str, List[str]]] = None
    custom_provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[CustomProvidersDeploymentsListQueryCreatedAt] = None
    updated_at: Optional[CustomProvidersDeploymentsListQueryUpdatedAt] = None


class mapCustomProvidersDeploymentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsListQuery:
        return CustomProvidersDeploymentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        custom_provider_id=data.get('custom_provider_id'),
        created_at=mapCustomProvidersDeploymentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCustomProvidersDeploymentsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

