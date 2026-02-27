from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsTools:
    object: str
    id: str
    name: str
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
    output_schema: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods:
    object: str
    id: str
    type: str
    name: str
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
    scopes: Optional[List[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes]] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItems:
    object: str
    id: str
    name: str
    tools: List[ManagementInstanceProvidersSpecificationsListOutputItemsTools]
    auth_methods: List[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    config_schema: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProvidersSpecificationsListOutput:
    items: List[ManagementInstanceProvidersSpecificationsListOutputItems]
    pagination: ManagementInstanceProvidersSpecificationsListOutputPagination


class mapManagementInstanceProvidersSpecificationsListOutputItemsTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsTools:
        return ManagementInstanceProvidersSpecificationsListOutputItemsTools(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        title=data.get('title'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        output_schema=data.get('output_schema'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes:
        return ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods:
        return ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        scopes=[mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItems:
        return ManagementInstanceProvidersSpecificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        tools=[mapManagementInstanceProvidersSpecificationsListOutputItemsTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputPagination:
        return ManagementInstanceProvidersSpecificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutput:
        return ManagementInstanceProvidersSpecificationsListOutput(
        items=[mapManagementInstanceProvidersSpecificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProvidersSpecificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProvidersSpecificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceProvidersSpecificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListQuery:
        return ManagementInstanceProvidersSpecificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
