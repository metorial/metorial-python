from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsUpdateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[PortalsUpdateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class PortalsUpdateOutputUrls:
    type: str
    url: str
@dataclass
class PortalsUpdateOutputBrand:
    image: str
    name: str
@dataclass
class PortalsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: PortalsUpdateOutputAuth
    urls: List[PortalsUpdateOutputUrls]
    brand: PortalsUpdateOutputBrand
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsUpdateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputAuthAllowedRedirectUrlFilters:
        return PortalsUpdateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputAuth:
        return PortalsUpdateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapPortalsUpdateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputUrls:
        return PortalsUpdateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutputBrand:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutputBrand:
        return PortalsUpdateOutputBrand(
        image=data.get('image'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutputBrand, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateOutput:
        return PortalsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapPortalsUpdateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsUpdateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        brand=mapPortalsUpdateOutputBrand.from_dict(data.get('brand')) if data.get('brand') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsUpdateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[PortalsUpdateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None


class mapPortalsUpdateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateBodyAllowedRedirectUrlFilters:
        return PortalsUpdateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsUpdateBody:
        return PortalsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapPortalsUpdateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[PortalsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

