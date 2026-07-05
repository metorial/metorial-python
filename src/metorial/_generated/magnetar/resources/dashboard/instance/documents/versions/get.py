from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsVersionsGetOutputEditorsConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsVersionsGetOutputEditors:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsVersionsGetOutputEditorsConsumer] = None
@dataclass
class DashboardInstanceDocumentsVersionsGetOutput:
    object: str
    id: str
    document_id: str
    version_number: float
    content: str
    editors: List[DashboardInstanceDocumentsVersionsGetOutputEditors]
    created_at: datetime
    previous_version_id: Optional[str] = None
    list_edited_at: Optional[datetime] = None


class mapDashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams:
        return DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor:
        return DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsGetOutputEditorsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsGetOutputEditorsConsumer:
        return DashboardInstanceDocumentsVersionsGetOutputEditorsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsGetOutputEditorsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsGetOutputEditors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsGetOutputEditors:
        return DashboardInstanceDocumentsVersionsGetOutputEditors(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsVersionsGetOutputEditorsOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsVersionsGetOutputEditorsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsGetOutputEditors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsGetOutput:
        return DashboardInstanceDocumentsVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        version_number=data.get('version_number'),
        previous_version_id=data.get('previous_version_id'),
        list_edited_at=datetime.fromisoformat(data.get('list_edited_at').replace('Z', '+00:00')) if data.get('list_edited_at') else None,
        content=data.get('content'),
        editors=[mapDashboardInstanceDocumentsVersionsGetOutputEditors.from_dict(item) for item in data.get('editors', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

