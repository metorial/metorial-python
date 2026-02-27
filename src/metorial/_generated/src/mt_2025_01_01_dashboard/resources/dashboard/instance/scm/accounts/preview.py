from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmAccountsPreviewOutputAccountsProvider:
    type: str
    name: str
@dataclass
class DashboardInstanceScmAccountsPreviewOutputAccounts:
    object: str
    provider: DashboardInstanceScmAccountsPreviewOutputAccountsProvider
    external_id: str
    name: str
    identifier: str
@dataclass
class DashboardInstanceScmAccountsPreviewOutput:
    object: str
    accounts: List[DashboardInstanceScmAccountsPreviewOutputAccounts]


class mapDashboardInstanceScmAccountsPreviewOutputAccountsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewOutputAccountsProvider:
        return DashboardInstanceScmAccountsPreviewOutputAccountsProvider(
        type=data.get('type'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmAccountsPreviewOutputAccountsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmAccountsPreviewOutputAccounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewOutputAccounts:
        return DashboardInstanceScmAccountsPreviewOutputAccounts(
        object=data.get('object'),
        provider=mapDashboardInstanceScmAccountsPreviewOutputAccountsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmAccountsPreviewOutputAccounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmAccountsPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmAccountsPreviewOutput:
        return DashboardInstanceScmAccountsPreviewOutput(
        object=data.get('object'),
        accounts=[mapDashboardInstanceScmAccountsPreviewOutputAccounts.from_dict(item) for item in data.get('accounts', []) if item]
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
