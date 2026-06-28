from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersTriggersListOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersTriggersListOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersTriggersListOutputItems:
    object: str
    id: str
    key: str
    name: str
    invocation: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ProvidersTriggersListOutputItemsInputSchema] = None
    output_schema: Optional[ProvidersTriggersListOutputItemsOutputSchema] = None
@dataclass
class ProvidersTriggersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersTriggersListOutput:
    items: List[ProvidersTriggersListOutputItems]
    pagination: ProvidersTriggersListOutputPagination


class mapProvidersTriggersListOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersListOutputItemsInputSchema:
        return ProvidersTriggersListOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersListOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersTriggersListOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersListOutputItemsOutputSchema:
        return ProvidersTriggersListOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersListOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersTriggersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersListOutputItems:
        return ProvidersTriggersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapProvidersTriggersListOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersTriggersListOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersTriggersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersListOutputPagination:
        return ProvidersTriggersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersTriggersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersListOutput:
        return ProvidersTriggersListOutput(
        items=[mapProvidersTriggersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersTriggersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersTriggersListQuery:
    provider_version_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProvidersTriggersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersListQuery:
        return ProvidersTriggersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

