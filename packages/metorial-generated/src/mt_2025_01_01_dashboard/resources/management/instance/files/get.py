from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFilesGetOutputPurpose:
    name: str
    identifier: str
@dataclass
class ManagementInstanceFilesGetOutput:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    purpose: ManagementInstanceFilesGetOutputPurpose
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None


class mapManagementInstanceFilesGetOutputPurpose:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesGetOutputPurpose:
        return ManagementInstanceFilesGetOutputPurpose(
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesGetOutputPurpose, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesGetOutput:
        return ManagementInstanceFilesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=mapManagementInstanceFilesGetOutputPurpose.from_dict(data.get('purpose')) if data.get('purpose') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

