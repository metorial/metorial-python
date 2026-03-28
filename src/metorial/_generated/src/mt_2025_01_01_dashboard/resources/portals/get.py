from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsGetOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class PortalsGetOutputUrls:
    type: str
    url: str
@dataclass
class PortalsGetOutputBrand:
    image: str
    name: str
@dataclass
class PortalsGetOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: PortalsGetOutputAuth
    urls: List[PortalsGetOutputUrls]
    brand: PortalsGetOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsGetOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsGetOutputAuth:
        return PortalsGetOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[PortalsGetOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsGetOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsGetOutputUrls:
        return PortalsGetOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsGetOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsGetOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsGetOutputBrand:
        return PortalsGetOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[PortalsGetOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsGetOutput:
        return PortalsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapPortalsGetOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsGetOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapPortalsGetOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

