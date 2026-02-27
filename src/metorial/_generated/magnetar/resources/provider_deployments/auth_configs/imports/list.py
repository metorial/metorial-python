from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsAuthConfigsImportsListOutputItems:
    object: str
    id: str
    note: str
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = None
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None
@dataclass
class ProviderDeploymentsAuthConfigsImportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderDeploymentsAuthConfigsImportsListOutput:
    items: List[ProviderDeploymentsAuthConfigsImportsListOutputItems]
    pagination: ProviderDeploymentsAuthConfigsImportsListOutputPagination


class mapProviderDeploymentsAuthConfigsImportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsListOutputItems:
        return ProviderDeploymentsAuthConfigsImportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsImportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsListOutputPagination:
        return ProviderDeploymentsAuthConfigsImportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsImportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsListOutput:
        return ProviderDeploymentsAuthConfigsImportsListOutput(
        items=[mapProviderDeploymentsAuthConfigsImportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderDeploymentsAuthConfigsImportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsAuthConfigsImportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProviderDeploymentsAuthConfigsImportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsImportsListQuery:
        return ProviderDeploymentsAuthConfigsImportsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsImportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
