from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmReposPreviewOutputItemsAccount:
    external_id: str
    name: str
    identifier: str
    provider: str
@dataclass
class ManagementInstanceScmReposPreviewOutputItems:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
    last_pushed_at: Optional[datetime] = None
    account: Optional[ManagementInstanceScmReposPreviewOutputItemsAccount] = None
@dataclass
class ManagementInstanceScmReposPreviewOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceScmReposPreviewOutput:
    items: List[ManagementInstanceScmReposPreviewOutputItems]
    pagination: ManagementInstanceScmReposPreviewOutputPagination


class mapManagementInstanceScmReposPreviewOutputItemsAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutputItemsAccount:
        return ManagementInstanceScmReposPreviewOutputItemsAccount(
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        provider=data.get('provider')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutputItemsAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposPreviewOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutputItems:
        return ManagementInstanceScmReposPreviewOutputItems(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        last_pushed_at=datetime.fromisoformat(data.get('last_pushed_at')) if data.get('last_pushed_at') else None,
        account=mapManagementInstanceScmReposPreviewOutputItemsAccount.from_dict(data.get('account')) if data.get('account') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposPreviewOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutputPagination:
        return ManagementInstanceScmReposPreviewOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutput:
        return ManagementInstanceScmReposPreviewOutput(
        items=[mapManagementInstanceScmReposPreviewOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceScmReposPreviewOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmReposPreviewBody:
    installation_id: str
    external_account_id: Optional[str] = None


class mapManagementInstanceScmReposPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewBody:
        return ManagementInstanceScmReposPreviewBody(
        installation_id=data.get('installation_id'),
        external_account_id=data.get('external_account_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
