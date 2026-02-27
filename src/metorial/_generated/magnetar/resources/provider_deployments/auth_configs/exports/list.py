from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsAuthConfigsExportsListOutputItems:
    object: str
    id: str
    note: str
    provider_auth_config_id: str
    value: Dict[str, Any]
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsAuthConfigsExportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderDeploymentsAuthConfigsExportsListOutput:
    items: List[ProviderDeploymentsAuthConfigsExportsListOutputItems]
    pagination: ProviderDeploymentsAuthConfigsExportsListOutputPagination


class mapProviderDeploymentsAuthConfigsExportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsExportsListOutputItems:
        return ProviderDeploymentsAuthConfigsExportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        value=data.get('value'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsExportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsExportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsExportsListOutputPagination:
        return ProviderDeploymentsAuthConfigsExportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsExportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsExportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsExportsListOutput:
        return ProviderDeploymentsAuthConfigsExportsListOutput(
        items=[mapProviderDeploymentsAuthConfigsExportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderDeploymentsAuthConfigsExportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsExportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsAuthConfigsExportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProviderDeploymentsAuthConfigsExportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsExportsListQuery:
        return ProviderDeploymentsAuthConfigsExportsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsExportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
