from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmAccountsPreviewOutputAccountsProvider:
    type: str
    name: str
@dataclass
class ScmAccountsPreviewOutputAccounts:
    object: str
    provider: ScmAccountsPreviewOutputAccountsProvider
    external_id: str
    name: str
    identifier: str
@dataclass
class ScmAccountsPreviewOutput:
    object: str
    accounts: List[ScmAccountsPreviewOutputAccounts]


class mapScmAccountsPreviewOutputAccountsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewOutputAccountsProvider:
        return ScmAccountsPreviewOutputAccountsProvider(
        type=data.get('type'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ScmAccountsPreviewOutputAccountsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmAccountsPreviewOutputAccounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewOutputAccounts:
        return ScmAccountsPreviewOutputAccounts(
        object=data.get('object'),
        provider=mapScmAccountsPreviewOutputAccountsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ScmAccountsPreviewOutputAccounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmAccountsPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmAccountsPreviewOutput:
        return ScmAccountsPreviewOutput(
        object=data.get('object'),
        accounts=[mapScmAccountsPreviewOutputAccounts.from_dict(item) for item in data.get('accounts', []) if item]
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

