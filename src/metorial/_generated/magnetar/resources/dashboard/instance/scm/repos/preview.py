from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmReposPreviewOutputItemsAccount:
    external_id: str
    name: str
    identifier: str
    provider: str
@dataclass
class DashboardInstanceScmReposPreviewOutputItems:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
    last_pushed_at: Optional[datetime] = None
    account: Optional[DashboardInstanceScmReposPreviewOutputItemsAccount] = None
@dataclass
class DashboardInstanceScmReposPreviewOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceScmReposPreviewOutput:
    items: List[DashboardInstanceScmReposPreviewOutputItems]
    pagination: DashboardInstanceScmReposPreviewOutputPagination


class mapDashboardInstanceScmReposPreviewOutputItemsAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewOutputItemsAccount:
        return DashboardInstanceScmReposPreviewOutputItemsAccount(
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        provider=data.get('provider')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewOutputItemsAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmReposPreviewOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewOutputItems:
        return DashboardInstanceScmReposPreviewOutputItems(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        last_pushed_at=datetime.fromisoformat(data.get('last_pushed_at')) if data.get('last_pushed_at') else None,
        account=mapDashboardInstanceScmReposPreviewOutputItemsAccount.from_dict(data.get('account')) if data.get('account') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmReposPreviewOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewOutputPagination:
        return DashboardInstanceScmReposPreviewOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmReposPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewOutput:
        return DashboardInstanceScmReposPreviewOutput(
        items=[mapDashboardInstanceScmReposPreviewOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceScmReposPreviewOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmReposPreviewBody:
    installation_id: str
    external_account_id: Optional[str] = None


class mapDashboardInstanceScmReposPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewBody:
        return DashboardInstanceScmReposPreviewBody(
        installation_id=data.get('installation_id'),
        external_account_id=data.get('external_account_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
