from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxImageBuildsGetOutputFailure:
    code: str
    message: str
@dataclass
class SandboxImageBuildsGetOutputRegions:
    region: str
    status: str
@dataclass
class SandboxImageBuildsGetOutput:
    object: str
    id: str
    image_id: str
    version_id: str
    status: str
    disk_size_bytes: float
    regions: List[SandboxImageBuildsGetOutputRegions]
    has_logs: bool
    created_at: datetime
    version_number: Optional[float] = None
    file_id: Optional[str] = None
    failure: Optional[SandboxImageBuildsGetOutputFailure] = None
    dockerfile_path: Optional[str] = None
    context_path: Optional[str] = None
    target: Optional[str] = None
    build_arg_names: Optional[List[str]] = None
    timeout_seconds: Optional[float] = None
    context_uploaded_at: Optional[datetime] = None
    built_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class mapSandboxImageBuildsGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImageBuildsGetOutputFailure:
        return SandboxImageBuildsGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImageBuildsGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImageBuildsGetOutputRegions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImageBuildsGetOutputRegions:
        return SandboxImageBuildsGetOutputRegions(
        region=data.get('region'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxImageBuildsGetOutputRegions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxImageBuildsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxImageBuildsGetOutput:
        return SandboxImageBuildsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        image_id=data.get('image_id'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        file_id=data.get('file_id'),
        status=data.get('status'),
        failure=mapSandboxImageBuildsGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        dockerfile_path=data.get('dockerfile_path'),
        context_path=data.get('context_path'),
        target=data.get('target'),
        build_arg_names=data.get('build_arg_names', []),
        timeout_seconds=data.get('timeout_seconds'),
        disk_size_bytes=data.get('disk_size_bytes'),
        regions=[mapSandboxImageBuildsGetOutputRegions.from_dict(item) for item in data.get('regions', []) if item],
        has_logs=data.get('has_logs'),
        context_uploaded_at=datetime.fromisoformat(data.get('context_uploaded_at').replace('Z', '+00:00')) if data.get('context_uploaded_at') else None,
        built_at=datetime.fromisoformat(data.get('built_at').replace('Z', '+00:00')) if data.get('built_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at').replace('Z', '+00:00')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxImageBuildsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

