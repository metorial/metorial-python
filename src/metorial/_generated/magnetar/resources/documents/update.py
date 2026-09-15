from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsUpdateOutputCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsUpdateOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsUpdateOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsUpdateOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsUpdateOutputCreatedByOrganizationActorMember] = None
@dataclass
class DocumentsUpdateOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsUpdateOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsUpdateOutputCreatedByOrganizationActor] = None
    consumer: Optional[DocumentsUpdateOutputCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsUpdateOutput:
    object: str
    id: str
    status: str
    title: str
    content: str
    file_id: str
    created_at: datetime
    updated_at: datetime
    parent_document_id: Optional[str] = None
    current_version_id: Optional[str] = None
    created_by: Optional[DocumentsUpdateOutputCreatedBy] = None


class mapDocumentsUpdateOutputCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateOutputCreatedByOrganizationActorMember:
        return DocumentsUpdateOutputCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateOutputCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsUpdateOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateOutputCreatedByOrganizationActorTeams:
        return DocumentsUpdateOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsUpdateOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateOutputCreatedByOrganizationActor:
        return DocumentsUpdateOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsUpdateOutputCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsUpdateOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsUpdateOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateOutputCreatedByConsumer:
        return DocumentsUpdateOutputCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsUpdateOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateOutputCreatedBy:
        return DocumentsUpdateOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsUpdateOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsUpdateOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateOutput:
        return DocumentsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('file_id'),
        parent_document_id=data.get('parent_document_id'),
        current_version_id=data.get('current_version_id'),
        created_by=mapDocumentsUpdateOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DocumentsUpdateBody:
    title: Optional[str] = None
    content: Optional[str] = None


class mapDocumentsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsUpdateBody:
        return DocumentsUpdateBody(
        title=data.get('title'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

