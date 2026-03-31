from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmConnectionsListOutputItemsExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ManagementInstanceScmConnectionsListOutputItems:
    object: str
    id: str
    provider: str
    external_account: ManagementInstanceScmConnectionsListOutputItemsExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None
@dataclass
class ManagementInstanceScmConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceScmConnectionsListOutput:
    items: List[ManagementInstanceScmConnectionsListOutputItems]
    pagination: ManagementInstanceScmConnectionsListOutputPagination


class mapManagementInstanceScmConnectionsListOutputItemsExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsListOutputItemsExternalAccount:
        return ManagementInstanceScmConnectionsListOutputItemsExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsListOutputItemsExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsListOutputItems:
        return ManagementInstanceScmConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapManagementInstanceScmConnectionsListOutputItemsExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsListOutputPagination:
        return ManagementInstanceScmConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsListOutput:
        return ManagementInstanceScmConnectionsListOutput(
        items=[mapManagementInstanceScmConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceScmConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceScmConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsListQuery:
        return ManagementInstanceScmConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

