from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsDeleteOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class PortalsDeleteOutputUrls:
    type: str
    url: str
@dataclass
class PortalsDeleteOutputBrand:
    image: str
    name: str
@dataclass
class PortalsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: PortalsDeleteOutputAuth
    urls: List[PortalsDeleteOutputUrls]
    brand: PortalsDeleteOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsDeleteOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsDeleteOutputAuth:
        return PortalsDeleteOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[PortalsDeleteOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsDeleteOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsDeleteOutputUrls:
        return PortalsDeleteOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsDeleteOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsDeleteOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsDeleteOutputBrand:
        return PortalsDeleteOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[PortalsDeleteOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsDeleteOutput:
        return PortalsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapPortalsDeleteOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsDeleteOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapPortalsDeleteOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

