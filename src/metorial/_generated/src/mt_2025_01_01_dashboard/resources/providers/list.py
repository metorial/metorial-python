from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersListOutput:
    items: List[Dict[str, Any]]
    pagination: ProvidersListOutputPagination


class mapProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutputPagination:
        return ProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListOutput:
        return ProvidersListOutput(
        items=data.get('items', []),
        pagination=mapProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersListQueryCapabilities:
    supports_config: Optional[bool] = None
    supports_auth: Optional[bool] = None
    supports_oauth: Optional[bool] = None
    supports_callbacks: Optional[bool] = None
    supports_oauth_auto_registration: Optional[bool] = None
    supports_auth_export: Optional[bool] = None
    supports_auth_import: Optional[bool] = None
@dataclass
class ProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    capabilities: Optional[ProvidersListQueryCapabilities] = None


class mapProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersListQuery:
        return ProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        capabilities=mapProvidersListQueryCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

