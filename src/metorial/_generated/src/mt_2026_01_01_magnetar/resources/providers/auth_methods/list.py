from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersAuthMethodsListOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersAuthMethodsListOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersAuthMethodsListOutputItemsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProvidersAuthMethodsListOutputItems:
    object: str
    id: str
    type: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ProvidersAuthMethodsListOutputItemsInputSchema] = None
    output_schema: Optional[ProvidersAuthMethodsListOutputItemsOutputSchema] = None
    scopes: Optional[List[ProvidersAuthMethodsListOutputItemsScopes]] = None
@dataclass
class ProvidersAuthMethodsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersAuthMethodsListOutput:
    items: List[ProvidersAuthMethodsListOutputItems]
    pagination: ProvidersAuthMethodsListOutputPagination


class mapProvidersAuthMethodsListOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListOutputItemsInputSchema:
        return ProvidersAuthMethodsListOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsListOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListOutputItemsOutputSchema:
        return ProvidersAuthMethodsListOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsListOutputItemsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListOutputItemsScopes:
        return ProvidersAuthMethodsListOutputItemsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListOutputItemsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListOutputItems:
        return ProvidersAuthMethodsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProvidersAuthMethodsListOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersAuthMethodsListOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProvidersAuthMethodsListOutputItemsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListOutputPagination:
        return ProvidersAuthMethodsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListOutput:
        return ProvidersAuthMethodsListOutput(
        items=[mapProvidersAuthMethodsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersAuthMethodsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersAuthMethodsListQuery:
    provider_version_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProvidersAuthMethodsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsListQuery:
        return ProvidersAuthMethodsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
