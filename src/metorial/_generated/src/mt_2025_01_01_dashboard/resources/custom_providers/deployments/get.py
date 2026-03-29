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
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

