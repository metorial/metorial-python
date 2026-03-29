from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutputScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushActor
    commit: ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushCommit
    repository: ManagementInstanceCustomProvidersDeploymentsGetOutputScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersDeploymentsGetOutputActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersDeploymentsGetOutputCommit] = None
    immutable_bucket: Optional[ManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucket] = None
    scm_push: Optional[ManagementInstanceCustomProvidersDeploymentsGetOutputScmPush] = None


class mapManagementInstanceCustomProvidersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersDeploymentsGetOutput:
        return ManagementInstanceCustomProvidersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersDeploymentsGetOutputCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapManagementInstanceCustomProvidersDeploymentsGetOutputImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapManagementInstanceCustomProvidersDeploymentsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersDeploymentsGetOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

