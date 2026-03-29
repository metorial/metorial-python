from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsDeleteOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class ManagementInstancePortalsDeleteOutputUrls:
    type: str
    url: str
@dataclass
class ManagementInstancePortalsDeleteOutputBrand:
    image: str
    name: str
@dataclass
class ManagementInstancePortalsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: ManagementInstancePortalsDeleteOutputAuth
    urls: List[ManagementInstancePortalsDeleteOutputUrls]
    brand: ManagementInstancePortalsDeleteOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsDeleteOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputAuth:
        return ManagementInstancePortalsDeleteOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputUrls:
        return ManagementInstancePortalsDeleteOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutputBrand:
        return ManagementInstancePortalsDeleteOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsDeleteOutput:
        return ManagementInstancePortalsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapManagementInstancePortalsDeleteOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapManagementInstancePortalsDeleteOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapManagementInstancePortalsDeleteOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

