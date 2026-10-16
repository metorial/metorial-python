from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxImagesBuildsCreateOutputFailure:
    code: str
    message: str
@dataclass
class SandboxImagesBuildsCreateOutputRegions:
    region: str
    status: str
@dataclass
class SandboxImagesBuildsCreateOutput:
    object: str
    id: str
    image_id: str
    version_id: str
    status: str
    disk_size_bytes: float
    regions: List[SandboxImagesBuildsCreateOutputRegions]
    has_logs: bool
    created_at: datetime
    version_number: Optional[float] = None
    file_id: Optional[str] = None
    failure: Optional[SandboxImagesBuildsCreateOutputFailure] = None
    dockerfile_path: Optional[str] = None
    context_path: Optional[str] = None
    target: Optional[str] = None
    build_arg_names: Optional[List[str]] = None
    timeout_seconds: Optional[float] = None
    context_uploaded_at: Optional[datetime] = None
    built_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class mapSandboxImagesBuildsCreateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesBuildsCreateOutputFailure:
        return SandboxImagesBuildsCreateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesBuildsCreateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImagesBuildsCreateOutputRegions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesBuildsCreateOutputRegions:
        return SandboxImagesBuildsCreateOutputRegions(
        region=data.get('region'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesBuildsCreateOutputRegions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImagesBuildsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesBuildsCreateOutput:
        return SandboxImagesBuildsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        image_id=data.get('image_id'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        file_id=data.get('file_id'),
        status=data.get('status'),
        failure=mapSandboxImagesBuildsCreateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        dockerfile_path=data.get('dockerfile_path'),
        context_path=data.get('context_path'),
        target=data.get('target'),
        build_arg_names=data.get('build_arg_names', []),
        timeout_seconds=data.get('timeout_seconds'),
        disk_size_bytes=data.get('disk_size_bytes'),
        regions=[mapSandboxImagesBuildsCreateOutputRegions.from_dict(item) for item in data.get('regions', []) if item],
        has_logs=data.get('has_logs'),
        context_uploaded_at=datetime.fromisoformat(data.get('context_uploaded_at').replace('Z', '+00:00')) if data.get('context_uploaded_at') else None,
        built_at=datetime.fromisoformat(data.get('built_at').replace('Z', '+00:00')) if data.get('built_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at').replace('Z', '+00:00')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesBuildsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxImagesBuildsCreateBody:
    file_id: str
    dockerfile_path: Optional[str] = None
    context_path: Optional[str] = None
    target: Optional[str] = None
    build_args: Optional[Dict[str, str]] = None
    timeout_seconds: Optional[float] = None
    disk_size_bytes: Optional[float] = None


class mapSandboxImagesBuildsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImagesBuildsCreateBody:
        return SandboxImagesBuildsCreateBody(
        file_id=data.get('file_id'),
        dockerfile_path=data.get('dockerfile_path'),
        context_path=data.get('context_path'),
        target=data.get('target'),
        build_args=data.get('build_args'),
        timeout_seconds=data.get('timeout_seconds'),
        disk_size_bytes=data.get('disk_size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImagesBuildsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

