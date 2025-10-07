from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFilesListOutputItemsPurpose:
    name: str
    identifier: str
@dataclass
class DashboardInstanceFilesListOutputItems:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    purpose: DashboardInstanceFilesListOutputItemsPurpose
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
@dataclass
class DashboardInstanceFilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceFilesListOutput:
    items: List[DashboardInstanceFilesListOutputItems]
    pagination: DashboardInstanceFilesListOutputPagination


class mapDashboardInstanceFilesListOutputItemsPurpose:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesListOutputItemsPurpose:
        return DashboardInstanceFilesListOutputItemsPurpose(
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesListOutputItemsPurpose, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesListOutputItems:
        return DashboardInstanceFilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=mapDashboardInstanceFilesListOutputItemsPurpose.from_dict(data.get('purpose')) if data.get('purpose') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesListOutputPagination:
        return DashboardInstanceFilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesListOutput:
        return DashboardInstanceFilesListOutput(
        items=[mapDashboardInstanceFilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceFilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceFilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    purpose: Optional[str] = None
    organization_id: Optional[str] = None


class mapDashboardInstanceFilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFilesListQuery:
        return DashboardInstanceFilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        purpose=data.get('purpose'),
        organization_id=data.get('organization_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

