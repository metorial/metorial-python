from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmAccountsPreviewOutputAccountsProvider:
    type: str
    name: str
@dataclass
class ManagementInstanceScmAccountsPreviewOutputAccounts:
    object: str
    provider: ManagementInstanceScmAccountsPreviewOutputAccountsProvider
    external_id: str
    name: str
    identifier: str
@dataclass
class ManagementInstanceScmAccountsPreviewOutput:
    object: str
    accounts: List[ManagementInstanceScmAccountsPreviewOutputAccounts]


class mapManagementInstanceScmAccountsPreviewOutputAccountsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewOutputAccountsProvider:
        return ManagementInstanceScmAccountsPreviewOutputAccountsProvider(
        type=data.get('type'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmAccountsPreviewOutputAccountsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmAccountsPreviewOutputAccounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewOutputAccounts:
        return ManagementInstanceScmAccountsPreviewOutputAccounts(
        object=data.get('object'),
        provider=mapManagementInstanceScmAccountsPreviewOutputAccountsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmAccountsPreviewOutputAccounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmAccountsPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmAccountsPreviewOutput:
        return ManagementInstanceScmAccountsPreviewOutput(
        object=data.get('object'),
        accounts=[mapManagementInstanceScmAccountsPreviewOutputAccounts.from_dict(item) for item in data.get('accounts', []) if item]
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

