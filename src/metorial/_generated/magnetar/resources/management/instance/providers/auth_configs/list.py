from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersAuthConfigsListOutputItems:
    object: str
    id: str
    type: str
    provider_id: str
    provider_auth_method_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class ManagementInstanceProvidersAuthConfigsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProvidersAuthConfigsListOutput:
    items: List[ManagementInstanceProvidersAuthConfigsListOutputItems]
    pagination: ManagementInstanceProvidersAuthConfigsListOutputPagination


class mapManagementInstanceProvidersAuthConfigsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthConfigsListOutputItems:
        return ManagementInstanceProvidersAuthConfigsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthConfigsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersAuthConfigsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthConfigsListOutputPagination:
        return ManagementInstanceProvidersAuthConfigsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthConfigsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersAuthConfigsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthConfigsListOutput:
        return ManagementInstanceProvidersAuthConfigsListOutput(
        items=[mapManagementInstanceProvidersAuthConfigsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProvidersAuthConfigsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthConfigsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProvidersAuthConfigsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_auth_method_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceProvidersAuthConfigsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthConfigsListQuery:
        return ManagementInstanceProvidersAuthConfigsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthConfigsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
