from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFilesListOutputItemsPurpose:
    name: str
    identifier: str
@dataclass
class ManagementInstanceFilesListOutputItems:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    purpose: ManagementInstanceFilesListOutputItemsPurpose
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
@dataclass
class ManagementInstanceFilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceFilesListOutput:
    items: List[ManagementInstanceFilesListOutputItems]
    pagination: ManagementInstanceFilesListOutputPagination


class mapManagementInstanceFilesListOutputItemsPurpose:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItemsPurpose:
        return ManagementInstanceFilesListOutputItemsPurpose(
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItemsPurpose, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItems:
        return ManagementInstanceFilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=mapManagementInstanceFilesListOutputItemsPurpose.from_dict(data.get('purpose')) if data.get('purpose') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputPagination:
        return ManagementInstanceFilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutput:
        return ManagementInstanceFilesListOutput(
        items=[mapManagementInstanceFilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceFilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    purpose: Optional[str] = None
    organization_id: Optional[str] = None


class mapManagementInstanceFilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListQuery:
        return ManagementInstanceFilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        purpose=data.get('purpose'),
        organization_id=data.get('organization_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

