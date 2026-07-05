from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceDocumentsVersionsGetOutputEditorsConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsVersionsGetOutputEditors:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor] = None
    consumer: Optional[ManagementInstanceDocumentsVersionsGetOutputEditorsConsumer] = None
@dataclass
class ManagementInstanceDocumentsVersionsGetOutput:
    object: str
    id: str
    document_id: str
    version_number: float
    content: str
    editors: List[ManagementInstanceDocumentsVersionsGetOutputEditors]
    created_at: datetime
    previous_version_id: Optional[str] = None
    list_edited_at: Optional[datetime] = None


class mapManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams:
        return ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor:
        return ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsGetOutputEditorsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsGetOutputEditorsConsumer:
        return ManagementInstanceDocumentsVersionsGetOutputEditorsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsGetOutputEditorsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsGetOutputEditors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsGetOutputEditors:
        return ManagementInstanceDocumentsVersionsGetOutputEditors(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceDocumentsVersionsGetOutputEditorsOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceDocumentsVersionsGetOutputEditorsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsGetOutputEditors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsGetOutput:
        return ManagementInstanceDocumentsVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        version_number=data.get('version_number'),
        previous_version_id=data.get('previous_version_id'),
        list_edited_at=datetime.fromisoformat(data.get('list_edited_at').replace('Z', '+00:00')) if data.get('list_edited_at') else None,
        content=data.get('content'),
        editors=[mapManagementInstanceDocumentsVersionsGetOutputEditors.from_dict(item) for item in data.get('editors', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

