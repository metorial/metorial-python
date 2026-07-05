from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsCloneOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCloneOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCloneOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DocumentsCloneOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCloneOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCloneOutputCreatedByOrganizationActor] = None
    consumer: Optional[DocumentsCloneOutputCreatedByConsumer] = None
@dataclass
class DocumentsCloneOutput:
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
    created_by: Optional[DocumentsCloneOutputCreatedBy] = None


class mapDocumentsCloneOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCloneOutputCreatedByOrganizationActorTeams:
        return DocumentsCloneOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCloneOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCloneOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCloneOutputCreatedByOrganizationActor:
        return DocumentsCloneOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDocumentsCloneOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCloneOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCloneOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCloneOutputCreatedByConsumer:
        return DocumentsCloneOutputCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCloneOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCloneOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCloneOutputCreatedBy:
        return DocumentsCloneOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCloneOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCloneOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCloneOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCloneOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCloneOutput:
        return DocumentsCloneOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('file_id'),
        parent_document_id=data.get('parent_document_id'),
        current_version_id=data.get('current_version_id'),
        created_by=mapDocumentsCloneOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCloneOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DocumentsCloneBody:
    target_document_id: Optional[str] = None
    title: Optional[str] = None


class mapDocumentsCloneBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCloneBody:
        return DocumentsCloneBody(
        target_document_id=data.get('target_document_id'),
        title=data.get('title')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCloneBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

