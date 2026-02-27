from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProvidersGetOutputPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProvidersGetOutputCurrentVersion:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceProvidersGetOutput:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    publisher: Optional[DashboardInstanceProvidersGetOutputPublisher] = None
    current_version: Optional[DashboardInstanceProvidersGetOutputCurrentVersion] = None


class mapDashboardInstanceProvidersGetOutputPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputPublisher:
        return DashboardInstanceProvidersGetOutputPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputCurrentVersion:
        return DashboardInstanceProvidersGetOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutput:
        return DashboardInstanceProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        publisher=mapDashboardInstanceProvidersGetOutputPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapDashboardInstanceProvidersGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
