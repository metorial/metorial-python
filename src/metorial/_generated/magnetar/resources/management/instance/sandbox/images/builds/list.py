from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxImagesBuildsListOutputItemsFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxImagesBuildsListOutputItemsRegions:
    region: str
    status: str
@dataclass
class ManagementInstanceSandboxImagesBuildsListOutputItems:
    object: str
    id: str
    image_id: str
    version_id: str
    status: str
    disk_size_bytes: float
    regions: List[ManagementInstanceSandboxImagesBuildsListOutputItemsRegions]
    has_logs: bool
    created_at: datetime
    version_number: Optional[float] = None
    file_id: Optional[str] = None
    failure: Optional[ManagementInstanceSandboxImagesBuildsListOutputItemsFailure] = None
    dockerfile_path: Optional[str] = None
    context_path: Optional[str] = None
    target: Optional[str] = None
    build_arg_names: Optional[List[str]] = None
    timeout_seconds: Optional[float] = None
    context_uploaded_at: Optional[datetime] = None
    built_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSandboxImagesBuildsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSandboxImagesBuildsListOutput:
    items: List[ManagementInstanceSandboxImagesBuildsListOutputItems]
    pagination: ManagementInstanceSandboxImagesBuildsListOutputPagination


class mapManagementInstanceSandboxImagesBuildsListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesBuildsListOutputItemsFailure:
        return ManagementInstanceSandboxImagesBuildsListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesBuildsListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImagesBuildsListOutputItemsRegions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesBuildsListOutputItemsRegions:
        return ManagementInstanceSandboxImagesBuildsListOutputItemsRegions(
        region=data.get('region'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesBuildsListOutputItemsRegions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImagesBuildsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesBuildsListOutputItems:
        return ManagementInstanceSandboxImagesBuildsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        image_id=data.get('image_id'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        file_id=data.get('file_id'),
        status=data.get('status'),
        failure=mapManagementInstanceSandboxImagesBuildsListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        dockerfile_path=data.get('dockerfile_path'),
        context_path=data.get('context_path'),
        target=data.get('target'),
        build_arg_names=data.get('build_arg_names', []),
        timeout_seconds=data.get('timeout_seconds'),
        disk_size_bytes=data.get('disk_size_bytes'),
        regions=[mapManagementInstanceSandboxImagesBuildsListOutputItemsRegions.from_dict(item) for item in data.get('regions', []) if item],
        has_logs=data.get('has_logs'),
        context_uploaded_at=datetime.fromisoformat(data.get('context_uploaded_at').replace('Z', '+00:00')) if data.get('context_uploaded_at') else None,
        built_at=datetime.fromisoformat(data.get('built_at').replace('Z', '+00:00')) if data.get('built_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at').replace('Z', '+00:00')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesBuildsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImagesBuildsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesBuildsListOutputPagination:
        return ManagementInstanceSandboxImagesBuildsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesBuildsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImagesBuildsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesBuildsListOutput:
        return ManagementInstanceSandboxImagesBuildsListOutput(
        items=[mapManagementInstanceSandboxImagesBuildsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSandboxImagesBuildsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesBuildsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxImagesBuildsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    image_version_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSandboxImagesBuildsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImagesBuildsListQuery:
        return ManagementInstanceSandboxImagesBuildsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        image_version_id=data.get('image_version_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImagesBuildsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

