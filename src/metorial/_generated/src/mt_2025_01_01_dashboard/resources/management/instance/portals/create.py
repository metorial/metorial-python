from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsCreateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class ManagementInstancePortalsCreateOutputUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsCreateOutputBrand:
    image: str
    name: str
@dataclass
class ManagementInstancePortalsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: ManagementInstancePortalsCreateOutputAuth
    urls: List[ManagementInstancePortalsCreateOutputUrls]
    brand: ManagementInstancePortalsCreateOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsCreateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputAuth:
        return ManagementInstancePortalsCreateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputUrls:
        return ManagementInstancePortalsCreateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutputBrand:
        return ManagementInstancePortalsCreateOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateOutput:
        return ManagementInstancePortalsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapManagementInstancePortalsCreateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsCreateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapManagementInstancePortalsCreateOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsCreateBody:
    name: str
    description: Optional[str] = None
    session_expiry_time_in_seconds: Optional[float] = None


class mapManagementInstancePortalsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsCreateBody:
        return ManagementInstancePortalsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

