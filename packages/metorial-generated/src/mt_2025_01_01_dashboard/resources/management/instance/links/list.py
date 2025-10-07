from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceLinksListOutputItemsPurpose:
    name: str
    identifier: str
@dataclass
class ManagementInstanceLinksListOutputItems:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    purpose: ManagementInstanceLinksListOutputItemsPurpose
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
@dataclass
class ManagementInstanceLinksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceLinksListOutput:
    items: List[ManagementInstanceLinksListOutputItems]
    pagination: ManagementInstanceLinksListOutputPagination


class mapManagementInstanceLinksListOutputItemsPurpose:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceLinksListOutputItemsPurpose:
        return ManagementInstanceLinksListOutputItemsPurpose(
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceLinksListOutputItemsPurpose, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceLinksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceLinksListOutputItems:
        return ManagementInstanceLinksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=mapManagementInstanceLinksListOutputItemsPurpose.from_dict(data.get('purpose')) if data.get('purpose') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceLinksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceLinksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceLinksListOutputPagination:
        return ManagementInstanceLinksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceLinksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceLinksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceLinksListOutput:
        return ManagementInstanceLinksListOutput(
        items=[mapManagementInstanceLinksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceLinksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceLinksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

