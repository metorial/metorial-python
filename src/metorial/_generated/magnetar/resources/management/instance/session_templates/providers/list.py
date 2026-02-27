from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionTemplatesProvidersListOutputItems:
    object: str
    id: str
    session_template_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
    provider_deployment_name: Optional[str] = None
    provider_config_name: Optional[str] = None
    provider_auth_config_name: Optional[str] = None
@dataclass
class ManagementInstanceSessionTemplatesProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionTemplatesProvidersListOutput:
    items: List[ManagementInstanceSessionTemplatesProvidersListOutputItems]
    pagination: ManagementInstanceSessionTemplatesProvidersListOutputPagination


class mapManagementInstanceSessionTemplatesProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesProvidersListOutputItems:
        return ManagementInstanceSessionTemplatesProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        session_template_id=data.get('session_template_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_deployment_name=data.get('provider_deployment_name'),
        provider_config_name=data.get('provider_config_name'),
        provider_auth_config_name=data.get('provider_auth_config_name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesProvidersListOutputPagination:
        return ManagementInstanceSessionTemplatesProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesProvidersListOutput:
        return ManagementInstanceSessionTemplatesProvidersListOutput(
        items=[mapManagementInstanceSessionTemplatesProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionTemplatesProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionTemplatesProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSessionTemplatesProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesProvidersListQuery:
        return ManagementInstanceSessionTemplatesProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
