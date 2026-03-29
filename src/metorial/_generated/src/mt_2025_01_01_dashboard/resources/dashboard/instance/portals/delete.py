from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsDeleteOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class DashboardInstancePortalsDeleteOutputUrls:
    type: str
    url: str
@dataclass
class DashboardInstancePortalsDeleteOutputBrand:
    image: str
    name: str
@dataclass
class DashboardInstancePortalsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: DashboardInstancePortalsDeleteOutputAuth
    urls: List[DashboardInstancePortalsDeleteOutputUrls]
    brand: DashboardInstancePortalsDeleteOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstancePortalsDeleteOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsDeleteOutputAuth:
        return DashboardInstancePortalsDeleteOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsDeleteOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsDeleteOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsDeleteOutputUrls:
        return DashboardInstancePortalsDeleteOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsDeleteOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsDeleteOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsDeleteOutputBrand:
        return DashboardInstancePortalsDeleteOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsDeleteOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsDeleteOutput:
        return DashboardInstancePortalsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapDashboardInstancePortalsDeleteOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapDashboardInstancePortalsDeleteOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapDashboardInstancePortalsDeleteOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

