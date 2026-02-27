from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionTemplatesUpdateOutput:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSessionTemplatesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionTemplatesUpdateOutput:
        return DashboardInstanceSessionTemplatesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionTemplatesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionTemplatesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSessionTemplatesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionTemplatesUpdateBody:
        return DashboardInstanceSessionTemplatesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionTemplatesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
