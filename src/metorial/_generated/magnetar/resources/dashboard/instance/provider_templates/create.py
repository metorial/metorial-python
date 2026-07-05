from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderTemplatesCreateOutput:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    integration_id: Optional[str] = None


class mapDashboardInstanceProviderTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderTemplatesCreateOutput:
        return DashboardInstanceProviderTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderTemplatesCreateBody:
    name: str
    integration_id: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceProviderTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderTemplatesCreateBody:
        return DashboardInstanceProviderTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

