from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmInstallationListOutputItemsExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ScmInstallationListOutputItems:
    object: str
    id: str
    provider: str
    external_account: ScmInstallationListOutputItemsExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None
@dataclass
class ScmInstallationListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ScmInstallationListOutput:
    items: List[ScmInstallationListOutputItems]
    pagination: ScmInstallationListOutputPagination


class mapScmInstallationListOutputItemsExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationListOutputItemsExternalAccount:
        return ScmInstallationListOutputItemsExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationListOutputItemsExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmInstallationListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationListOutputItems:
        return ScmInstallationListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapScmInstallationListOutputItemsExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmInstallationListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationListOutputPagination:
        return ScmInstallationListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmInstallationListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationListOutput:
        return ScmInstallationListOutput(
        items=[mapScmInstallationListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapScmInstallationListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmInstallationListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapScmInstallationListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationListQuery:
        return ScmInstallationListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

