from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushActor
    commit: DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushCommit
    repository: DashboardInstanceCustomProvidersDeploymentsGetOutputScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersDeploymentsGetOutputActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersDeploymentsGetOutputCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersDeploymentsGetOutputScmPush] = None


class mapDashboardInstanceCustomProvidersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetOutput:
        return DashboardInstanceCustomProvidersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersDeploymentsGetOutputCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersDeploymentsGetOutputImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersDeploymentsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersDeploymentsGetOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

