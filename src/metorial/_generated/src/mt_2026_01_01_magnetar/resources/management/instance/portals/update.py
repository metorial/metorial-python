from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsUpdateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class ManagementInstancePortalsUpdateOutputUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsUpdateOutputBrand:
    image: str
    name: str
@dataclass
class ManagementInstancePortalsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: ManagementInstancePortalsUpdateOutputAuth
    urls: List[ManagementInstancePortalsUpdateOutputUrls]
    brand: ManagementInstancePortalsUpdateOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsUpdateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputAuth:
        return ManagementInstancePortalsUpdateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputUrls:
        return ManagementInstancePortalsUpdateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutputBrand:
        return ManagementInstancePortalsUpdateOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateOutput:
        return ManagementInstancePortalsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapManagementInstancePortalsUpdateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsUpdateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapManagementInstancePortalsUpdateOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    session_expiry_time_in_seconds: Optional[float] = None


class mapManagementInstancePortalsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsUpdateBody:
        return ManagementInstancePortalsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

