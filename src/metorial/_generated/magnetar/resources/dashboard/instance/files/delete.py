from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceFilesDeleteOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceFilesDeleteOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceFilesDeleteOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceFilesDeleteOutputCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceFilesDeleteOutputCreatedByConsumer] = None
@dataclass
class DashboardInstanceFilesDeleteOutput:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    title: str
    purpose: str
    created_at: datetime
    updated_at: datetime
    created_by: Optional[DashboardInstanceFilesDeleteOutputCreatedBy] = None


class mapDashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams:
        return DashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesDeleteOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesDeleteOutputCreatedByOrganizationActor:
        return DashboardInstanceFilesDeleteOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceFilesDeleteOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesDeleteOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesDeleteOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesDeleteOutputCreatedByConsumer:
        return DashboardInstanceFilesDeleteOutputCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesDeleteOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesDeleteOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesDeleteOutputCreatedBy:
        return DashboardInstanceFilesDeleteOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceFilesDeleteOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceFilesDeleteOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesDeleteOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesDeleteOutput:
        return DashboardInstanceFilesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapDashboardInstanceFilesDeleteOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

