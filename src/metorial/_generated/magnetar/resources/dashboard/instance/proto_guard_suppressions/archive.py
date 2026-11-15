from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProtoGuardSuppressionsArchiveOutputFilter:
    object: str
    id: str
    key: str
    name: str
@dataclass
class DashboardInstanceProtoGuardSuppressionsArchiveOutput:
    object: str
    id: str
    status: str
    filter: DashboardInstanceProtoGuardSuppressionsArchiveOutputFilter
    created_at: datetime
    updated_at: datetime
    reason: Optional[str] = None
    provider_id: Optional[str] = None
    tool_key: Optional[str] = None
    content_hash: Optional[str] = None
    expires_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None


class mapDashboardInstanceProtoGuardSuppressionsArchiveOutputFilter:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsArchiveOutputFilter:
        return DashboardInstanceProtoGuardSuppressionsArchiveOutputFilter(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsArchiveOutputFilter, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardSuppressionsArchiveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsArchiveOutput:
        return DashboardInstanceProtoGuardSuppressionsArchiveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        reason=data.get('reason'),
        filter=mapDashboardInstanceProtoGuardSuppressionsArchiveOutputFilter.from_dict(data.get('filter')) if data.get('filter') else None,
        provider_id=data.get('provider_id'),
        tool_key=data.get('tool_key'),
        content_hash=data.get('content_hash'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsArchiveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

