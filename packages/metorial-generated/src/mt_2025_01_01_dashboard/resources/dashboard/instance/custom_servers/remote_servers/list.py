from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class DashboardInstanceCustomServersRemoteServersListOutputItems:
    object: str
    id: str
    remote_url: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[DashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth] = None
@dataclass
class DashboardInstanceCustomServersRemoteServersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCustomServersRemoteServersListOutput:
    items: List[DashboardInstanceCustomServersRemoteServersListOutputItems]
    pagination: DashboardInstanceCustomServersRemoteServersListOutputPagination


class mapDashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth:
        return DashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth(
        config=data.get('config'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersRemoteServersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersListOutputItems:
        return DashboardInstanceCustomServersRemoteServersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        remote_url=data.get('remote_url'),
        provider_oauth=mapDashboardInstanceCustomServersRemoteServersListOutputItemsProviderOauth.from_dict(data.get('provider_oauth')) if data.get('provider_oauth') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersRemoteServersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersListOutputPagination:
        return DashboardInstanceCustomServersRemoteServersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersRemoteServersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersListOutput:
        return DashboardInstanceCustomServersRemoteServersListOutput(
        items=[mapDashboardInstanceCustomServersRemoteServersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCustomServersRemoteServersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomServersRemoteServersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceCustomServersRemoteServersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersListQuery:
        return DashboardInstanceCustomServersRemoteServersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

