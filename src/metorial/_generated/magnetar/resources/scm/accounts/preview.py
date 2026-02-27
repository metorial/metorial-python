from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmAccountsPreviewOutputItems:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
@dataclass
class ScmAccountsPreviewOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ScmAccountsPreviewOutput:
    items: List[ScmAccountsPreviewOutputItems]
    pagination: ScmAccountsPreviewOutputPagination


class mapScmAccountsPreviewOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewOutputItems:
        return ScmAccountsPreviewOutputItems(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ScmAccountsPreviewOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmAccountsPreviewOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewOutputPagination:
        return ScmAccountsPreviewOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ScmAccountsPreviewOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmAccountsPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewOutput:
        return ScmAccountsPreviewOutput(
        items=[mapScmAccountsPreviewOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapScmAccountsPreviewOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmAccountsPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmAccountsPreviewBody:
    installation_id: str


class mapScmAccountsPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewBody:
        return ScmAccountsPreviewBody(
        installation_id=data.get('installation_id')
        )

    @staticmethod
    def to_dict(value: Union[ScmAccountsPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
