from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmAccountsPreviewOutputItems:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
@dataclass
class DashboardInstanceScmAccountsPreviewOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceScmAccountsPreviewOutput:
    items: List[DashboardInstanceScmAccountsPreviewOutputItems]
    pagination: DashboardInstanceScmAccountsPreviewOutputPagination


class mapDashboardInstanceScmAccountsPreviewOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewOutputItems:
        return DashboardInstanceScmAccountsPreviewOutputItems(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmAccountsPreviewOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmAccountsPreviewOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewOutputPagination:
        return DashboardInstanceScmAccountsPreviewOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmAccountsPreviewOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmAccountsPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewOutput:
        return DashboardInstanceScmAccountsPreviewOutput(
        items=[mapDashboardInstanceScmAccountsPreviewOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceScmAccountsPreviewOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmAccountsPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmAccountsPreviewBody:
    installation_id: str


class mapDashboardInstanceScmAccountsPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewBody:
        return DashboardInstanceScmAccountsPreviewBody(
        installation_id=data.get('installation_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmAccountsPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
