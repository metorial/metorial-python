from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmReposPreviewOutputItemsAccount:
    external_id: str
    name: str
    identifier: str
    provider: str
@dataclass
class ScmReposPreviewOutputItems:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
    last_pushed_at: Optional[datetime] = None
    account: Optional[ScmReposPreviewOutputItemsAccount] = None
@dataclass
class ScmReposPreviewOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ScmReposPreviewOutput:
    items: List[ScmReposPreviewOutputItems]
    pagination: ScmReposPreviewOutputPagination


class mapScmReposPreviewOutputItemsAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewOutputItemsAccount:
        return ScmReposPreviewOutputItemsAccount(
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        provider=data.get('provider')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewOutputItemsAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposPreviewOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewOutputItems:
        return ScmReposPreviewOutputItems(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        last_pushed_at=datetime.fromisoformat(data.get('last_pushed_at')) if data.get('last_pushed_at') else None,
        account=mapScmReposPreviewOutputItemsAccount.from_dict(data.get('account')) if data.get('account') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposPreviewOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewOutputPagination:
        return ScmReposPreviewOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewOutput:
        return ScmReposPreviewOutput(
        items=[mapScmReposPreviewOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapScmReposPreviewOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmReposPreviewBody:
    installation_id: str
    external_account_id: Optional[str] = None


class mapScmReposPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewBody:
        return ScmReposPreviewBody(
        installation_id=data.get('installation_id'),
        external_account_id=data.get('external_account_id')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
