from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsUpdateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class DashboardInstancePortalsUpdateOutputUrls:
    type: str
    url: str
@dataclass
class DashboardInstancePortalsUpdateOutputBrand:
    image: str
    name: str
@dataclass
class DashboardInstancePortalsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: DashboardInstancePortalsUpdateOutputAuth
    urls: List[DashboardInstancePortalsUpdateOutputUrls]
    brand: DashboardInstancePortalsUpdateOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstancePortalsUpdateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputAuth:
        return DashboardInstancePortalsUpdateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputUrls:
        return DashboardInstancePortalsUpdateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutputBrand:
        return DashboardInstancePortalsUpdateOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateOutput:
        return DashboardInstancePortalsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapDashboardInstancePortalsUpdateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapDashboardInstancePortalsUpdateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapDashboardInstancePortalsUpdateOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    session_expiry_time_in_seconds: Optional[float] = None


class mapDashboardInstancePortalsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsUpdateBody:
        return DashboardInstancePortalsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

