from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmConnectionsListOutputItemsExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ScmConnectionsListOutputItems:
    object: str
    id: str
    provider: str
    external_account: ScmConnectionsListOutputItemsExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None
@dataclass
class ScmConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ScmConnectionsListOutput:
    items: List[ScmConnectionsListOutputItems]
    pagination: ScmConnectionsListOutputPagination


class mapScmConnectionsListOutputItemsExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmConnectionsListOutputItemsExternalAccount:
        return ScmConnectionsListOutputItemsExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ScmConnectionsListOutputItemsExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmConnectionsListOutputItems:
        return ScmConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapScmConnectionsListOutputItemsExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmConnectionsListOutputPagination:
        return ScmConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ScmConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmConnectionsListOutput:
        return ScmConnectionsListOutput(
        items=[mapScmConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapScmConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapScmConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmConnectionsListQuery:
        return ScmConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ScmConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

