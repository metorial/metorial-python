from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsDeleteOutputAuthAllowedRedirectUrlFilters:
    url: str
@dataclass
class PortalsDeleteOutputAuth:
    object: str
    session_expiry_time_in_seconds: float
    allowed_redirect_url_filters: List[PortalsDeleteOutputAuthAllowedRedirectUrlFilters]
@dataclass
class PortalsDeleteOutputUrls:
    type: str
    url: str
@dataclass
class PortalsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    slug: str
    auth: PortalsDeleteOutputAuth
    urls: List[PortalsDeleteOutputUrls]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsDeleteOutputAuthAllowedRedirectUrlFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsDeleteOutputAuthAllowedRedirectUrlFilters:
        return PortalsDeleteOutputAuthAllowedRedirectUrlFilters(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[PortalsDeleteOutputAuthAllowedRedirectUrlFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsDeleteOutputAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsDeleteOutputAuth:
        return PortalsDeleteOutputAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        allowed_redirect_url_filters=[mapPortalsDeleteOutputAuthAllowedRedirectUrlFilters.from_dict(item) for item in data.get('allowed_redirect_url_filters', []) if item]
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

