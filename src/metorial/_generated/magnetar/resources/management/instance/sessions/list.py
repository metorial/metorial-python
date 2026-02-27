from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsListOutputItemsUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsListOutputItemsProviderDeployments:
    object: str
    id: str
    provider_id: str
    name: Optional[str] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsListOutputItems:
    object: str
    id: str
    connection_status: str
    usage: ManagementInstanceSessionsListOutputItemsUsage
    provider_deployments: List[ManagementInstanceSessionsListOutputItemsProviderDeployments]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    connection_url: Optional[str] = None
    connection_key: Optional[str] = None
@dataclass
class ManagementInstanceSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsListOutput:
    items: List[ManagementInstanceSessionsListOutputItems]
    pagination: ManagementInstanceSessionsListOutputPagination


class mapManagementInstanceSessionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsUsage:
        return ManagementInstanceSessionsListOutputItemsUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItemsProviderDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsProviderDeployments:
        return ManagementInstanceSessionsListOutputItemsProviderDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsProviderDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItems:
        return ManagementInstanceSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        connection_status=data.get('connection_status'),
        usage=mapManagementInstanceSessionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        connection_url=data.get('connection_url'),
        connection_key=data.get('connection_key'),
        provider_deployments=[mapManagementInstanceSessionsListOutputItemsProviderDeployments.from_dict(item) for item in data.get('provider_deployments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputPagination:
        return ManagementInstanceSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutput:
        return ManagementInstanceSessionsListOutput(
        items=[mapManagementInstanceSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListQuery:
        return ManagementInstanceSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
