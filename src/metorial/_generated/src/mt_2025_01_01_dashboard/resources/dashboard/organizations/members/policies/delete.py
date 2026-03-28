from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsMembersPoliciesDeleteOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsMembersPoliciesDeleteOutputActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsMembersPoliciesDeleteOutputActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsMembersPoliciesDeleteOutputActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsMembersPoliciesDeleteOutput:
    object: str
    id: str
    status: str
    role: str
    user_id: str
    organization_id: str
    actor_id: str
    policies: List[DashboardOrganizationsMembersPoliciesDeleteOutputPolicies]
    last_active_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: DashboardOrganizationsMembersPoliciesDeleteOutputActor


class mapDashboardOrganizationsMembersPoliciesDeleteOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesDeleteOutputPolicies:
        return DashboardOrganizationsMembersPoliciesDeleteOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesDeleteOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsMembersPoliciesDeleteOutputActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesDeleteOutputActorTeams:
        return DashboardOrganizationsMembersPoliciesDeleteOutputActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesDeleteOutputActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsMembersPoliciesDeleteOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesDeleteOutputActor:
        return DashboardOrganizationsMembersPoliciesDeleteOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsMembersPoliciesDeleteOutputActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesDeleteOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsMembersPoliciesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsMembersPoliciesDeleteOutput:
        return DashboardOrganizationsMembersPoliciesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role'),
        user_id=data.get('user_id'),
        organization_id=data.get('organization_id'),
        actor_id=data.get('actor_id'),
        policies=[mapDashboardOrganizationsMembersPoliciesDeleteOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsMembersPoliciesDeleteOutputActor.from_dict(data.get('actor')) if data.get('actor') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsMembersPoliciesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

