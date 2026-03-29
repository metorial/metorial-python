from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsMembersPoliciesCreateOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsMembersPoliciesCreateOutputActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsMembersPoliciesCreateOutputActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsMembersPoliciesCreateOutputActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsMembersPoliciesCreateOutput:
    object: str
    id: str
    status: str
    role: str
    user_id: str
    organization_id: str
    actor_id: str
    policies: List[DashboardOrganizationsMembersPoliciesCreateOutputPolicies]
    last_active_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: DashboardOrganizationsMembersPoliciesCreateOutputActor


class mapDashboardOrganizationsMembersPoliciesCreateOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesCreateOutputPolicies:
        return DashboardOrganizationsMembersPoliciesCreateOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesCreateOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsMembersPoliciesCreateOutputActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesCreateOutputActorTeams:
        return DashboardOrganizationsMembersPoliciesCreateOutputActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesCreateOutputActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsMembersPoliciesCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesCreateOutputActor:
        return DashboardOrganizationsMembersPoliciesCreateOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsMembersPoliciesCreateOutputActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsMembersPoliciesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesCreateOutput:
        return DashboardOrganizationsMembersPoliciesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role'),
        user_id=data.get('user_id'),
        organization_id=data.get('organization_id'),
        actor_id=data.get('actor_id'),
        policies=[mapDashboardOrganizationsMembersPoliciesCreateOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsMembersPoliciesCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsMembersPoliciesCreateBody:
    access_policy_id: str


class mapDashboardOrganizationsMembersPoliciesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesCreateBody:
        return DashboardOrganizationsMembersPoliciesCreateBody(
        access_policy_id=data.get('access_policy_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

