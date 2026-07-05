from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceStoresItemsGetOutputFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceStoresItemsGetOutputFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceStoresItemsGetOutputFileCreatedByConsumer] = None
@dataclass
class ManagementInstanceStoresItemsGetOutputFile:
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
    created_by: Optional[ManagementInstanceStoresItemsGetOutputFileCreatedBy] = None
@dataclass
class ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceStoresItemsGetOutputDocumentCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer] = None
@dataclass
class ManagementInstanceStoresItemsGetOutputDocument:
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
    created_by: Optional[ManagementInstanceStoresItemsGetOutputDocumentCreatedBy] = None
@dataclass
class ManagementInstanceStoresItemsGetOutput:
    object: str
    id: str
    kind: str
    path: str
    store_id: str
    created_at: datetime
    updated_at: datetime
    directory_id: Optional[str] = None
    file: Optional[ManagementInstanceStoresItemsGetOutputFile] = None
    document: Optional[ManagementInstanceStoresItemsGetOutputDocument] = None


class mapManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams:
        return ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor:
        return ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputFileCreatedByConsumer:
        return ManagementInstanceStoresItemsGetOutputFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputFileCreatedBy:
        return ManagementInstanceStoresItemsGetOutputFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceStoresItemsGetOutputFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceStoresItemsGetOutputFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputFile:
        return ManagementInstanceStoresItemsGetOutputFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapManagementInstanceStoresItemsGetOutputFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams:
        return ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor:
        return ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer:
        return ManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputDocumentCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputDocumentCreatedBy:
        return ManagementInstanceStoresItemsGetOutputDocumentCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceStoresItemsGetOutputDocumentCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceStoresItemsGetOutputDocumentCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputDocumentCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutputDocument:
        return ManagementInstanceStoresItemsGetOutputDocument(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('file_id'),
        parent_document_id=data.get('parent_document_id'),
        current_version_id=data.get('current_version_id'),
        created_by=mapManagementInstanceStoresItemsGetOutputDocumentCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresItemsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresItemsGetOutput:
        return ManagementInstanceStoresItemsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        kind=data.get('kind'),
        path=data.get('path'),
        store_id=data.get('store_id'),
        directory_id=data.get('directory_id'),
        file=mapManagementInstanceStoresItemsGetOutputFile.from_dict(data.get('file')) if data.get('file') else None,
        document=mapManagementInstanceStoresItemsGetOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresItemsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

