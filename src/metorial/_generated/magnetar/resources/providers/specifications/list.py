from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersSpecificationsListOutputItemsTools:
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
class ProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProvidersSpecificationsListOutputItemsAuthMethods:
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
    scopes: Optional[List[ProvidersSpecificationsListOutputItemsAuthMethodsScopes]] = None
@dataclass
class ProvidersSpecificationsListOutputItems:
    object: str
    id: str
    name: str
    tools: List[ProvidersSpecificationsListOutputItemsTools]
    auth_methods: List[ProvidersSpecificationsListOutputItemsAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    config_schema: Optional[Dict[str, Any]] = None
@dataclass
class ProvidersSpecificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersSpecificationsListOutput:
    items: List[ProvidersSpecificationsListOutputItems]
    pagination: ProvidersSpecificationsListOutputPagination


class mapProvidersSpecificationsListOutputItemsTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsTools:
        return ProvidersSpecificationsListOutputItemsTools(
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
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsAuthMethodsScopes:
        return ProvidersSpecificationsListOutputItemsAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsAuthMethods:
        return ProvidersSpecificationsListOutputItemsAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        scopes=[mapProvidersSpecificationsListOutputItemsAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItems:
        return ProvidersSpecificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        tools=[mapProvidersSpecificationsListOutputItemsTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapProvidersSpecificationsListOutputItemsAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputPagination:
        return ProvidersSpecificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutput:
        return ProvidersSpecificationsListOutput(
        items=[mapProvidersSpecificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersSpecificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersSpecificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProvidersSpecificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListQuery:
        return ProvidersSpecificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
