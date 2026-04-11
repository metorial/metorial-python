from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsCreateOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsCreateOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[PortalsCreateOutputAuthAllowedRedirectUrlFilters]
@dataclass
class PortalsCreateOutputUrls:
    type: str
    url: str
@dataclass
class PortalsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: PortalsCreateOutputAuth
    urls: List[PortalsCreateOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsCreateOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsCreateOutputAuthAllowedRedirectUrlFilters:
        return PortalsCreateOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsCreateOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsCreateOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsCreateOutputAuth:
        return PortalsCreateOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapPortalsCreateOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[PortalsCreateOutputAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsCreateOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsCreateOutputUrls:
        return PortalsCreateOutputUrls(
        type=data.get('type'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsCreateOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsCreateOutput:
        return PortalsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        auth=mapPortalsCreateOutputAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        urls=[mapPortalsCreateOutputUrls.from_dict(item) for item in data.get('urls', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsCreateBodyAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsCreateBody:
    name: str
    description: Optional[str] = None
    allowed_redirect_url_filters: Optional[List[PortalsCreateBodyAllowedRedirectUrlFilters]] = None
    session_expiry_time_in_seconds: Optional[float] = None


class mapPortalsCreateBodyAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsCreateBodyAllowedRedirectUrlFilters:
        return PortalsCreateBodyAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsCreateBodyAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsCreateBody:
        return PortalsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        allowed_redirect_url_filters=[mapPortalsCreateBodyAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item],
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds')
        )

    @staticmethod
    def to_dict(value: Union[PortalsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

