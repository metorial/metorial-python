from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class ManagementInstanceCustomServersRemoteServersListOutputItems:
    object: str
    id: str
    remote_url: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[ManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth] = None
@dataclass
class ManagementInstanceCustomServersRemoteServersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCustomServersRemoteServersListOutput:
    items: List[ManagementInstanceCustomServersRemoteServersListOutputItems]
    pagination: ManagementInstanceCustomServersRemoteServersListOutputPagination


class mapManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth:
        return ManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth(
        config=data.get('config'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersRemoteServersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersRemoteServersListOutputItems:
        return ManagementInstanceCustomServersRemoteServersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        remote_url=data.get('remote_url'),
        provider_oauth=mapManagementInstanceCustomServersRemoteServersListOutputItemsProviderOauth.from_dict(data.get('provider_oauth')) if data.get('provider_oauth') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersRemoteServersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersRemoteServersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersRemoteServersListOutputPagination:
        return ManagementInstanceCustomServersRemoteServersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersRemoteServersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersRemoteServersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersRemoteServersListOutput:
        return ManagementInstanceCustomServersRemoteServersListOutput(
        items=[mapManagementInstanceCustomServersRemoteServersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCustomServersRemoteServersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersRemoteServersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomServersRemoteServersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceCustomServersRemoteServersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersRemoteServersListQuery:
        return ManagementInstanceCustomServersRemoteServersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersRemoteServersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

