from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceLinksListOutputItemsPurpose:
    name: str
    identifier: str
@dataclass
class DashboardInstanceLinksListOutputItems:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    purpose: DashboardInstanceLinksListOutputItemsPurpose
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
@dataclass
class DashboardInstanceLinksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceLinksListOutput:
    items: List[DashboardInstanceLinksListOutputItems]
    pagination: DashboardInstanceLinksListOutputPagination


class mapDashboardInstanceLinksListOutputItemsPurpose:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceLinksListOutputItemsPurpose:
        return DashboardInstanceLinksListOutputItemsPurpose(
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceLinksListOutputItemsPurpose, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceLinksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceLinksListOutputItems:
        return DashboardInstanceLinksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=mapDashboardInstanceLinksListOutputItemsPurpose.from_dict(data.get('purpose')) if data.get('purpose') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceLinksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceLinksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceLinksListOutputPagination:
        return DashboardInstanceLinksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceLinksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceLinksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceLinksListOutput:
        return DashboardInstanceLinksListOutput(
        items=[mapDashboardInstanceLinksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceLinksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceLinksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

