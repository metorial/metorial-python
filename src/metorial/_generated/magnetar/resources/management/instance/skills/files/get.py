from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsFilesGetOutput:
    object: str
    path: str
    kind: str
    size: float
    etag: str
    skill_id: str
    store_item_id: str
    updated_at: datetime
    document_id: Optional[str] = None
    file_id: Optional[str] = None
    content: Optional[str] = None
    download_url: Optional[str] = None


class mapManagementInstanceSkillsFilesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsFilesGetOutput:
        return ManagementInstanceSkillsFilesGetOutput(
        object=data.get('object'),
        path=data.get('path'),
        kind=data.get('kind'),
        size=data.get('size'),
        etag=data.get('etag'),
        skill_id=data.get('skill_id'),
        store_item_id=data.get('store_item_id'),
        document_id=data.get('document_id'),
        file_id=data.get('file_id'),
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        content=data.get('content'),
        download_url=data.get('download_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsFilesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsFilesGetQuery:
    path: str


class mapManagementInstanceSkillsFilesGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsFilesGetQuery:
        return ManagementInstanceSkillsFilesGetQuery(
        path=data.get('path')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsFilesGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

