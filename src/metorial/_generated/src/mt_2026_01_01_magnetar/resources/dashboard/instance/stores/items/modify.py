from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsFile:
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
    created_by: Optional[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutputItemsDocument:
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
    created_by: Optional[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutputItems:
    object: str
    id: str
    kind: str
    path: str
    store_id: str
    created_at: datetime
    updated_at: datetime
    directory_id: Optional[str] = None
    file: Optional[DashboardInstanceStoresItemsModifyOutputItemsFile] = None
    document: Optional[DashboardInstanceStoresItemsModifyOutputItemsDocument] = None
@dataclass
class DashboardInstanceStoresItemsModifyOutput:
    object: str
    items: List[DashboardInstanceStoresItemsModifyOutputItems]


class mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams:
        return DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor:
        return DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer:
        return DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy:
        return DashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsFile:
        return DashboardInstanceStoresItemsModifyOutputItemsFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapDashboardInstanceStoresItemsModifyOutputItemsFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams:
        return DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor:
        return DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer:
        return DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy:
        return DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItemsDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItemsDocument:
        return DashboardInstanceStoresItemsModifyOutputItemsDocument(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('file_id'),
        parent_document_id=data.get('parent_document_id'),
        current_version_id=data.get('current_version_id'),
        created_by=mapDashboardInstanceStoresItemsModifyOutputItemsDocumentCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItemsDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutputItems:
        return DashboardInstanceStoresItemsModifyOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        kind=data.get('kind'),
        path=data.get('path'),
        store_id=data.get('store_id'),
        directory_id=data.get('directory_id'),
        file=mapDashboardInstanceStoresItemsModifyOutputItemsFile.from_dict(data.get('file')) if data.get('file') else None,
        document=mapDashboardInstanceStoresItemsModifyOutputItemsDocument.from_dict(data.get('document')) if data.get('document') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyOutput:
        return DashboardInstanceStoresItemsModifyOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceStoresItemsModifyOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceStoresItemsModifyBodyOperations:
    type: Optional[str] = None
    item_id: Optional[str] = None
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    path: Optional[str] = None
@dataclass
class DashboardInstanceStoresItemsModifyBody:
    operations: List[DashboardInstanceStoresItemsModifyBodyOperations]


class mapDashboardInstanceStoresItemsModifyBodyOperations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyBodyOperations:
        return DashboardInstanceStoresItemsModifyBodyOperations(
        type=data.get('type'),
        item_id=data.get('itemId'),
        file_id=data.get('fileId'),
        document_id=data.get('documentId'),
        path=data.get('path')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyBodyOperations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresItemsModifyBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresItemsModifyBody:
        return DashboardInstanceStoresItemsModifyBody(
        operations=[mapDashboardInstanceStoresItemsModifyBodyOperations.from_dict(item) for item in data.get('operations', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresItemsModifyBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

