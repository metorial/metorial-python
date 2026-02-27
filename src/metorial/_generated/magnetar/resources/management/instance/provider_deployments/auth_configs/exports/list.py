from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems:
    object: str
    id: str
    note: str
    provider_auth_config_id: str
    value: Dict[str, Any]
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutput:
    items: List[ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems]
    pagination: ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination


class mapManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems:
        return ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        value=data.get('value'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination:
        return ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsExportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutput(
        items=[mapManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderDeploymentsAuthConfigsExportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsExportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsExportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsExportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsExportsListQuery:
        return ManagementInstanceProviderDeploymentsAuthConfigsExportsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsExportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
