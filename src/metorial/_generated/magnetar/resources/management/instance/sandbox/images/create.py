from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxImagesCreateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    owner: str
    status: str
    regions: List[str]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    identifier: Optional[str] = None
    latest_version_id: Optional[str] = None
    latest_version_number: Optional[float] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceSandboxImagesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesCreateOutput:
        return ManagementInstanceSandboxImagesCreateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        owner=data.get('owner'),
        status=data.get('status'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        regions=data.get('regions', []),
        latest_version_id=data.get('latest_version_id'),
        latest_version_number=data.get('latest_version_number'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxImagesCreateBody:
    name: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceSandboxImagesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesCreateBody:
        return ManagementInstanceSandboxImagesCreateBody(
        name=data.get('name'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

