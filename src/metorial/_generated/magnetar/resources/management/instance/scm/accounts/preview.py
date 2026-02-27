from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmAccountsPreviewOutputItems:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
@dataclass
class ManagementInstanceScmAccountsPreviewOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceScmAccountsPreviewOutput:
    items: List[ManagementInstanceScmAccountsPreviewOutputItems]
    pagination: ManagementInstanceScmAccountsPreviewOutputPagination


class mapManagementInstanceScmAccountsPreviewOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewOutputItems:
        return ManagementInstanceScmAccountsPreviewOutputItems(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmAccountsPreviewOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmAccountsPreviewOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewOutputPagination:
        return ManagementInstanceScmAccountsPreviewOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmAccountsPreviewOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmAccountsPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewOutput:
        return ManagementInstanceScmAccountsPreviewOutput(
        items=[mapManagementInstanceScmAccountsPreviewOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceScmAccountsPreviewOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmAccountsPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmAccountsPreviewBody:
    installation_id: str


class mapManagementInstanceScmAccountsPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewBody:
        return ManagementInstanceScmAccountsPreviewBody(
        installation_id=data.get('installation_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmAccountsPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
